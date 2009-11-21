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
def getword():
    import sys
    from random import Random

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
    import os, sys
    filename = os.path.join("", "pwlist.txt")
    fp = open(filename, "w")
    res = ""
    count = 0
    # 100 paswörter erstellen
    for i in range(0,140):
        w1 = getword()
        w2 = getword()
        w3 = getword()
        w4 = getword()
        res += str(count+1) + "\t"+ w1 + "\t" +str(count+2) + "\t"+ w2 + "\t" +str(count+3) + "\t"+w3 + "\t"+ str(count+4) + "\t" + w4 + "\n"
        print str(count+1) + "\t"+ w1 + "\t" +str(count+2) + "\t"+ w2 + "\t" +str(count+3) + "\t"+w3 + "\t"+ str(count+4) + "\t" + w4 + "\n"
        count += 4
    fp.write(res)
    fp.close()
        
    return 0

if __name__ == '__main__': main()
