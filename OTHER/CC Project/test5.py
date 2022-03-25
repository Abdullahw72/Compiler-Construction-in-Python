import re
import shlex

class token:
    word = ""
    type = "Invalid"
    lineNo = 0

    def __init__(self, inp:str,lineno:int,type:str="calcType"):
        self.word = inp
        if(type == "calcType"):
            self.idenType()
        else:
            self.type = type
        self.lineNo = lineno

    def idenType(self):
        Keywords = ["then","true","end","default","for","send","else","int","def","do until","until","double","main","long","dec","let","new","rule","build","bool","state","stop","char"]
        dataType = ["int","alpha","string","dec","word","long","double"]
        punctt = ['+',':','{','}','(',')', '/','"',',']
        arithop = ['+','-','*','/','^','%']
        logicalop = ['||','&&']
        assignop = ['=', '+=','-=','*=','/=','%=','^=']
        relationalop = ['<','>','<=','>=','==', '!=']
        dictii= ["#include","iostream","namespace","std","using","void"]
        if(self.word in dictii):
            self.type = "dictii"
        if(self.word in dataType):
            self.type = "dataType" 
            return
        if(self.word in Keywords):
            self.type = "Keyword"
            return
        elif(self.word == ";"):
            self.type = "Terminator"
            return
        elif(self.word == "++"):
            self.type = "increment"
            return
        elif(self.word == "--"):
            self.type = "Decrement"
            return
        elif(self.word in punctt):
            self.type = "Punctuator"
            return
        elif(self.word in arithop):
            self.type = "Arithematic Operator"
            return
        elif(self.word in logicalop):
            self.type = "Logical Operator"
            return
        elif(self.word in assignop):
            self.type = "Assignment Operator"
            return
        elif(self.word in relationalop):
            self.type = "Relational Operator"
            return
        elif(re.match(r"^^[a-zA-Z_]\w*$", self.word)):
            self.type = "identifier"
            return
        elif(re.match('^"[^"]*"$', self.word)):
            self.type = "StringConstant"
            return
        elif(re.match("^'.'$", self.word)):
            self.type = "CharacterConstant"
            return
        elif(re.match(r"\d+", self.word)):
            self.type = "IntegerConstant"
            return
        elif(re.match(r"\d+[.]\d+", self.word)):
            self.type = "FloatConstant"
            return
        elif(self.word in ["true","false"]):
            self.type = "BooleanConstant"
            return
        return

    def __repr__(self):
        return("< " + self.word + ", " + self.type + ", " + str(self.lineNo) + " >")
    def Printraw(self):
        return("Word: " + self.word + ", Type: " + self.type + ", Line number: " + str(self.lineNo))
    

def getTokens():
    tokenlist = []
    wordlist = []
    file = open('func.txt','r')
    content = file.read()
    content = content + "\n"
    lineno = 1
    content = seperateWords(content)

    wordlist = getWordList(content)
    for word in wordlist:
        if (word != "$$nl"):
            tokenlist.append(token(word,lineno))
        else:
            lineno = lineno + 1
    tokenlist.append(token("$",tokenlist[-1].lineNo + 1,"$"))
    return tokenlist

def getWordList(content):
    return shlex.split(content, posix=False)

def seperateWords(content = ""):
    if content == "":
        f = open('func.txt','r')
        content = f.read()
        content = content + "\n"

    toReplace = ['(//).*(\n)',r'\s*/\*(.|\s)*\*/\s*',r'(\n)']

    theReplacement = ['\n','\n',' $$nl ']

    allrep = len(toReplace)

    for ind in range(allrep):
        content = re.sub(toReplace[ind],theReplacement[ind],content)

    matchlist = re.finditer(r"\[|\]|\{|\}|\(|\)|;", content)
    i = 0
    for match in matchlist:
        s = match.start() + (i * 2)
        e = match.end() + (i * 2)
        leng = len(content)
        if(s != 0):
            behind = content[0:s]
            bracket = content[s]
            ahead = content[e:leng]
            newstr = behind + " " + bracket + " " + ahead
        else:
            newstr = " " + content[0] + " " + content[1:leng]
        content = newstr
        i = i + 1
    return content

def PrintTokens(tokenlist):
    for Stok in tokenlist:
        print("\t" + str(Stok))

def WriteTokens(tokenlist):
    f = open('func_new.txt', 'w')
    f.truncate()
    for Stok in tokenlist:
        f.write(str(Stok) + "\n")
