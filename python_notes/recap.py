# #this is how to add notes.

# print("This is my file.")

# greeting = "hello world"

# print(greeting)

# print("this is a string for displaying characters")
# print("1234") #this is a string
# print(1234+1) #this is an integer
# print(12.34)
# print(True)
# print(False)
# print(None)

# print(len(greeting))

# print(greeting[1])

# print(greeting.upper())

# print("HELLO".lower())

# print("hello EVERYONE. This is innovate".capitalize())

# 
# my_name="kie"
# # my_age=19

# # print("Hello, my name is", my_name)
# # print("My age is", my_age)

# # print("Hello my name is " + my_name)
# # print("I am " + my_age)


# #addition
# print(1+2)
# #minus
# print(3-2)
# #multiplication
# print(3*3)
# #to the power of _
# print(3**3)
# #division
# print(6/2)
# #modulus (remainder) -> 15/3 = 5r0 therefore output = 0
# print(15%3)

# balance=100
# print(balance)
# amount=20

# #updating the balance variable by adding amount
# balance=amount+balance
# #
# balance +=amount
# print(balance)
# #balance =+amount is wrong as the + is refering to the integer "amount" as a positive

#input is used when a variable/input is wanted to be given by the user
# answer=input("what is your name?")
# #answer is a variable where, here, it is attached to input. this allow the user to assign an input to the variable "answer"
# print(answer)
#\n is used to create a new line. when used with input, it forces the user to input their answer on the line below the question.
# answer=input("what is your name? \n")

# music = "classical"
# #if else statements allow multiple outcomes.
# if music == "classical":
#     print("How boring.")
#     print("No more please")
# elif music == "no music":
#     print("This is peaceful")
# else:
#     print("Turn up the tunes.")
# #if starts the statemnt giving an outcome to a specif string input. 
# #elif gives another outcome. (You can use as many elif statements as needed)
# #else is the end of the statemnt and allows inputs that do not match anything in the if's or elifs so that there is nothing in the code to give an error.

# print(10%2==0)
# #this would give the output boolean "True"
# print(10%3==0)
# #this would give the output boolean "False"

# num=10
# num2=20
# #greater than and less than are useful in if else statements when working with numbers(intergers and floats)
# if num > num2:
#     print(f"{num} is bigger.")
# elif num2 > num:
#     print(f"{num2} is bigger.")
# else:
#     print("both are equal.")

# place="MCR"
# weather="Cloudy"
# #if and else statemnts can have multiple conditions using "and".
# if place =="MCR" and weather =="Sunny":
#     print("Check again")
# elif place =="MCR" and weather=="Cloudy":
#     print("Why is it not raining?")
# else:
#     print("What is wrong with the british weather?")

# day=Saturday
# #if else statements can widen the condition that needs to be met. here there are now two conditions for the first outcome to be correct. this uses "or".
# if day =="Saturday" or day =="sunday":
#     print("It is the weekend! WOOHOO!!")
# else:
#     print("Its another working day")
# bank_hol=true
# #or can also be used for boolean variables giving possibilities of independent variable values such as bank holidays as a day off.
# if day =="Saturday" or day =="sunday" or bank_hol:
#     print("It is the weekend! WOOHOO!!")
# else:
#     print("Its another working day")

#def = define
# def light_switch():
#     print("Switching the lights.")
#     print("Activating the lights.")
# #the function (def) gives the variable (light_switch) perameters
# light_switch()
# #you can give functions perameters as seen below.
# def cash_withdraw(amount,accnum):
#     print(f"You have withdrawn {amount} from {accnum}")
# #you have to enter the line below. this gives the perameters a value.
# cash_withdraw(300,123445775)

#list are written with square brackets.
# fav_songs = [
#     "Numb - Lincoln Park",
#     "Hey there delilah - Plain White T's",
#     "Stan - Eminem"
# ]
# #lists are easy, crate the list and print using the variable.
# print(fav_songs)
print(fav_songs[1])
#this will only print the 2nd option in the list
fav_songs[1] = "Lethat combination - The Wombats"
#this updates the list, changing hey there delilah with Lethal combination. this all uses index position.
print(len(fav_songs))
#prints the number of things in the list.
fav_songs.append("Welcome to the black parade - MY Chemical Romance")
#append add another item to the end of the list.
print(fav_songs)
#using_.pop will remove an item from the list
fav_songs.pop(2)
#this will get rid of the 3rd option in the list: stan - eminem
print(fav_songs)
#prints the list without stan - eminem
