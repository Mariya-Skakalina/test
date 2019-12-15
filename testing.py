import re
import math

latin = {"е":"e","у":"y","о":"o","р":"p","а":"a","х":"x","с":"c"}
rep = dict((re.escape(k), v) for k, v in latin.items()) 
pattern = re.compile("|".join(rep.keys()))
text = "удлинение газели с еврофургоном до 4.2 м, 5.2 м, 6.2 м"
final = pattern.subn(lambda m: rep[re.escape(m.group(0))],text)
print(final)
factorial = math.factorial(final[1])
print(factorial)

# with open('./tut.txt', 'w+') as inLine:
#     inLine.writelines(str(factorial))


#  с еврофургоном до 4.2 м, 5.2 м, 6.2 м

test = "удлинение газели с еврофургоном до 4.2 м, 5.2 м, 6.2 м"
reg = r"([уеарохс])"
f = re.findall(reg, test)
fact = math.factorial(len(f))
print(fact)