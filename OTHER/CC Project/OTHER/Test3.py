from distutils.command.clean import clean
import re

def removecomments(code):
	single = re.sub(r"(#|(//))(.+?)[\n]","",code)
	multireg = re.compile(r"((\"\"\")(.+?)(\"\"\"))|((/\*)(.+?)(\*/))", re.DOTALL)
	multi = re.sub(multireg,"", single)
	return multi

def writecleancode(cleancode):
    file3 = open("cleancode.txt", "w")
    file3.write(cleancode)
    file3.close()

def readinput():
	file1 = open("ini_code.txt","r")
	fileVal = file1.read()
	file1.close()
	return fileVal


def lex_Analyzer(store):

    file = open("lex.txt", "w")

    keyword = r"main|if|el|elif|back|rng|elif|print|in|func|define|out|halt|chr|run_until|def_class|impt|null|do_until|print"
    relationOp = r"(\=\=)|(\<\=)|(\>\=)|[<>]"
    identifier =r"[A-Za-z_][\w]*"
    integ = r"[0-9]"
    increment = r"[++]"
    decrement = r"[--]"
    punc = r"[\[\]\(\)\:\,\{\}]"
    terminate = r"[\;]"
    mathOp = r"[\+\-\*\/\%]"
    logicOp =  r"(\&\&)|(\|\|)|(\>\=)|[<>]|and|or|not"
    litr = r"(\".+?\")|(\'.+?\')"
    whitesp =  r"\s"
    dType = r"int|strn|float|check|chr|list|rng|check"
    storeVal = store.split()

    for word in storeVal:
        if word in logicOp:
            file.write("(logical-Operator(s): "+ word +" )"+"\n")
        
        elif word in punc:
            file.write("(Punctuation: "+ word +" )"+ "\n")
        
        elif word in terminate:
            file.write("(Terminator: "+ word +" )"+ "\n")

        elif word in keyword:
            file.write("(Keyword: "+ word +" )"+"\n")
        
        elif word in dType:
            file.write("(Data-type: "+ word +" )"+"\n")

        elif word in relationOp:
            file.write("(Relational-Operator(s): "+ word +" )"+"\n")

        elif re.match(integ,word):
            file.write("(Integer: "+ word +" )"+"\n")

        elif word in mathOp:
            file.write("(Mathematical-Operator(s): "+ word +" )"+ "\n")

        elif re.match(increment,word):
            file.write("(Increment: "+ word +" )"+"\n")

        elif re.match(decrement,word):
            file.write("(Decrement: "+ word +" )"+"\n")

        elif re.match(identifier, word): 
            file.write("(Identifier(s): "+ word +" )"+"\n")

        elif re.match(litr,word):
            file.write("(Literal(s): "+ word +" )"+"\n")
        
    file = open("lex.txt",'r')
    print(file.read())
    return storeVal


ini_code = readinput()
clean_code = removecomments(ini_code)
writecleancode(clean_code)
tokens = lex_Analyzer(clean_code)