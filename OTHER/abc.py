from lib2to3.pgen2 import token
from beautifultable import BeautifulTable
import re
import ProjMain as PM
dt= PM.dt
tab=[]
tokenSplit=[]
tokenSplit=PM.main()

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
    global dt
    while(i<len(tokenSplit)):
        if tokenSplit[i]=='{':
            flag=True
            scopee+=1
            i+=1
        elif tokenSplit[i]=='}':
            scopee-=1
            i+=1
            flag=True         
        else:
            while(i<len(tokenSplit) and tokenSplit[i]!='{' and tokenSplit[i]!='}'):
                i+=1
                namee=""
                tipe=""
                if tokenSplit[i] in PM.keyword or tokenSplit[i] in PM.punc or tokenSplit[i] in PM.increment or tokenSplit[i] in PM.decrement or tokenSplit[i] in PM.logicOp or tokenSplit[i] in PM.mathOp or tokenSplit[i] in PM.relationOp or tokenSplit[i] in PM.litr or tokenSplit[i] in PM.integ or tokenSplit[i] in PM.preProcess:
                    i+=1
                    continue
                elif tokenSplit[i] in dt:
                    tipe=tokenSplit[i]
                    i+=1
                    if re.match('^[a-zA-Z]+$',tokenSplit[i]):
                        namee=tokenSplit[i]
                        i+=1
                        if lookup(namee,scopee):
                            insert(namee,tipe,scopee)
                            table.append_row([namee,tipe,scopee])
                        elif tokenSplit[i]=='=':
                            None
                            i+=1
                            if tokenSplit[i-3]=='int' and re.match('^[0-9]+$',tokenSplit[i]):
                                i+=1
                                insert(namee,tipe,scopee)
                                table.append_row([namee,tipe,scopee])
                            elif tokenSplit[i-3]=='string' and re.match('^"[\w]+"$',tokenSplit[i]):
                                i+=1
                                insert(namee,tipe,scopee)
                                table.append_row([namee,tipe,scopee])
                            elif tokenSplit[i-3]=='char' and re.match("^'[A-Za-z0-9]'$",tokenSplit[i]):
                                i+=1
                                insert(namee,tipe,scopee)
                                table.append_row([namee,tipe,scopee])
                            elif tokenSplit[i-3]=='float' and re.match('[+-]?\d+\.\d+', tokenSplit[i]):
                                i+=1
                                insert(namee,tipe,scopee)
                                table.append_row([namee,tipe,scopee])
                            else:
                                print("ERROR:",namee,"'s Datatype Mismatch at scope",scopee)
                                error=True
                                if len(tab)!=0:
                                    tab.pop()
                                    table.pop_row()
                                    i+=1
                        else:
                            print("ERROR:",namee," is already defined at scope",scopee)
                            error=True
                    else:
                        i+=1                   
                else:
                    i+=1
            

        
    if(not error):
        print("No Error Found!!!")
    print("\nSymbol Table")
    print(table)

