#ACTIVITY 1#
#define number. define allows you to run a code with one line.
#print instructions (display message)
#userinput number.
#try - user inputs - if an integer, print the number and data type.
#except - anything that isnt an integer will lead you here.
#^^^ ask the user to enter a whole number. add another input here to allow the code to loop until int given.
#call fo function
# def Number():
#     displayMessage = "Please enter a whole number"
#     print(displayMessage)
#     num = input()
#     try:
#         print(type(int(num)))
#         print(f"Your number is {num}")
#     except:
#         print("Please enter a whole number ONLY")
#         num = input() # can also put in "number()" instead
# Number()

# #ACTIVITY 2#
#create a dictionary for countries.
countries = {
    "UK":"London",
    "France":"Paris",
    "Germany":"Berlin",
    "Spain":"Madrid",
    "Italy":"Rome"
}
#print the list/dictionary with contries to their capital
print("These are countries with their correspoding capitals.")
for i in countries.items():
    print(i)
#add 2 other contries with their capital
countries.setdefault("Japan","Tokyo")
countries.setdefault("Netherlands","Amsterdam")
#change from capital to language spoken
countries["UK"]="English"
countries["France"] = "French"
countries["Germany"] = "German"
countries["Spain"] = "Spanish"
countries["Italy"] = "Italian"
countries["Japan"] = "Japanese"
countries["Netherlands"] = "Dutch"
print("These are countries with their corresponding languages.")
for i in countries.items():
    print(i)
print("\n")
#print countries with their language spoken.
#################
#ACTIVITY 3#
#create a fav_songs list
fav_songs = [
    "Numb ",
    "Hey there delilah ",
    "Stan",
    "Welcome to the black parade"
]
print("this is a list of song names", fav_songs[::1])
#create dictionaries for each song
numb = {
    "Artist":"Lincoln Park",
    "song name":"Numb",
    "Genre":"Alternative Rock",
    "Release year":"2003"
}
htd = {
    "Artist":"Plain White T's",
    "song name":"Hey There Delilah",
    "Genre":"Alternative/Indie",
    "Release year":"2006"
}
stan = {
    "Artist":"Eminem",
    "song name":"Stan",
    "Genre":"R&B/Rap",
    "Release year":"2000"
}
wttbp = {
    "Artist":"My Chemical Romance",
    "song name":"Welcome to the black parade",
    "Genre":"Alternative Rock/ alternative indie",
    "Release year":"2006"
}
#add a user input to determine which songs details they want to see.
num = int(input("Pick a number 1-4 to find out about a song. If you ant to see them all, enter a random number.\n"))
#if else statement to organise the users answer to their prefered choice of song(s).
if num == 1:
    for n in numb.items():
        print(n)
elif num == 2:
    for h in htd.items():
        print(h)
elif num == 3:
    for s in stan.items():
        print(s)
elif num == 4:
    for w in wttbp.items:
        print(w)
else:
    #if they want to see all the details of each song they enter a random number > 4.
    for n in numb.items():
        print("Song 1", n , "\n")
    for h in htd.items():
        print("Song 2", h ,"\n")
    for s in stan.items():
        print("Song 3", s , "\n")
    for w in wttbp.items():
        print("Song 4", w ,"\n")

# Come back, there is a lot to improve.
