import TypeChecking as TC
import re

def CheckSamantics(inpp):
    inpList = "".join(inpp)
    Dtypes=["double","string","int","float","bool","char"]
    RValues=["DoubleConstant","StringConstant","IntegerConstant","FloatConstant","BooleanConstant","CharacterConstant"]

    SemanticRegex = re.compile(r"("+"|".join(Dtypes)+r")\s(identifier)\s=\s("+"|".join(RValues)+r")\s;")

    identifierPos = SemanticRegex.findall(inpList)
    print("\nSemantic Analyzer:")
    print("\t\t\tChecking for type errors in code....")
    for iden in identifierPos:
        if not TC.compare(iden[0],iden[2]):
            print("\t\t\tvalue and datatype do not match, " + iden [0]+ ", " + iden[2])
            return False
    print("\t\t\tNo type error detected")
    return True
