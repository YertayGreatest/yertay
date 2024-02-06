def avgbycat(movies, category):
    bycate = [movie for movie in movies if movie["category"]==category]
    scores = [movie["imdb"] for movie in bycate]
    return sum(scores) / len(scores)


