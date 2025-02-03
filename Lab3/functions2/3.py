from movies import movies 

def sameGenre(s):
    for i in range(len(movies)): #найти жанр
        if movies[i]["name"] == s:
            genre = movies[i]["category"]
    for i in range(len(movies)):
        if movies[i]["category"] == genre:
            print(movies[i])

a = input("Enter movie name: ")

sameGenre(a)