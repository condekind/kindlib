#ifndef ATOMIC_SWAP
#define ATOMIC_SWAP

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <assert.h>
#include <limits.h>


// Macro stringify
#define xstr(s) str(s)
#define str(s) #s

// Using pathconf to set PATH_MAX if _PC_PATH_MAX is defined
# if !defined PATH_MAX && defined _PC_PATH_MAX
#   define PATH_MAX ( (pathconf(".", _PC_PATH_MAX) < 1 ) ? 127 \
                     : pathconf(".", _PC_PATH_MAX) )
# endif

// "Safe" small value, if the above fails.
#ifndef PATH_MAX
#define PATH_MAX 63
#endif

// This flag is responsible for the swap operation. See `man renameat2`.
#ifndef RENAME_EXCHANGE
#define RENAME_EXCHANGE (1 << 1)
#endif

#endif
