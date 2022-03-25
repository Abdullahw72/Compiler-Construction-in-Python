from lib2to3.pgen2 import token
from beautifultable import BeautifulTable
import ProjMain as PM
import re
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
    while(i<len(tokenSplit)):
        if tokenSplit[i]=='{':
            flag=True
            scopee+=1
            i+=1
        while(i<len(tokenSplit) and tokenSplit[i]!='{'):
            namee=""
            tipe=""
            if tokenSplit[i] in PM.keyword or tokenSplit[i] in PM.punc or tokenSplit[i] in PM.increment or tokenSplit[i] in PM.decrement or tokenSplit[i] in PM.logicOp or tokenSplit[i] in PM.mathOp or tokenSplit[i] in PM.relationOp or tokenSplit[i] in PM.litr or tokenSplit[i] in PM.integ or tokenSplit[i] in PM.preProcess:
                i+=1
                continue
            elif tokenSplit[i] in dt:
                tipe=tokenSplit[i]
                if re.match('^[a-zA-Z]+$',tokenSplit[i]):
                    namee=tokenSplit[i]
                    if lookup(namee,scopee):
                        insert(namee,tipe,scopee)
                        table.append_row([namee,tipe,scopee])
                    else:
                        print("ERROR:",namee," is already defined at scope",scopee)
                        error=True
                elif (re.match(r"^[a-zA-Z]\w*$",tokenSplit[i]) or tokenSplit[i] in PM.keyword) and tokenSplit[i+1]=="(" and tokenSplit[i+2]==")":
                        print("AAAA")
                        i+=3
                        continue
                        
                if tokenSplit[i]=='}':
                    scopee-=1
                    i+=1
                    flag=False
        else:
            i+=1
    if(not error):
        print("No Error Found!!!")
    print("\nSymbol Table")
    print(table)

