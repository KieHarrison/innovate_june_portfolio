import random
# #CASTING CONCEPT

print(int(5.9))
#this will always round down

print(int("54"))
#changes from int data type into int data type.

print(int(round(5.9)))
#this allows you to round up floating points.

print(type(int("54")))
#proof of above code. the type data type show what data type it is.

# print(int("one"))
#this provides a value error. it is impossible

balance = 100
#int is important to distinguish data types. using int will make the computer only accept integers for this input.
deposit = int(input("How much do you want to deposit?"))
balance +=deposit
print(f"you have {balance}")
#in this code, you must have int(input())). if int is not include, it is concatenation and will not work.

print("What is your name?")
name = input()
#in the below if/else statement, there is nothing after name. this means this route will only take truthy inputs.
if name:
    print("Welcome {name} to Innovate!")
else:
    print("You did not submit a name.")
#the else statement only takes falsey inputs. these are: "", 0, 0.0 and false


day="Monday"
bank_hol = True
#if bank_hol was false, it is falsey.
#both of these variables are truthy. anything other than "", 0, 0.0, False is truthy and would be accepted.
if day =="Saturday" or day =="Sunday" or bank_hol:
    print("YAY, a day off")
else:
    print("Off to innovate we go.")
# this code is specifically an example of looking for bank_hol to be truthy.

#list of names on an enterance list.
allowed=["Andy","Bob","Carol","Dean"]
name=input("What is your name?")
#"not in" allows you to check if the input is truthy or falsy.
while name not in allowed:
    print("Your name isn't on the list.")
    print("Try again.")
    name=input("What is your name?")
print("You can come in.")
#This while loop will loop until the user provides a name that is in the list.
#if __ in answer: is a way to iscolate a string in an input. if str is found, it is truthy.

deposit = int(input("How much do you want to deposit?")). 
# this is a fatal error.
# a fatal error is an error in the code that stops it from working completely.


def add_up():
    num1 = input("What is the first number you'd like to add up? \n ")
    num2 = input("What is the seecond number you'd like to add up? \n ")
    print(int(num1) + int(num2))



def add_up():
    num1 = input("What is the first number you'd like to add up? \n ")
    num2 = input("What is the seecond number you'd like to add up? \n ")
#try except statements has the same layout as if else statemnts. in an if else statemnt, it searches for a specific perameters
#while try except statemnt has 2 outcomes- the first part is successful or it is given to the except part.
    try:
        print(int(num1) + int(num2))
    except:
        print("Please use numbers only")
        add_up()
# here the except part of the statemnt loops the code until the conditions of the first part is met.
add_up()
# this is successful code that will not give you an error.

light = False
#the line above is a global variable and is needed. this is 
def light_switch():
    # ##light = False##
    #^^If this is the first line of the function. whenver the function runs, light will always be set to false.
    global light
    #this lets pythin know that the initial variable is global and
    #it changes the local variable to global.
    if light:
        print("Whoa! It's bright in here")
        light = False
        #this is a local variable for light and is different from the global variable.
    #you can not change a global variable locally.
    else:
        print("Who turned out the lights?")
        light = True
light_switch()
light_switch()
# global is only used when you want to define a variable as global so it wont be local.

###TUPLES###
# tuples use normal brackets while lists use square brackets.
# this is a list- can be changed with methods:insert, remove, append, pop and more which change the lists properties.
even_nums =[2,4,6,8,10]
even_nums.append(12)
even_nums.insert(0,0)
#insert will put the number 0 at the index position 0 which is the 1st value in the list
print(even_nums)
#tuples are immutable meaning it can not change like a list.
odd_nums=(1,3,5,7,9)
odd_nums.append(11)
print(odd_nums)
# methods such as append(11) does not work on tuples, it need square brackets for it to work []
#tuples have a limited amount of methods that can be used on it.
#slice notation: fav_songs list.
fav_songs = [
    "Numb - Lincoln Park",
    "Hey there delilah - Plain White T's",
    "Stan - Eminem",
    "Welcome to the black parade - My chemical romance"
]
#index position works from slice notation.start:stop:step
print(fav_songs[1:3:1])
#starts at index pos 1 and ends at index pos 2. it increases by 1 step.
#you can slice through the whole list with print(fav_songs[1:])
#print(fav_songs[1]): this is the start value. Without the colon it will print only the starting str.

#make a string variable
#if it reads forwards the same as backwards(palindrome)
#if it does say YES if it doesnt say no
test = "hello"
#
if test == test[::-1]:
    #it starts at the start, ends at the end and because of the -1, it will go backwards.
    print(f"Yes! {test} is a palindrome")
else:
    print("it is not a palindrome")

loop_run = True
while loop_run == True:
    print("This will run forever")
    loop_run=False


num=random.randint(1,50)

while num%2==0:
    print("We like evem number! Go again.")
print("Oh no! An odd number.")
#this while loop will stop running when random num is odd.
#it compares variables and runs under specific conditions.
##################################################
#this is  a while true loop which will always initialise.
while True:
    num=random.randint(1,50)
    print(num)
    if num%2==0:
        print("We like evem number! Go again.")
        continue
    else:
        print("Oh no! An odd number.")
        break
#This is always goin to start running.
#this handles all situations. because of the if/else statement, it covers all inputs. while true














