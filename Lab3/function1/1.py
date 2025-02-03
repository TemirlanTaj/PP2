def GramsToOnces(gram):
    onces = gram / 28.3495231
    print(onces)

def OuncesToGrams(ounces): #v2
    grams = ounces * 28.3495231
    print(grams)


a = float(input("How much grams do you need? \n"))
GramsToOnces(a)
OuncesToGrams(a)#v2