from asyncio.windows_events import NULL
import re

print("BOTTOM UP (SHIFT REDUCE) PARSER\n")
print("E -> E + T\n")
print("T' -> T + F\n")
print("F -> n\n")

inp = input("Enter Your Input to Test Against the CFG: ")
splt = inp.split()
print(splt)

i=0
strng=[None]*len(inp)

def parseReduce():
    global i
    if strng[i]=='n':
        strng[i]='E'
        print('Reducing E--> n', strng[i])
        i=i+1
    elif (strng[i]=='E') and (strng[i-2]=='E'):
        strng[i]=NULL
        strng[i-1]=NULL
        print('Reducing E--> E+E')
        i=i-2
    else:
        i=i+1

while(splt[i]!='$'):
    strng[i]=splt[i]
    print('SHIFT-->',strng[i])
    parseReduce()

print(strng)
