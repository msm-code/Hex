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

```
/home/msm/Projects/Hex$ head -c 50 /dev/urandom | hex
6effcd4c19492122ebcb337712bae09f11ff48301858c6872963849ebaeee4944493de07f710bc3170bc911e8a2cdb79bedb

/home/msm/Projects/Hex$ head -c 60 /dev/urandom | hex -D
00000000 d6cd31278198ae321d12af80aaa4e198 ..1'...2........
00000010 45bbc95ae042c0d7b47dd86999b55022 E..Z.B...}.i..P"
00000020 60b0ad9b34ff3df584a750bb294e0d52 `...4.=...P.)N.R
00000030 104788397337ba70c01fd46d         .G.9s7.p...m

/home/msm/Projects/Hex$ head -c 60 /dev/urandom | hex -D | hex -c
00000000 d0cb355edbf7bf7905d12764add3a092 ..5^...y..'d....
00000010 35954abaa15ce9175d5c11dc72baf98a 5.J..\..]\..r...
00000020 6e714b1204fb784c8f1ffbe60c0743da nqK...xL......C.
00000030 3b502131b6c9eb232b80d522         ;P!1...#+.."

/home/msm/Projects/Hex$ echo 692067756573732074686174277320616c6c | hex -r
i guess that's all
```

## Why?

For the most common use case, it's easier to type `hex` than `xxd -ps`, I prefer `hex -s` to `cat -v`, like colors in `hex -c`, and `hex -f` is almost like a binary grep. Overall, it has all the binary features that I need, and when it doesn't I can always add them.
