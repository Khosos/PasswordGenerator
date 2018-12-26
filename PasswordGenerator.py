import random

def generatePassword ():
    numLowerCase = numUpperCase = numSpecialCase =  numNumber = 0
    password = ""
    randomChars = "-|@.,?/!~#%^&*(){}[]\=*"
    length = random.randint(10, 25)

    while(numSpecialCase < 1 or numNumber < 1 or numLowerCase < 1 or numUpperCase < 1):
        password = ""
        numLowerCase = numUpperCase = numSpecialCase =  numNumber = 0
        
        for i in range (length):
            charType = random.randint(0, 3)
        
            #lowercase letters
            if(charType == 0):
                password+= chr(random.randint(97, 121))
                numLowerCase+=1
                
            #uppercase letters
            elif(charType == 1):
                password+= chr(random.randint(65, 90))
                numUpperCase+=1
                
            #number letters
            elif(charType == 2):
                password+= chr(random.randint(48, 57))
                numNumber+=1
                
            #special characters
            else:
                password+= randomChars[random.randint(0, len(randomChars)-1)]
                numSpecialCase+=1

    return password

def main():
    print(generatePassword())
    
main()
