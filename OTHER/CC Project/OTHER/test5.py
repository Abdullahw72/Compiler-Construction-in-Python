from beautifultable import BeautifulTable
import re
codeFile = open("ini_code.txt")
inp = codeFile.read()
dt=['int','char','string','double','float']
tab=[]
tokenSplit=[]
tokenSplit=inp.split()
print(tokenSplit,"\n")
def lookup(name,scope):
    i=0
    if len(tab)!=0:
        while(i<len(tab)):
            if name in tab[i] and scope in tab[i]:
                return False
            else:
                i+=1
        return True
    else:
        return True
    
def insert(name,typee,scope):
        tab.append([name,typee,scope])
        
def main():
    table=BeautifulTable()
    table.column_headers=["Name","Type","Scope"]
    error=False
    flag=True
    scopee=-1
    i=0
    while(i<len(tokenSplit)):
        if tokenSplit[i]=='{':
            flag=True
            scopee+=1
            i+=1
        while(i<len(tokenSplit) and flag==True):
            namee=""
            tipe=""
            if tokenSplit[i] in dt:
                tipe=tokenSplit[i]
                i+=1
                if re.match('^[a-zA-Z]+$',tokenSplit[i]):
                    namee=tokenSplit[i]
                    if lookup(namee,scopee):
                        insert(namee,tipe,scopee)
                        table.append_row([namee,tipe,scopee])
                    else:
                        print("ERROR:",namee," is already defined at scope",scopee)
                        error=True
                i+=1
                if tokenSplit[i]=='=':
                    None
                    i+=1
                    if tokenSplit[i-3]=='int' and re.match('^[0-9]+$',tokenSplit[i]):
                        i+=1
                    elif tokenSplit[i-3]=='string' and re.match('^"[\w]+"$',tokenSplit[i]):
                        i+=1
                    elif tokenSplit[i-3]=='char' and re.match("^'[A-Za-z0-9]'$",tokenSplit[i]):
                        i+=1
                    elif tokenSplit[i-3]=='float' and re.match(r"[+-]?\d+\.\d+",tokenSplit[i]):
                        i+=1
                    else:
                        print("ERROR:",namee,"'s Datatype Mismatch at scope",scopee)
                        error=True
                        if len(tab)!=0:
                            tab.pop()
                            table.pop_row()
                            i+=1
                if tokenSplit[i]==';':
                    i+=1
                else:
                    print("ERROR:",namee,"'s Terminator missing at scope",scopee)
                    error=True
                    if len(tab)!=0:
                        tab.pop()
                        table.pop_row()
                        
                if tokenSplit[i]=='}':
                    i+=1
                    flag=False
            elif re.match('^[a-zA-Z]+$',tokenSplit[i]):
                print("ERROR:",tokenSplit[i]," is not Declared as scope",scopee)
                error=True
                i+=1
            else:
                i+=1
        else:
            i+=1
    if(not error):
        print("No Error Found!!!")
    print("\nSymbol Table")
    print(table)

main()
