#include "xz_private.h"


static size_t
x86_code(simple_x86 *simple, uint32_t now_pos, bool is_encoder,
	 	 uint8_t *buffer, size_t size)
{
	static const bool MASK_TO_ALLOWED_STATUS[8]
		= { true, true, true, false, true, false, false, false };

	static const uint32_t MASK_TO_BIT_NUMBER[8]
			= { 0, 1, 2, 2, 3, 3, 3, 3 };

	uint32_t prev_mask = simple->prev_mask;
	uint32_t prev_pos = simple->prev_pos;

	if (size < 5)
		return 0;

	if (now_pos - prev_pos > 5)
		prev_pos = now_pos - 5;

	const size_t limit = size - 5;
	size_t buffer_pos = 0;

	while (buffer_pos <= limit) {
		uint8_t b = buffer[buffer_pos];
		if (b != 0xE8 && b != 0xE9) {
			++buffer_pos;
			continue;
		}

		const uint32_t offset = now_pos + (uint32_t)(buffer_pos)
				- prev_pos;
		prev_pos = now_pos + (uint32_t)(buffer_pos);

		if (offset > 5) {
			prev_mask = 0;
		} else {
			for (uint32_t i = 0; i < offset; ++i) {
				prev_mask &= 0x77;
				prev_mask <<= 1;
			}
		}

		b = buffer[buffer_pos + 4];

		if (bcj_x86_test_msbyte(b)
			&& MASK_TO_ALLOWED_STATUS[(prev_mask >> 1) & 0x7]
				&& (prev_mask >> 1) < 0x10) {

			uint32_t src = ((uint32_t)(b) << 24)
				| ((uint32_t)(buffer[buffer_pos + 3]) << 16)
				| ((uint32_t)(buffer[buffer_pos + 2]) << 8)
				| (buffer[buffer_pos + 1]);

			uint32_t dest;
			while (true) {
				if (is_encoder)
					dest = src + (now_pos + (uint32_t)(
							buffer_pos) + 5);
				else
					dest = src - (now_pos + (uint32_t)(
							buffer_pos) + 5);

				if (prev_mask == 0)
					break;

				const uint32_t i = MASK_TO_BIT_NUMBER[
						prev_mask >> 1];

				b = (uint8_t)(dest >> (24 - i * 8));

				if (!bcj_x86_test_msbyte(b))
					break;

				src = dest ^ ((1U << (32 - i * 8)) - 1);
			}

			buffer[buffer_pos + 4]
					= (uint8_t)(~(((dest >> 24) & 1) - 1));
			buffer[buffer_pos + 3] = (uint8_t)(dest >> 16);
			buffer[buffer_pos + 2] = (uint8_t)(dest >> 8);
			buffer[buffer_pos + 1] = (uint8_t)(dest);
			buffer_pos += 5;
			prev_mask = 0;

		} else {
			++buffer_pos;
			prev_mask |= 1;
			if (bcj_x86_test_msbyte(b))
				prev_mask |= 0x10;
		}
	}

	simple->prev_mask = prev_mask;
	simple->prev_pos = prev_pos;

	return buffer_pos;
}

void bcj_x86_simple_x86_init(simple_x86 * simple)
{
	simple->prev_mask = 0;
	simple->prev_pos = (uint32_t)(-5);
}

size_t bcj_x86_encoder(simple_x86 * simple, uint8_t *buf, size_t size)
{
	size_t now_pos = 0;
    size_t pos = x86_code(simple, now_pos, true, buf, size);
    return pos;
}

size_t bcj_x86_decoder(simple_x86* simple, uint8_t *buf, size_t size)
{
	size_t now_pos = 0;
    size_t pos = x86_code(simple, now_pos, false, buf, size);
    return pos;
}
