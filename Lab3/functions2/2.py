from movies import movies

def subList_v1(int):
    res = []
    for i in range(len(movies)):
        if movies[i]["imdb"] >= int:
            res.append(movies[i])
    for i in res:
        print(i)

def subList_v2(int):
    for i in range(len(movies)):
        if movies[i]["imdb"] >= int:
            print(movies[i])


a = float(input("Enter imdb score: "))

subList_v1(a)
subList_v2(a)


