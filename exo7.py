def crypt(word):

    chars="abcdefghijklmnopqrstuvwxyz"

    res = ""

    for char in word:
        res=res+str(chars.index(char))+"-"
    
    res = res[:-1]

    print(res)

    return res

crypt("abc")