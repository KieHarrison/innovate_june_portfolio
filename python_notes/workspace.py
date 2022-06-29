# welcome = "welcome to code nation."
# print(welcome)
# num = len(welcome)
# print("There are", num ,"characters in the welcome message.")
#activity 1

welcome = "welcome to code nation."
num = len(welcome)
val = num%2
if val == 0:
    print(welcome,".", "there are an even amount of character in the welcome message as there are", num,"characters in the previous scentence")
else:
    print(welcome, "there is an odd number of characters in the welcome message")
# activity 2

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
for i in alphabet:
    print(i)

alph_num = int(input("type a number from 1-26 that corresponds to a letter in the alphabet. \n"))
alph_num = alph_num-1
new_alph = alphabet[int(alph_num)]
print("you have chosen the letter", new_alph)
# this code asks the user to input a number corresponding to a letter in the alphabet.
# the code will print the letter corresponding to the number they chose.


#activity 1 - teachers basic code
# test_string = "Welcome to code nation"

# string_len = len(test_string)

# def odd_even_checker():
#     if string_len%2==0:
#         print("The length of the string {test_string} is {string_len} and it is even")
# else:
#     print("The length of the string {test_string} is {string_len} and it is odd")

# odd_even_checker()







#activity 1 teachers better code: 
# test_string = "Welcome to code nation"

# string_len = len(test_string)

# def odd_even_checker(test_string):
#     string_len = len(test_string)
#     if string_len%2==0:
#         print("The length of the string {test_string} is {string_len} and it is even")
# else:
#     print("The length of the string {test_string} is {string_len} and it is odd")

# odd_even_checker("hello")
# odd_even_checker("hellos")
# odd_even_checker("hellosss")
# odd_even_checker("hey")




# activity 2 teachers basic code:
# alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# for i in alpha:
#     print(i)

# answer=int(input("Type a number to see the corresponding letter."))
# answer -=1
# print(alpha[answer])



