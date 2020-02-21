# kindlib

## About
This is a miscellaneous library that I intend to populate with
tiny but useful code. At the moment, only the atomic file swap
is documented. It currently works on systems running GNU/Linux
with support to -std=gnu17

Other systems might support it, but that was not tested.

## Clone and Build:

``` bash
git clone https://github.com/condekind/kindlib.git
cd kindlib
make swap
```


## Usage

``` bash
./swap file1 file2
```
It also works with directories, so no more copying stuff around
and worrying about concurrency. The renameat2 syscall will take
care of that for us! It's especially useful for deployment:
``` bash
./swap path/to/backup path/to/production
```
