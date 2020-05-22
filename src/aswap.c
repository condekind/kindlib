/*
 * Do not run this within NFS:
 *   https://manpages.debian.org/testing/manpages-dev/renameat2.2.en.html#BUGS 
*/

#define _GNU_SOURCE
#include "aswap.h"

int ierr(int err, const char *s)
{
  fprintf(stderr, "%s\n", s);
  return err;
}

inline const char *usage()
{
  return "\
  Usage: aswap file1 file2\n\n\
  -h, -H, --help          Display this menu\n\n\
  Info: PATH_MAX is set to "xstr(PATH_MAX);
}

int main(int argc, char *argv[])
{
  assert(2 < PATH_MAX);

  if(argc != 3)
    return ierr(EXIT_FAILURE, usage());

  if ( (strlen(argv[1]) >= PATH_MAX) || (strlen(argv[2]) >= PATH_MAX) )
    return ierr(EXIT_FAILURE, "Error: Long path.");

  // File path buffers
  char f1path[PATH_MAX], f2path[PATH_MAX];
  memset(f1path, 0, PATH_MAX);
  memset(f2path, 0, PATH_MAX);

  // Canonicalize paths
  if (realpath(argv[1], f1path) == NULL)
    ierr(EXIT_FAILURE, "Error: failed resolving path of file #1");
  if (realpath(argv[2], f2path) == NULL)
    ierr(EXIT_FAILURE, "Error: failed resolving path of file #2");

  // Open files for swapping
  int fd1 = open(f1path, O_PATH);
  int fd2 = open(f2path, O_PATH);

  // Atomic swap
  int err;
  if ((err = renameat2(fd1, f1path, fd2, f2path, RENAME_EXCHANGE)))
    return ierr(EXIT_FAILURE, "Error: atomic swap failed.");

  close(fd1);
  close(fd2);

  return 0;
}
