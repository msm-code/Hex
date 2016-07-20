#!/usr/bin/python

import sys
import re

import errno


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


def colorize():
    for l in sys.stdin:
        i = 0
        for m in re.finditer('([0-9A-F]{2}){4,}|([0-9a-f]{2}){4,}', l):
            frm, to = m.span()
            sys.stdout.write(l[i:frm])
            colorhex(l[frm:to])
            i = to
        sys.stdout.write(l[i:])


def dump():
    for l in sys.stdin:
        sys.stdout.write(l.encode('hex'))
    sys.stdout.write('\n')

if __name__ == '__main__':
    try:
        if len(sys.argv) == 1:
            colorize()
        elif sys.argv[1] == '-d':
            if len(sys.argv) > 2:
                sys.stdin = open(sys.argv[2], 'rb')
            dump()
        elif sys.argv[1] == '-f':
            pattern = sys.argv[2].lower()
            data = open(sys.argv[3], 'rb').read().encode('hex')
            if data.find(pattern) >= 0:
                print sys.argv[3]
        else:
            sys.stderr.write("Usage: {} [-d]\n".format(sys.argv[0]))
    except IOError as e:
        if e.errno == errno.EPIPE:
            pass
        else:
            raise
