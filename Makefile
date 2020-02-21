CC=gcc
CFLAGS=-std=gnu17 -O3
DEPS=hellomake.h

swap: atomic_fswap.c
	$(CC) $(CFLAGS) $< -o $@

clean:
	rm swap
