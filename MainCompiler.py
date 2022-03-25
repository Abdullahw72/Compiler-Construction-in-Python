import ProjMain as LA
import LRParser as Parser
import SymbolTable as ST


space = "\t\t\t"
sucess = False
#Get tokens from the source file
print("Lexical Analyzer:")
print(space+"Tokenizing File....")
ini_code = LA.readinput()
clean_code = LA.removecomments(ini_code)
LA.writecleancode(clean_code)
tokens = LA.lex_Analyzer(clean_code)
LA.typeCheck(tokens)

Tokens = tokens
print(space+"Tokenization Successful, Tokens stored in lex.txt")


#all words with spaces in between
inpp = []
for inp in Tokens:
    if inp.type not in ["identifier", "DoubleConstant","BooleanConstant","StringConstant","IntegerConstant","FloatConstant","CharacterConstant"]:
        inpp.append(inp.word)
    elif inp.word == "main":
        inpp.append(inp.word)
    else:
        inpp.append(inp.type)
    inpp.append(" ")        

#Check the input string using the cfg "cfgList"
print("\nSyntax Analyzer:")
cfgList ="""
_S_ -> _IMPORTS_ _NAMESPACE_ _FUNC DEFS_ _S_ | _NAMESPACE_ _S_ | _MAIN_ | _FUNC DEFS_ _S_ | _IMPORTS_ _S_
_IMPORTS_ -> #include identifier
_NAMESPACE_ -> using namespace identifier ;
_FUNC DEFS_ -> _IDENTIF_ ( ) _BLOCK STATEMENT_ | _FUNC DEFS_ _FUNC DEFS_ | $$fde | $$fds
_MAIN_ -> _DTYPE_ main ( ) _BLOCK STATEMENT_
_IDENTIF_ -> _DTYPE_ identifier
_BLOCK STATEMENT_ -> { _BLOCK STATEMENT_ } | { _STATEMENT_ } | { _EXPRESSION_ } | { _EXPRESSION_ _BLOCK STATEMENT_ } | { _EXPRESSION_ _STATEMENT_ } | { _STATEMENT_ _BLOCK STATEMENT_ } | { } | _BLOCK STATEMENT_ _EXPRESSION_
_STATEMENT_ -> _IF STATEMENT_ | _SWITCH STATEMENT_ | _LOOP_ | _EXPRESSION_  | _STATEMENT_ _STATEMENT_ | break ; | continue ; | _BLOCK STATEMENT_ _STATEMENT_ | _ASSIGNMENT_
_EXPRESSION_ -> _VARIABLEINITASSIGN_ | _IDENTVALCHANGE_ | _CONDITION_ ; | _IDENTIF_ ; | _STATEMENT_ _EXPRESSION_ | _EXPRESSION_ _EXPRESSION_ | _CONDITION_ | _EXPRESSION_ ;
_IF STATEMENT_ -> if ( _EXPRESSION_ ) _BLOCK STATEMENT_ | if ( _STATEMENT_ ) _BLOCK STATEMENT_  | _IF STATEMENT_ else _BLOCK STATEMENT_ | _IF STATEMENT_ else if ( _EXPRESSION_ ) _BLOCK STATEMENT_ | _IF STATEMENT_ else if ( _STATEMENT_ ) _BLOCK STATEMENT_ | _STATEMENT_ else _BLOCK STATEMENT_ | _STATEMENT_ else _STATEMENT_  
_SWITCH STATEMENT_ -> switch ( identifier ) { _CASE EXPRESSION_ }
_CASE EXPRESSION_ -> default : _STATEMENT_ | case _RVALUE_ : _STATEMENT_ _CASE EXPRESSION_ | case _RVALUE_ : _STATEMENT_ | _CASE EXPRESSION_ _CASE EXPRESSION_ |  _CASE EXPRESSION_ _STATEMENT_
_LOOP_ -> while ( _EXPRESSION_ ) _BLOCK STATEMENT_ | while ( _STATEMENT_ ) _BLOCK STATEMENT_ | do _BLOCK STATEMENT_ while ( _EXPRESSION_ ) | do _BLOCK STATEMENT_ while ( _STATEMENT_ ) | for ( _FORCOND_ ) _BLOCK STATEMENT_
_FORCOND_ -> _STATEMENT_ identifier _CHANGEOPERATOR_ _RVALUE_ ; | STATEMENT_ identifier _CHANGEOPERATOR_ _RVALUE_ ; | _VARIABLEINITASSIGN_ ; _EXPRESSION_ ; _IDENTVALCHANGE_ | _STATEMENT_ ; identifier -= _RVALUE_ ; | _STATEMENT_ ; identifier += _RVALUE_ ;
_CONDITION_ -> identifier _CONDOPERATOR_ _RVALUE_  | identifier _CONDOPERATOR_ identifier | _CONDITION_ _ANDOROPERATOR_ _CONDITION_  | _CONDITION_ _ANDOROPERATOR_ identifier  
_IDENTVALCHANGE_ -> _IDENTIF_ _CHANGEOPERATOR_ _RVALUE_ ; | _IDENTIF_ _CHANGEOPERATOR_ identifier ;
_DTYPE_ -> double | string | int | float | bool | char | void
_RVALUE_ -> DoubleConstant | StringConstant | IntegerConstant | FloatConstant | BooleanConstant | CharacterConstant | _CALCULATION_ | _CALCULATION_ ;
_CHANGEOPERATOR_ -> _CALCULATION OPERATOR_=
_CONDOPERATOR_ -> < | > | <= | <= | != | ==
_ANDOROPERATOR_ || | &&
_VARIABLEINITASSIGN_ -> _IDENTIF_ = _RVALUE_ ; | _IDENTIF_ = identifier ;
_CALCULATION_ -> identifier _CALCULATION OPERATOR_ _RVALUE_ | _RVALUE_ _CALCULATION OPERATOR_ _RVALUE_ | identifier _CALCULATION OPERATOR_ identifier | _RVALUE_ _CALCULATION OPERATOR_ identifier | _CALCULATION_ _CALCULATION OPERATOR_ _CALCULATION_ | _RVALUE_ _CALCULATION OPERATOR_ _CALCULATION_ | _CALCULATION_ _CALCULATION OPERATOR_ _RVALUE_ | identifier _CALCULATION OPERATOR_ _CALCULATION_ | _CALCULATION_ _CALCULATION OPERATOR_ identifier
_CALCULATION OPERATOR_ -> + | - | * | /
_ASSIGNMENT_ -> identifier = _RVALUE_ ;
"""

print(space+"Checking tokens for Syntax Errors....")

if(Parser.checkStringForLanguage(cfgList,Tokens.copy(),"_S_")):

    print(space+"Accepted By Parser, Results stored in ParserLog.txt")
    print(space+"Inserting into symbol table...")
    
    symbols = ST.tokensIntoTable(Tokens)

    print("\nSymbol Table:")
    if(symbols == False):
        print(space+"Symbol Table insertion Failed")
    else:
        print(space+"Symbol Table insertion Successful")
        ST.PrintSymbols(symbols)
        print("")

else:
    print(space+"Rejected By Parser, Results stored in ParserLog.txt")

if symbols:
    print("\nThe given C++ file is syntactically and semantically correct")
else:
    print("\nThe given C++ file is either syntactically or semantically incorrect")
