#1)check if a string is a palindrome

#we gonna use -> string method -> reversed here for this and then use conditional statements
#answer:-
def PalindromeChecker(userInput):
    print("userInput")
    newReverseString = ""
    for i in userInput:
        newReverseString = i + newReverseString # i ka value add to ist then at again 2nd value to 1st indx 3 value 1st idx ->i.e reversing (newReverstring + i -> would have gone right way but we did purposely)
    if(newReverseString == userInput):print("It matches")
    else:print("Doesn't match")
userInput  = input("Enter Your Text :- ").lower()
print(userInput)
PalindromeChecker(userInput)

PalindromeChecker("lol")


#2nd method :- slicing / easy one
#sequence-> [start:stop:step]

inp = input("Enter the string ").lower()

reversedinp = inp[::-1] # : : means start 1st se end lst tk -> step - main ho toh backwared
print(reversedinp)
if(reversedinp == inp):
    print(f"it is a palindrome i.e {reversedinp}")
else:
    print("Not a palindrome>>>>")
    