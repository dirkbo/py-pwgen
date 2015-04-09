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


def pwgen(pattern, a='abcdefghijklmnopqrstuvwxyz', A='ABCDEFGHIJKLMNOPQRSTUVWXYZ', b='1234567890', c='!$%&=_-+#'):
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
    filename = os.path.join("", "pwlist.txt")
    fp = open(filename, "w")
    res = ""
    count = 0
    # 100 paswörter erstellen
    lines = 140
    offset = 0
    user_pattern = "aaaabbbaaa"
    try:
        user_pattern = sys.argv[1]
    except:
        pass

    try:
        lines = int(sys.argv[2])
    except:
        pass

    try:
        count = int(sys.argv[3])
    except:
        pass
    
    if not is_pattern(user_pattern):
        user_pattern = "aaaabbbaaa"
        
    for i in range(0, lines):
        w1 = getword(pattern=user_pattern)
        w2 = getword(pattern=user_pattern)
        w3 = getword(pattern=user_pattern)
        w4 = getword(pattern=user_pattern)
       
        res += str(count+1) + "\t" + w1 + "\t" + str(count+2) + "\t" + w2 + "\t" + str(count+3) + "\t"+w3 + "\t" + \
            str(count+4) + "\t" + w4 + "\n"
        print str(count+1) + "\t" + w1 + "\t" + str(count+2) + "\t" + w2 + "\t" + str(count+3) + "\t"+w3 + "\t" + \
            str(count+4) + "\t" + w4 + "\n"
        count += 4
    fp.write(res)
    fp.close()
        
    return 0

if __name__ == '__main__':
    main()
