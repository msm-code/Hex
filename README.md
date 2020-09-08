# Hex

    Sane[ish] hex utility (aka swiss army knife for hexadecimal operations).

## Usage:

```
$ hex --help
usage: hex [-h] [--dump] [--dump-pretty] [--reverse] [--colorize]
           [--colorize-dword] [--find FIND] [--find-all FIND_ALL] [--sanitize]
           [--quiet]
           [file]

positional arguments:
  file

optional arguments:
  -h, --help            show this help message and exit
  --dump, -d
  --dump-pretty, -D
  --reverse, -r
  --colorize, -c
  --colorize-dword
  --find FIND, -f FIND
  --find-all FIND_ALL, -F FIND_ALL
  --sanitize, -s
  --quiet, -q
```

When `[file]` is not supplied, use stdin instead

## Why?

For the most common use case, it's easier to type `hex` than `xxd -ps`, I prefer `hex -s` to `cat -v`, like colors in `hex -c`, and `hex -f` is almost like a binary grep. Overall, it has all the binary features that I need, and when it doesn't I can always add them.
