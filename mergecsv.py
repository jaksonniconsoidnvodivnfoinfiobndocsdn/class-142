import csv
with open ("movies.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]
    headers = data[0]
headers.append("poster_link")
with open ("final.csv","a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)

with open("movie_links.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movie_links = data[1:]

for movie_items in all_movies:
    poster_found = any(movie_items[8] in movie_links_items for movie_link_items in all_movie_links )
    if poster_found:
        for movie_link_item in all_movie_links:
            if movie_items[8]== movie_link_item[0]:
                movie_items.append(movie_link_item[1])
                if len(movie_items) == 28:
                    with open("final.csv","a+") as f :
                        csv_writer = csv.writer(f)
                        csv_writer.writerow(movie_item)