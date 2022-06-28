# #CASTING CONCEPT

# print(int(5.9))
# #this will always round down

# print(int("54"))
# #changes from int data type into int data type.

# print(int(round(5.9)))
# #this allows you to round up floating points.

# print(type(int("54")))
# #proof of above code. the type data type show what data type it is.

# # print(int("one"))
# #this provides a value error. it is impossible

# balance = 100
# deposit = int(input("How much do you want to deposit?"))
# balance +=deposit
# print(f"you have {balance}")
# #in this code, you must have int(input())). if int is not include, it is concatenation and will not work.

# print("What is your name?")
# name = input()
# #in the below if/else statement, there is nothing after name. this means this route will only take truthy inputs.
# if name:
#     print("Welcome {name} to Innovate!")
# else:
#     print("You did not submit a name.")
# #the else statement only takes falsey inputs. these are: "", 0, 0.0 and false


# day="Monday"
# bank_hol = True
# #both of these variables are truthy. anything other than "", 0, 0.0, False is truthy and would be accepted.
# if day =="Saturday" or day =="Sunday" or bank_hol:
#     print("YAY, a day off")
# else:
#     print("Off to innovate we go.")
# #this code is specifically an example of looking for bank_hol to be truthy.

# allowed=["Andy","Bob","Carol","Dean"]
# name=input("What is your name?")
# #"not in" allows you to check if the input is truthy or falsy.
# while name not in allowed:
#     print("Your name isn't on the list.")
#     print("Try again.")
#     name=input("What is your name?")
# print("You can come in.")
# #This while loop will loop until the user provides a name that is in the list.
# #if __ in answer: is a way to iscolate a string in an input. if str is found, it is truthy.

# deposit = int(input("How much do you want to deposit?")). this is a fatal error.
# a fatal error is an error in the code that stops it from working completely.

# def add_up():
#     num1 = input("What is the first number you'd like to add up? \n ")
#     num2 = input("What is the seecond number you'd like to add up? \n ")
#     print(int(num1) + int(num2))


#
def add_up():
    num1 = input("What is the first number you'd like to add up? \n ")
    num2 = input("What is the seecond number you'd like to add up? \n ")
#
    try:
        print(int(num1) + int(num2))
    except:
        print("Please use numbers only")
        add_up()
add_up()
#this is successful code that will not give you an error.







