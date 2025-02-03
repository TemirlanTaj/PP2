from movies import movies 

def goodMovie(s):
    for i in range(len(movies)):
        if movies[i]["name"] == s and movies[i]["imdb"] >= 5.5:
            return True
    return False


a = input("What movie do you want to watch? \n")

print(goodMovie(a))