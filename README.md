# Hex

    Sane[ish] hex utility (aka swiss army knife for hexadecimal operations). – Edit 

Usage examples:

`hex -d [file]` - hexdump file, without newlines
`hex -f pattern [file] [-q]` - find hex pattern in file. Use -q for quiet mode (don't print offsets)
`hex -c [file]` - print colorized file (with green printable strings)

When [file] is not supplied, use stdin instead
