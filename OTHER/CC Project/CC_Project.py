import re
def readinputstream():
	file1 = open("code.txt","r")
	fileInfo = file1.read()
	file1.close()
	return fileInfo

def removecomments(code):
	single = re.sub(r"(#|(//))(.+?)[\n]","",code)
	multireg = re.compile(r"((\"\"\")(.+?)(\"\"\"))|((/\*)(.+?)(\*/))", re.DOTALL)
	multi = re.sub(multireg,"", single)
	return multi

def tokenize(cleancode):
	rules = [
		("literals", r"0|([1-9][0-9]*)|(.[0-9]+)|(\".+?\")|(\'.+?\')"),		
		("whitespace", r"\s"),
		("keywords",r"void |main|if|else|return|range|elif|print|in"),
		("datatypes",r"int|float|string"),		
		("identifiers",r"[A-Za-z_][\w]*"),
		("punctuaters",r"[\[\]\(\)\:\;\,\{\}]"),
		("mathematical_operators", r"[\+\-\*\/\%]"),
		("relational_operators", r"(\=\=)|(\<\=)|(\>\=)|[<>]"),
		("logical_operators", r"(\&\&)|(\|\|)|(\>\=)|[<>]|and|or|not"),		
		("unknowns", r"."),
	]
	tokens = "|".join(r"(?P<%s>%s)" % x for x in rules)
	tokenized = []
	for m in re.finditer(tokens, cleancode):
		tokentype = m.lastgroup
		tokenstring = m.group(tokentype)
		# print((tokentype, tokenstring))
		if tokentype == "whitespace":
			continue
		if tokentype == "unknowns":
			print(f"Unknown symbol detected-->\'{tokenstring}\'")
			continue		
		tokenized.append(f"<{tokentype}, {tokenstring}>")
		if tokentype == "identifiers":
			n = re.search("|".join(r"(?P<%s>%s)" % x for x in [rules[2],rules[3]]),(tokenstring).lower())
			if n:
				possibletype = n.lastgroup
				possibletokenstring = n.group(possibletype)	
				if (not possibletokenstring == tokenstring) and possibletype:
					print (f"{tokenstring} should be changed to {possibletokenstring}")
	return tokenized

code = readinputstream()
# print(code)
cleancode = removecomments(code)
# print(cleancode)

file3 = open("cleancode.txt", "w")
file3.write(cleancode)
file3.close()

tokens = tokenize(cleancode)

file2 = open("output.txt", "w")
for t in tokens:
	file2.write(f"{t}\n")
file2.close()
