
import ProjMain as PM #Lexical and Type Checking
#import SymbolTable as ST #Symbol Table
import LRtest as LR
import symtest as ST
import warnings
from time import sleep
warnings.filterwarnings("ignore")
tokSplit = []
ST.dt = PM.dt
file = open("lex.txt",'r')
# for line in file:
#     fileVal = file.read()
#     tokSplit.append(fileVal.split("\n"))
print(" ================= SYMBOL TABLE ================= ")
ST.main()
sleep(3)
print(" ================= LR PARSER ================= ")
LR.main()
sleep(3)
print(" ================= COMPILER FINISHED ================= ")
sleep(3)
print(" ================= THANKYOU FOR USING! ================= ")

#ST2.tokensIntoTable(PM.tokens)
#ST.main()