def decrypt(indexes:str):

    indexes = indexes.split("-")

    indexes

    chars="abcdefghijklmnopqrstuvwxyz"

    res = ""

    for i in indexes:
        res=res+chars[int(i)]

    print(res)

    return res

decrypt("0-1-2")