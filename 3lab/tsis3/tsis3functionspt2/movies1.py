
def imdabove55(movie):
    if movie["imdb"] >5.5:
        return True
    return False
print(imdabove55({ "name": "Usual Suspects", "imdb": 7.0,"category": "Thriller" } ))