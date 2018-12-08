import random

def generatePassword ():
    password = ""
    randomChars = "-|@.,?/!~#%^&*(){}[]\=*"
    length = random.randint(10, 25)
    
    for i in range (length):
        charType = random.randint(0, 3)
        
        #lowercase letters
        if(charType == 0):
            password+= chr(random.randint(97, 122))
            
        #uppercase letters
        elif(charType == 1):
            password+= chr(random.randint(65, 91))
            
        #special characters
        else:
            password+= randomChars[random.randint(0, len(randomChars))]

    return password

def main():
    password = generatePassword()
    print(password)
    
main()
