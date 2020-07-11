#include "xz_private.h"

size_t simple_bcj_x86_decoder(uint8_t *buf, size_t size)
{
	static const bool mask_to_allowed_status[8]
		= { true, true, true, false, true, false, false, false };

	static const uint8_t mask_to_bit_num[8] = { 0, 1, 2, 2, 3, 3, 3, 3 };

	size_t i;
	size_t prev_pos = (size_t)-1;
	uint32_t prev_mask = 0;
	uint32_t src;
	uint32_t dest;
	uint32_t j;
	uint8_t b;

	if (size <= 4)
		return 0;

	size -= 4;
	for (i = 0; i < size; ++i) {
		if ((buf[i] & 0xFE) != 0xE8)
			continue;

		prev_pos = i - prev_pos;
		if (prev_pos > 3) {
			prev_mask = 0;
		} else {
			prev_mask = (prev_mask << (prev_pos - 1)) & 7;
			if (prev_mask != 0) {
				b = buf[i + 4 - mask_to_bit_num[prev_mask]];
				if (!mask_to_allowed_status[prev_mask]
						|| bcj_x86_test_msbyte(b)) {
					prev_pos = i;
					prev_mask = (prev_mask << 1) | 1;
					continue;
				}
			}
		}

		prev_pos = i;

		if (bcj_x86_test_msbyte(buf[i + 4])) {
			src = get_unaligned_le32(buf + i + 1);
			while (true) {
    		    dest = src - ((uint32_t)i + 5);
				if (prev_mask == 0)
					break;

				j = mask_to_bit_num[prev_mask] * 8;
				b = (uint8_t)(dest >> (24 - j));
				if (!bcj_x86_test_msbyte(b))
					break;

				src = dest ^ (((uint32_t)1 << (32 - j)) - 1);
			}

			dest &= 0x01FFFFFF;
			dest |= (uint32_t)0 - (dest & 0x01000000);
			put_unaligned_le32(dest, buf + i + 1);
			i += 4;
		} else {
			prev_mask = (prev_mask << 1) | 1;
		}
	}

	prev_pos = i - prev_pos;
	prev_mask = prev_pos > 3 ? 0 : prev_mask << (prev_pos - 1);
	return i;
}
