print("Hello player, today we are going to play a game")
answer = input("Would you like to play?, Answer yes or no.")

if answer.lower() == "yes":
    print("Welcome, today I have a challenge for you!")

else:
    print("You are a boring")
    exit()

if answer.lower() == "yes":
    print("Guess the password and you will receive a prize!")

while True:
    try:
        #first requirement
        firsttry = input("Give me a guess: ")

        if len(firsttry) <12:
            raise Exception("Rule 1: The password is too short")
        
        #second requirement
        digitslist = []
        for letter in firsttry:
            if letter.isdigit():
                digitslist.append(int(letter)) 
        if not (sum(digitslist) == 32):
            raise Exception("Rule 2: The password must add up to 31 or 32, or 33. Find out :)") 
        
        #third requirement
        Symbols = [".",",","\\","!","@","#","$","%","^","&","*","()","[]","||","<",">","?",";",":"]
        test = []
        symbolsQuantity = 0
        for symbol in Symbols:
            test.append(symbol in firsttry) #note for future self, I added this lol
        for value in test:
            if (value):
                symbolsQuantity+=1
        if symbolsQuantity < 6:
            raise Exception("Rule 3: The password must have at least 6 symbols")
        else:
            print("Your password has 6 or more symbol, correct")
        
        #fourth requirement
        test = []
        lowercaseQ = 0
        for letter in firsttry:
            test.append(letter.islower())
        for value in test:
            if (value):
                lowercaseQ+=1
        if len(firsttry) ==5:
            raise Exception("Rule 4: The password need to have a specific amount of lowercase letters")            
        else: 
            print("Your password has 5 lowercase letters, correct")

        #fifth requirement
        test = []
        uppercaseQ = 0
        for letter in firsttry:
            test.append(letter.isupper())
        for value in test:
            if (value):
                uppercaseQ+=1
        if len(firsttry) ==4:
            raise Exception("Rule 5: The password need to have a specific amount of uppercase letters")            
        else: 
            print("Your password has 4 uppercase letters, correct")

    except Exception as e:
        print(e)
    else:
        break
      
    