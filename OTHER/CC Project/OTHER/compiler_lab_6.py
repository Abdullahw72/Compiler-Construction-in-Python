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
    # file = open("lex.txt", "w")
    # keyword = ['for','if','elif','Else','while','def','range','in', 'main', 'func', 'out', 'print']
    # relationOp = ['<','>','<=','>=','<>',':']
    # identifier = r"[a-zA-Z]"
    # integ = r"[0-9]"
    # increment = r"[++]"
    # decrement = r"[--]"
    # punc = ['(',')','[',']','{', '}' , '.' , ';' , ':' ,'"']
    # mathOp = ['+', '-' , '/' , '*' , '%']
    # logicOp = ["and" , "or" , "not"]
    # litr = r"\"[a-zA-Z]+\""

    for i in len(store):
        if(store[i]=='"'):
            i=i+1
            while(store[i]!='"'):
                i=i+1
                continue
        else:
            print(store[i])
        #storeVal = store.split()


#     for word in storeVal:
#         if word in logicOp:
#             file.write("(logical operator: "+ word +" )"+"\n")
        
#         elif word in punc:
#             file.write("(Punctuation: "+ word +" )"+ "\n")

#         elif re.findall('\"[a-zA-Z]+\"',word):
#             file.write("(Literals: "+ word +" )"+"\n")

#         elif word in keyword:
#             file.write("(Keyword: "+ word +" )"+"\n")

#         elif word in relationOp:
#             file.write("(Relational operators: "+ word +" )"+"\n")

#         elif re.match(integ,word):
#             file.write("(Integer: "+ word +" )"+"\n")

#         elif word in mathOp:
#             file.write("(Mathematical operator: "+ word +" )"+ "\n")

#         elif re.match(increment,word):
#             file.write("(Increment: "+ word +" )"+"\n")

#         elif re.match(decrement,word):
#             file.write("(Decrement: "+ word +" )"+"\n")

#         elif re.match(identifier, word): 
#             file.write("(Identifier: "+ word +" )"+"\n")

#     file = open("lex.txt",'r')
#     print(file.read())

ini_code = readinput()
clean_code = removecomments(ini_code)
writecleancode(clean_code)
lex_Analyzer(clean_code)