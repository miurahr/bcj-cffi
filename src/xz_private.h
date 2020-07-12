#include <stddef.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

#ifndef simple_x86
typedef struct {
	uint32_t prev_mask;
	uint32_t prev_pos;
} simple_x86;
#endif