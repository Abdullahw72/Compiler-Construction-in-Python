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
    keyword = ['for','if','elif','Else','while','def','range','in', 'main', 'func', 'out', 'print']
    relationOp = ['<','>','<=','>=','<>',':']
    identifier = r"[a-zA-Z]"
    integ = r"[0-9]"
    increment = r"[++]"
    decrement = r"[--]"
    punc = ['(',')','[',']','{', '}' , '.' , ';' , ':' ,'"']
    mathOp = ['+', '-' , '/' , '*' , '%']
    logicOp = ["and" , "or" , "not"]
    assignmentOP = ["="]
    litr = r"(\".+?\")|(\'.+?\')"

    storeVal = store.split()

    for word in storeVal:
        if word in logicOp:
            file.write("(logical operator: "+ word +" )"+"\n")
        
        elif word in punc:
            file.write("(Punctuation: "+ word +" )"+ "\n")

        elif re.findall('\"[a-zA-Z]+\"',word):
            file.write("(Literals: "+ word +" )"+"\n")

        elif word in keyword:
            file.write("(Keyword: "+ word +" )"+"\n")

        elif word in relationOp:
            file.write("(Relational operators: "+ word +" )"+"\n")

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
    else:
        return False

def main(tok):
    error=False
    flag=True
    i=0
    dt=['int','char','string', 'float', 'void']
    namee=""
    tipe=""
    while i<len(tok) and flag==True:
        if tok[i] in dt:
            tipe=tok[i]
            i+=1
            if (tok[i] == "main"):
                i+=1
                continue
        else:
            print("ERROR: Datatype expected but got something else:", tok[i])
            error=True
            i+=1   
        if (tok[i] == "main"):
            continue
        elif (re.match('^[a-zA-Z]+$',tok[i])):
             namee=tok[i]
             i+=1
        else:
            print("ERROR: Invalid Variable Name")
            error=True
            i+=1
        if tok[i]=="main":
            continue
        elif (tok[i]=='='):
            i+=1
        else:
            print("ERROR: '=' expected but got something else")
            error=True
            i+=1
        if tok[i]=="main":
           continue
        elif (checkk(tipe,tok[i])):
            checkk(tipe,tok[i])
            tipe=""
            i+=1    
        else:
            print("ERROR:",namee,"'s Datatype Mismatch")
            error=True
            i+=1
        if tok[i]==';' or tok[i]==' ':
            i+=1
        elif (tok[i]==';' or tok[i]==' '):
            i+=1
        else:
            print("ERROR:",namee,"'s Terminator missing")
            error=True
            i+=1
            
    if(not error):
        print("No Error Found!!!")



ini_code = readinput()
clean_code = removecomments(ini_code)
writecleancode(clean_code)
tokens = lex_Analyzer(clean_code)
main(tokens)