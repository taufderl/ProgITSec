import re
 
string = "Dies ist eine Textzeile"
 
match = re.search(r"(.*)(e.*e)(.*)", string)
print(match.groups())

match = re.search(r"(.*?)(e.*?e)(.*)", string)
print(match.groups())
 
match = re.search(r"(.*?)(e.*e)(.*?)", string)
print(match.groups())