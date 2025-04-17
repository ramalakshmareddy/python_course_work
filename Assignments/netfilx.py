# Accepting different data types as input
movie_name = input("Enter movie name: ")  # str
director_name = input("Enter director name: ")  # str
movie_review = input("Enter movie review: ")  # str
rating = float(input("Enter rating: "))  # float
release_year = int(input("Enter release year: "))  # int
languages = set(input("Enter language: ").split(","))  # set
is_available = bool(input("Is the movie available? (True/False): "))  # bool
cast = input("Enter cast (comma-separated): ").split(",")  # list
genres = tuple(input("Enter genres (comma-separated): ").split(","))  # tuple
subtitles = set(input("Enter subtitles (comma-separated): ").split(","))  # set
runtime_budget = {"runtime": input("Enter runtime: "), "budget": input("Enter budget: ")}  # dict

#comma method 
print("movie_name:",movie_name,"director_name:",director_name,"movie_review:",movie_review,"rating:",rating,sep=",")
print("languages:",languages,"release_year:",release_year,"is_available:",is_available,"cast:",cast,"genres:",genres,"subtitles:",subtitles,"runtime_budget:",runtime_budget ,sep=",")
#using f() method
print(f"\n movie_name:{movie_name} director_name:{director_name} movie_review:{movie_review}rating:{rating}release_year:{release_year}",sep="/")
print(f"languages:{languages} is_available:{is_available} cast:{cast} genres:{genres} subtitles:{subtitles} runtime_budget:{runtime_budget}",sep="/")

#.format method     
print("\n movie_name:{}|director_name:{}|movie_review:{}||rating:{}|release_year:{}".format(movie_name,director_name,movie_review,rating,release_year,))
print("languages:{}|is_available:{}|cast:{}|genres:{}|subtitles:{}|runtime_budget:{}".format(languages,is_available,cast,genres,subtitles,runtime_budget,))

#%f format method
print("\n movie_name:%s|director_name:%s|movie_review:%s|rating:%.2f|release_year:%d"%(movie_name,director_name,movie_review,rating,release_year))
print("languages:",languages,"is_available:",is_available,"cast:",cast,"genres:",genres,"subtitles:",subtitles,"runtime_budget:",runtime_budget,sep="|")
