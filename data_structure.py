import json
import webbrowser

def sortGenre(movie, runtime, year):
    if "Drama" in movie["Genre"]:
        tree[runtime][year][1].append(movie)
    if "Adult" in movie["Genre"]:
        tree[runtime][year][2].append(movie)
    if "Documentary" in movie["Genre"]:
        tree[runtime][year][3].append(movie)
    if "Adventure" in movie["Genre"]:
        tree[runtime][year][4].append(movie)
    if "Comedy" in movie["Genre"]:
        tree[runtime][year][5].append(movie)
    if "Crime" in movie["Genre"]:
        tree[runtime][year][6].append(movie)
    if "Mystery" in movie["Genre"]:
        tree[runtime][year][7].append(movie)
    if "Fantasy" in movie["Genre"]:
        tree[runtime][year][8].append(movie)
    if "Thriller" in movie["Genre"]:
        tree[runtime][year][9].append(movie)
    if "Drama" not in movie["Genre"] and "Adult" not in movie["Genre"] and "Documentary" not in movie["Genre"] and \
       "Adventure" not in movie["Genre"] and "Comedy" not in movie["Genre"] and "Crime" not in movie["Genre"] and \
       "Mystery" not in movie["Genre"] and "Fantasy" not in movie["Genre"] and "Thriller" not in movie["Genre"]:
       tree[runtime][year][10].append(movie)

tree = ['Please choose one kind of time period the movie may be released:', 
         ['Please choose one kind of runtime of the movie:', 
           ['Please choosing one kind of movie genres you want to search:', 
            [],[],[],[],[],[],[],[],[],[]], 
           ['Please choosing one kind of movie genres you want to search:', 
            [],[],[],[],[],[],[],[],[],[]],
           ['Please choosing one kind of movie genres you want to search:', 
            [],[],[],[],[],[],[],[],[],[]]
         ], 
         ['Please choose one kind of runtime of the movie:', 
           ['Please choosing one kind of movie genres you want to search:', 
            [],[],[],[],[],[],[],[],[],[]], 
           ['Please choosing one kind of movie genres you want to search:', 
            [],[],[],[],[],[],[],[],[],[]],
           ['Please choosing one kind of movie genres you want to search:', 
            [],[],[],[],[],[],[],[],[],[]]
         ]
       ]

f = open("cache.json","r")
movieDict = json.loads(f.read())
f.close()



for movie in movieDict:
    year = ''.join(filter(lambda i: i.isdigit(), movie["Year"]))
    runtime = ''.join(filter(lambda i: i.isdigit(), movie["Runtime"]))
    if int(year) <= 2000:
        if int(runtime) <= 40:
            sortGenre(movie, 1, 1)
        elif 40 < int(runtime) <= 60:
            sortGenre(movie, 1, 2)
        elif int(runtime) > 60:
            sortGenre(movie, 1, 3)
    else:
        if int(runtime) <= 40:
            sortGenre(movie, 2, 1)
        elif 40 < int(runtime) <= 60:
            sortGenre(movie, 2, 2)
        elif int(runtime) > 60:
            sortGenre(movie, 2, 3)

with open("tree.json", "w") as outfile:
    json.dump(tree, outfile)
