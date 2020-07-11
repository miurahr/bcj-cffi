#include <stddef.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

/* Inline functions to access unaligned unsigned 32-bit integers */
static inline uint32_t get_unaligned_le32(const uint8_t *buf)
{
	return (uint32_t)buf[0]
			| ((uint32_t)buf[1] << 8)
			| ((uint32_t)buf[2] << 16)
			| ((uint32_t)buf[3] << 24);
}

static inline void put_unaligned_le32(uint32_t val, uint8_t *buf)
{
	buf[0] = (uint8_t)val;
	buf[1] = (uint8_t)(val >> 8);
	buf[2] = (uint8_t)(val >> 16);
	buf[3] = (uint8_t)(val >> 24);
}

static inline int bcj_x86_test_msbyte(uint8_t b)
{
	return b == 0x00 || b == 0xFF;
}
