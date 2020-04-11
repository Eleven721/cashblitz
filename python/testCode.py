
import xxhash
import zlib
import struct
import os
import sys

def changeStrToAssic(str):
    strLen = len(str);
    asciiInts   = [];
    asciiDiffs  = [];
    for idx in xrange(0,strLen):
        asciiInts.append(ord(str[idx]));    # print("idx::{}  asccii::{}".format(idx, ord(str[idx])))
        if idx > 0:
            asciiDiffs.append(asciiInts[idx] - asciiInts[idx-1])
    asciiDiffs.append(-asciiInts[strLen-1])
    # 
    print("")
    print("//////////////////////////////////////")
    print("//" + str);
    print("int x = 0;");
    print("char *y = (char *)malloc({});".format(strLen+1))
    print("char *z = y;");
    print("*(z++) = {};".format('%#X'%asciiInts[0]));
    # 
    for val in asciiDiffs:
        if val >= 0:
            print("*(z++)=y[x++]+{};".format('%#X'%val));
        else:
            print("*(z++)=y[x++]{};".format('%#X'%val));
    print("return y;")
    print("//////////////////////////////////////")

def changeStrToAssicExt(str, varNameX, varNameY, varNameZ):
    strLen = len(str);
    asciiInts   = [];
    asciiDiffs  = [];
    for idx in xrange(0,strLen):
        asciiInts.append(ord(str[idx]));    # print("idx::{}  asccii::{}".format(idx, ord(str[idx])))
        if idx > 0:
            asciiDiffs.append(asciiInts[idx] - asciiInts[idx-1])
    asciiDiffs.append(-asciiInts[strLen-1])
    # 
    print("")
    print("//" + str);
    print("int {} = 0;".format(varNameX));
    print("char *{} = (char *)malloc({});".format(varNameY, strLen+1))
    print("char *{} = {};".format(varNameZ, varNameY));
    print("*({}++) = {};".format(varNameZ, '%#X'%asciiInts[0]));
    # 
    for val in asciiDiffs:
        if val >= 0:
            print("*({}++)={}[{}++]+{};".format(varNameZ, varNameY, varNameX, '%#X'%val));
        else:
            print("*({}++)={}[{}++]{};".format(varNameZ, varNameY, varNameX, '%#X'%val));
    # 
    print("return {};".format(varNameY))
    print("")


if __name__ == "__main__":
    print("--------------------")
    # changeStrToAssic("eckk@BoomEgg2014")
    # 
    # changeStrToAssicExt("eckk@BoomEgg2014", "x", "y", "z")
    print("------------------------------------")
    # changeStrToAssicExt("XINGBOKEJI-SLOTSGAME", "x", "y", "z")
    # changeStrToAssicExt("XINGBO-GAME-DRAGONHOU-211", "x", "y", "z")
    changeStrToAssicExt("UUIDKEY-XBGODSLOSTCASINO-2019-02-18", "x", "y", "z")
    # print("------------------------------------")
    # changeStrToAssicExt("XINGBO-GAME-DRAGONHOU-211", "index", "tmp", "arr")
    # for s in str:
    #     asciiInts.append(ord(s));