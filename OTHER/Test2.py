import re

keyword = ['for','if','elif','else','while','def','range','in', 'main', 'func', 'out', 'print', 'while', 'switch', 'case', 
'break', 'continue', 'default', 'void']
relationOp = ['<','>','<=','>=','<>',':', '!=']
identifier = r"[a-zA-Z]"
integ = r"[0-9]"
float = r"[+-]?\d+\.\d+"
increment = r"[++]"
decrement = r"[--]"
punc = ['(',')','[',']','{', '}' , '.' , ';' , ':' ,'"']
mathOp = ['+', '-' , '/' , '*' , '%']
logicOp = ["and" , "or" , "not"]
assignmentOP = ["="]
dt=['int','char','string', 'float', 'void', 'bool', 'double']
preProcess = ['include', 'iostream', 'using', 'namespace', 'std']
litr = r"(\".+?\")|(\'.+?\')"
err = False

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
    storeVal = store.split()

    for word in storeVal:
        if word in logicOp:
            file.write("(Logical Operator: "+ word +" )"+"\n")
        
        elif word in punc:
            file.write("(Punctuation: "+ word +" )"+ "\n")

        elif word in preProcess:
            continue
        
        elif re.findall('\"[a-zA-Z]+\"',word):
            file.write("(Literals: "+ word +" )"+"\n")

        elif word in keyword:
            file.write("(Keyword: "+ word +" )"+"\n")

        elif word in dt:
            file.write("(Data Type: "+ word + " )"+"\n")

        elif word in relationOp:
            file.write("(Relational operators: "+ word +" )"+"\n")

        elif re.match(float,word):
            file.write("(Float: "+ word +" )"+"\n")

        elif re.match(integ,word):
            file.write("(Integer: "+ word +" )"+"\n")

        elif word in mathOp:
            file.write("(Mathematical operator: "+ word +" )"+ "\n")

        elif re.match(increment,word):
            file.write("(Increment: "+ word +" )"+"\n")

        elif re.match(decrement,word):
            file.write("(Decrement: "+ word +" )"+"\n")

        elif re.match(identifier, word): 
            file.write("(Identifier: "+ word +" )"+"\n")
        elif word in assignmentOP:
            file.write("(Assignment Operator: "+ word + " )"+"\n")

    file = open("lex.txt",'r')
    print(file.read())
    return storeVal


def checkk(typee,value):
    if typee=='int' and re.match('[0-9]+$',value) or value=="main":
        return True
    elif typee=='string' and re.match('^"[\w]+"$',value) or value=="main":
        return True
    elif typee=='char' and re.match("^'[A-Za-z0-9]'$",value) or value=="main":
        return True
    elif typee=='float' and re.match('[+-]?\d+\.\d+',value) or value=="main":
        return True
    elif typee=='bool' and (value=='True' or value =='False'):
        return True
    else:
        return False

def typeCheck(tok):
    global err
    error=False
    flag=True
    i=0
    namee=""
    tipe=""
    
    while i<len(tok) and flag==True:
        if tok[i] in keyword or tok[i] in punc or tok[i] in increment or tok[i] in decrement or tok[i] in logicOp or tok[i] in mathOp or tok[i] in relationOp or tok[i] in litr or tok[i] in integ:
            i+=1 
        elif tok[i] in dt:
            tipe=tok[i]
            i+=1
            if (tok[i] == "main" and tok[i+1]=="(" and tok[i+2]==")"):
                i+=3
                continue
            elif (re.match("^[a-zA-Z_]\w*$",tok[i])):
                namee=tok[i]
                i+=1                
                if tok[i]=='=':
                    i+=1
                    if checkk(tipe,tok[i]):
                        tipe=""
                        i+=1
                    else:
                        print("ERROR:",namee,"'s Datatype Mismatch")
                        error=True
                        i+=1     
                else:
                    print("= missing after ", tok[i])
                    i+=1
            else: 
                print("Identifier", tok[i], "is not correct. ")
        else:
            error = True
            err = True
            i+=1  

            
    if(not error):
        print("No Error Found!!!")
    elif(err==True):
        print("Datatype expected, but got something else")





ini_code = readinput()
clean_code = removecomments(ini_code)
writecleancode(clean_code)
tokens = lex_Analyzer(clean_code)
typeCheck(tokens)
