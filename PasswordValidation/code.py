#validate a password with at least 8 characters, an uppercase letter and a number

def passValidator(pwd):
    has_SmChar = False
    has_upChar = False
    has_numChar = False


# Lowercase letters
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
# Uppercase letters
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# nos
    numbers = '1234567890'
    
    if len(pwd) <8:
        print("Password less than 8 digits!!!!!")
        return 
    valueSaved = commonPasswordChecker(pwd)
    if(valueSaved):
        print("Select a Strong Password These Passwords are Common and cause threats !")
        return
    print(f"-------this is the {pwd}=======didn't change as made in local (understand local scope and globals cope )")
    for eachChar in pwd:
        if eachChar.islower():
            has_SmChar = True
        elif eachChar.isupper():
            has_upChar = True
        elif eachChar.isdigit() :
            has_numChar = True
    if(has_SmChar)and(has_upChar)and(has_numChar):
        print("Strong Password....!")
    else:
        print("Enter Mixed Digits!....")

inputPwd = input("-Enter The Text -   ")

def commonPasswordChecker(pwd):
        common_passwords = [
    "password", "123456", "12345", "123456789", "qwerty", "abc123", "letmein", "welcome", 
    "admin", "1234", "password1", "123123", "monkey", "dragon", "sunshine", "iloveyou", 
    "qwertyuiop", "1q2w3e4r5t", "123qwe", "password123", "123321", "password1", "admin123", 
    "root", "trustno1", "letmein123", "shadow", "welcome1", "123qwerty", "111111", "1234qwer"
]
        pwd = pwd.lower() #locally changed !! won't affect 
        for eachElem in common_passwords:
            if eachElem == pwd:
                return True
        return False   
            
passValidator(inputPwd)

