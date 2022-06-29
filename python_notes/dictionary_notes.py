# #DICTIONARY#
# name = key. salem = value
# no key duplicates are allowed.
my_cat = {
    "Name":"Salem",
    "colour":"Black",
    "Mood":"Sassy"
}
# ####



my_dog = {
    "name":"Spud",
    "Colour":"Blue",
    "Mood":"Playful"
}
Print(my_dog[2])
# ^^this does not work - key error X
print(my_dog["Mood"])
print(my_dog["name"])
#you have to target the specific key in the dictionary. O
print(f'My dog \"{my_dog["name"]} is a bit {my_dog["Mood"]} today')
#the opening speach marks must be different from the speech marks on the keys - Mood, name etc.
#also the key is surrounded by both brackets.

#you can change values in a dictionary.
my_dog["mood"] = "hungry"
# this is similar to changing a list but instead of using index, use a key to update the value.
print(my_dog.keys())

my_list=["hello","hello","goodbye"]

y = my_list.count("hello")
#this happens before everything below.
my_list.append("hello")

print(y)
# y would be 2.

x=my_dog.keys()
#keys is a view object meaning change can happen whenever using the .keys.
my_dog["age"]=2
#age would be added even though x was given a function before.
print(x)
#variables made from keys will update.
print(my_dog.values())
print(my_dog.items())
#
print(my_dog.get("Mood"))
#acts the same way as the index method.
print(my_dog.get("legs"))
#when searching for a key that doesnt exist, the get method returns the data none.
#the list method will give an error that will stop the code from working.
print(my_dog["legs"])
#

print(my_dog.keys())
#prints the list as - dict_keys([list])
print(list(my_dog.keys()))
#list horizontal
#makes it easier to see that it is a list
for i in my_dog.keys():
    print(i)
#prints list vertical.

#update method works the same as append so keys can be added
my_dog.update({"legs":"4"})
#needs curly brackets and split with a colon
my_dog.update({"name":"Buster"})
#can update keys that are already accounted for
print(my_dog)
my_dog.pop("Mood")
#.pop can remove keys.


