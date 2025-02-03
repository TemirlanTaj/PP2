from movies import movies 

def avgMov(l, genre):
    total = 0
    c = 0
    for i in range(len(l)):
        if l[i]["category"] == genre:
            total += l[i]["imdb"]
            c += 1
    return total/c

print(avgMov(movies, "Action"))