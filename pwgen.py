#!/usr/bin/env python
# coding=utf-8
#
#       pwgen.py
#       
#       Copyright 2008 Dirk B. <dirkbo@googlemail.com>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.


def is_pattern(pattern):
    """
    checks whether pattern is a valid passwordpattern
    e.g. aaaAAbbcc
    """
    for p in pattern:
        if p == 'a':
            continue
        elif p == 'A':
            continue
        elif p == 'b':
            continue
        elif p == 'c':
            continue
        else:
            return False
    return True


def pwgen(pattern, a='abcdefghijklmnopqrstuvwxyz', A='ABCDEFGHIJKLMNOPQRSTUVWXYZ', b='1234567890', c='!@$%&=_-+#.:)(/*#?'):
    """
    generates a password with the given pattern
    
    Args:
        pattern:
            pattern must contain the characters 'a', 'A', 'b' or 'c'
            'a' = small latin characters
            'A' = capital latin characters
            'b' = numbers
            'c' = special characters ! $ % & = _ - + #
        
        a:
            range of small latin characters
        A:
            range of capital latin characters
        b:
            range of numbers
        c:
            range of special characters
    
    Returns:
        string
    """
    import random
    
    pw = []
    rand = random.Random()
    
    for p in pattern:
        if p == 'a':
            pw.append(rand.choice(a))
        elif p == 'A':
            pw.append(rand.choice(A))
        elif p == 'b':
            pw.append(rand.choice(b))
        elif p == 'c':
            pw.append(rand.choice(c))
    
    return ''.join(pw)
        

def getword(pattern=None):
    import sys
    from random import Random
    
    if pattern:
        return pwgen(pattern)
    
    
    bereich = "qwertzuiopasdfghjklyxcvbnm"
    #bereich  += "QWERTZUIOPASDFGHJKLYXCVBNM"
    zbereich = "1234567890"
    
    word = ""
    rng = Random()
    
    for i in range(0, 5):
        word += rng.choice(bereich)
    for i in range(0, 3):
        word += rng.choice(zbereich)
    for i in range(0, 3):
        word += rng.choice(bereich)
    
    return word


def main():
    import os
    import sys
    import argparse
    
    res = ""
    count = 0
    lines = 140
    perline = 4
    seperator = "\t"
    offset = 0
    user_pattern = "aaaabbbaaa"

    parser = argparse.ArgumentParser(description="Generates a text file with a numbered List of Passwords.")

    parser.add_argument(
        '--file',
        default="pwlist.txt",
        help='Filename to save list of Passwords to. default: pwlist.txt'
    )

    parser.add_argument(
        '--pattern',
        default="aaaabbbaaa",
        help='Provide a pattern for Password creation. aA letters, b Numerics, c Symbols, default: aaaabbbaaa'
    )

    parser.add_argument(
        '--lines',
        default=140,
        help='Number of lines with passwords to write in file. Default: 140'
    )

    parser.add_argument(
        '--perline',
        default=4,
        help='Number of passwords per Line to write in file. Default: 4'
    )

    parser.add_argument(
        '--offset',
        default=0,
        help='Start numbered Password list with this number. Default: 0'
    )

    opt_args = parser.parse_args()  

    user_pattern = opt_args.pattern

    lines = int(opt_args.lines)

    count = int(opt_args.offset)

    perline = int(opt_args.perline)

    filename = os.path.join("", opt_args.file)	
    fp = open(filename, "w")
    
    if not is_pattern(user_pattern):
        user_pattern = "aaaabbbaaa"
        
    for i in range(0, lines):
        is_start = True
        current_line = ""
        for j in range(0, perline):
            w = getword(pattern=user_pattern)
            count += 1
            if is_start:
                is_start = False
            else:
                current_line += seperator
            current_line += "{number:04d} {seperator} {word}".format(number=count, seperator=seperator, word=w)
        current_line += "\n"

        res += current_line
        print(current_line)
    fp.write(res)
    fp.close()
        
    return 0


if __name__ == '__main__':
    main()
