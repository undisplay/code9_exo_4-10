
def initial_gen(name:str):
    initial = ""

    name = name.replace(" ","-")

    name = name.split("-")

    for w in name:
        initial = initial + w[0].capitalize()

    print(initial)

    return initial

initial_gen("meritus-jean freedy")