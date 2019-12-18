import re
import math

latin = {"е":"e","у":"y","о":"o","р":"p","а":"a","х":"x","с":"c"}
rep = dict((re.escape(k), v) for k, v in latin.items()) 
text = "удлинение"
variant = []
def replace_edit(m):
    result = rep[re.escape(m.group(0))]
    return result


def run():

    reg_pravilo = "|".join(rep.keys())
    # reg_pravilo = re.sub(r'^',,reg_pravilo)
    print(reg_pravilo)
    pattern = re.compile(reg_pravilo)
    print(pattern)
    final = pattern.subn(replace_edit,text)
    print(final)
    factorial = math.factorial(final[1])
    print(factorial)


def config_reg():
    reg = True
    text2 = text
    while reg:
        for i in rep.keys():
            reg_pravilo = f"{i}"
            print(reg_pravilo)
            # conf = '[force]{}'.format(reg_pravilo)
            pattern = re.compile(reg_pravilo)
            text2 = pattern.subn(replace_edit,text2,count=0)
            if text2[1] == 0:
                reg = False
                break
            text2 = text2[0]
            variant.append(text2)
    # print(pattern)

config_reg()
print(len(variant))
print(variant)


# # with open('./tut.txt', 'w+') as inLine:
# #     inLine.writelines(str(factorial))


# #  с еврофургоном до 4.2 м, 5.2 м, 6.2 м


# latin = {"е":"e","у":"y","о":"o","р":"p","а":"a","х":"x","с":"c"}
# rep = dict((re.escape(k), v) for k, v in latin.items()) 
# pattern = re.compile("|".join(rep.keys()))
# text = "удлинение таз"
# final = pattern.subn(lambda m: rep[re.escape(m.group(0))],text)


# with open('./tut.txt', 'w+') as inLine:
#     inLine.writelines(str(factorial))
