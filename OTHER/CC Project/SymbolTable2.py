from texttable import Texttable

SymbolTable = []
scp = "0"
previous = []
class symbol():
    name :str
    type :str
    scope :str

    def __init__(self,name,type,scope):
        self.name = name
        self.type = type
        self.scope = scope
    def __repr__(self):
        return "<" + self.type + ", " + self.name + ", " + self.scope + ">"

def insert(smb:symbol):
    try:
        global SymbolTable
        for sym in SymbolTable:
            if(sym.name == smb.name) and (sym.scope == smb.scope):
                print("\t\t\tUnable to insert variable name '" +sym.name+"' into scope '" + sym.scope +"', Value already exists for current scope")
                return False
        SymbolTable.append(smb)
        return True
    except Exception:
            return False

def Lookup(name, scope):
    try:
        global SymbolTable
        for sym in SymbolTable:
            if(sym.name == name) and (sym.scope == scope):
                return True
        return False
    except Exception:
        return False

def scopeinc():
    global scp
    previous.append(scp)
    scp = str(int(getScopeNum()) + 1)
    for sym in SymbolTable:
        tempVal = ''
        for i in sym.scope:
            if i.isdigit():
                tempVal+=i
    
        if tempVal == scp:
            tempVal = ''
            m = []
            for x in SymbolTable:
                m.append(x.scope)
            for i in range(len(scp)):
                m = [x for x in m if x[i] == scp[i]]
            m.sort()
            tempVal = m[-1]
            tempValchar = ""
            for i in tempVal:
                if i.isalpha():
                    tempValchar+=i
    
            if len(tempValchar) == 0:
                tempValchar+="a"
                scp+=tempValchar
    
            elif tempValchar[-1] == "z":
                tempValchar+="a"
                scp+=tempValchar
    
            else:
                ch = bytes(tempValchar, 'utf-8')
                s = bytes([ch[-1] + 1])
                tempValchar=s.decode("utf-8")
                scp+=tempValchar
            break

def scopedec():
    global scp
    scp = previous.pop()

def getScopeNum():
    global scp
    ret = ''
    for i in scp:
        if i.isdigit():
            ret+=i
    return ret

def getScopeChar():
    global scp
    ret = ''
    for i in scp:
        if i.isalpha():
            ret+=i
    return ret

def tokensIntoTable(tokenList):
    global scp
    ti = len(tokenList)
       
    for i in range(ti):
            if i == 56:
                i = i
            curr = tokenList[i]
            if curr.type == "Identifier":
                prev = tokenList[i - 1]
                next = tokenList[i + 1]
                if next.word != "(" and prev.word in ["double","string","int","float","bool","char"]:
                    newsymb = symbol(curr.word,prev.word,scp)
                    if(not insert(newsymb)):
                        return False
            elif curr.word in ["{","("]:
                scopeinc()
            elif curr.word in ["}",")"]:
                scopedec()
    return SymbolTable

def PrintSymbols(SymTbl:list):
    List = []
    List.append(['Name', 'Type', 'Scope'])
    for sym in SymTbl:
        List.append([sym.name,sym.type,sym.scope])
    t = Texttable()
    t.add_rows(List)
    print(t.draw())