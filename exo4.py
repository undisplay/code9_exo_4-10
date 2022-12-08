import random

def random_code(n):
    chars="abcdefghijklmnopqrstuvwxyz1234567890"
    code=""
    for i in range(0,n):
        random_char=random.choice(chars)
        chars = chars.replace(random_char,"")
        
        code=code+random_char
    
    print(code,len(code))

    return code

random_code(36)
