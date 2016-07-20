#!/usr/bin/python

import sys
import re
import argparse


def chunks(str, n):
    return [str[i*n:(i+1)*n] for i in range(len(str)/n)]


def colorhex(str):
    prevcol = ''
    for chk in chunks(str, 2):
        v = int(chk, 16)
        if 0x20 <= v <= 0x7f:
            color = '32'
        elif v < 0x20:
            color = '33'
        elif v < 0xd0:
            color = '31'
        else:
            color = '31'
        if color != prevcol:
            sys.stdout.write('\033[{}m'.format(color))
            prevcol = color
        sys.stdout.write(chk)
    sys.stdout.write('\033[0m')


def hex_chunks(line):
    return re.finditer('([0-9A-F]{2}){4,}|([0-9a-f]{2}){4,}', line)


def colorize(infile, args):
    for l in infile:
        i = 0
        for m in hex_chunks(l):
            frm, to = m.span()
            sys.stdout.write(l[i:frm])
            colorhex(l[frm:to])
            i = to
        sys.stdout.write(l[i:])


def find(infile, args):
    sought = args.find.decode('hex')
    ndx = infile.read().find(sought)
    if ndx >= 0:
        if args.quiet:
            print args.file
        else:
            print '{ndx:<5} {ndx:<5x} {}'.format(args.file, ndx=ndx)


def dump(infile, args):
    for l in infile:
        sys.stdout.write(l.encode('hex'))
    sys.stdout.write('\n')


def reverse(infile, args):
    for l in infile:
        sys.stdout.write(l.strip().decode('hex'))


def parse_args():
    parser = argparse.ArgumentParser(prog='hex')
    parser.add_argument('--dump', '-d', action='store_true')
    parser.add_argument('--reverse', '-r', action='store_true')
    parser.add_argument('--colorize', '-c', action='store_true')
    parser.add_argument('--find', '-f', type=str)
    parser.add_argument('--quiet', '-q', action='store_true')
    parser.add_argument('file', nargs='?')
    return parser.parse_args()


def process_args(args):
    if args.file:
        infile = open(args.file, 'rb')
    else:
        infile = sys.stdin

    if args.colorize:
        func = colorize
    elif args.find:
        func = find
    elif args.reverse:
        func = reverse
    else:
        func = dump

    return infile, func


def main():
    args = parse_args()
    infile, func = process_args(args)
    func(infile, args)


if __name__ == '__main__':
    main()
