
import ProjMain as PM #Lexical and Type Checking
import LRtest as LR
import symtest as ST
import ICG as ICG
import warnings
from time import sleep
warnings.filterwarnings("ignore")
tokSplit = []
ST.dt = PM.dt
file = open("lex.txt",'r')

print(" ================= SYMBOL TABLE ================= ")
ST.main()
sleep(3)
print(" ================= LR PARSER ================= ")
LR.main()
sleep(3)
print(" ================= INTERMERDIATE CODE GENERATION ================= ")
ICG.main()
print(" ================= COMPILER FINISHED ================= ")
sleep(3)
print(" ================= THANKYOU FOR USING! ================= ")
#ST2.tokensIntoTable(PM.tokens)
#ST.main()