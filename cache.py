import requests
import json

# fetch data from the website
movie_dict = []
movie_count = 0


def get_movie(url,id, ty = "movie" ,key = 'baa5f9b5'):
    parameter={'i':id , 'type':ty , 'apikey' : key}
    res = requests.get(url, parameter).json()
    return res

web_url = "http://www.omdbapi.com"


for i in range(1285016, 1286017):
    movie_id = "tt" + str(i)
    data = get_movie(web_url, movie_id)

    if("Year" in data):
        if("Runtime" in data):
            if("Genre" in data):
                if(data["Year"] != "N/A" and data["Runtime"] != "N/A" and data["Genre"] != "N/A" and data["imdbRating"] != "N/A"):
                    movie_dict.append(data)
                    movie_count += 1



print("number of cached movies: ", movie_count)

with open("cache.json", "w") as outfile:
    json.dump(movie_dict, outfile)


