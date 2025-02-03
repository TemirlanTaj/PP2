from movies import movies 

def avgMov(l):
    total = 0
    for i in range(len(l)):
        total += l[i]["imdb"]
    return total/len(l)

print(avgMov(movies))