import enchant
dict = enchant.Dict("en_US")

while True:
    try:
        no_of_letters = int(input("Enter no. of letters in your word [range: 3-15] \n"))
        if (no_of_letters >2 and no_of_letters<16):
            break
        else:
            print("Number out of range!")
            continue
    except ValueError:
        print("Invalid value. Please enter a number!")
myletters = {}

while (len(myletters)<no_of_letters):
    #entering character
    while True:
        letter = input("Enter a character \n").lower()
        try:
            if not letter.isalpha():
                print("Invalid value. Please enter a letter")
                continue
            if (letter in myletters):
                print("You entered an existing value. Please re-enter!")
                continue
            else:
                break
        except ValueError:
            print("Invalid value. Please enter a letter!")
            
    #entering number
    while True:
        try:
            letter_num = int(input("Enter the importance of the character [1-9]"))
            if (letter_num >0 and letter_num<10):
                break
            else:
                print("Number out of range!")
                continue
        except ValueError:
            print("Invalid value. Please enter a number!")    
    myletters[letter]=letter_num
print(myletters)

letter_score = 0
word_score = 0
total_score = 0

flag = True
#loop runs for every other word
while flag == True:
    while True:
        try:
            word = input("Enter your word \n ")
            break
        except ValueError:
            print("Invalid word. Please enter a correct word")
    #checking if user entered a number
    if (word.isnumeric()):
        flag = False
        continue
    #checking if the word is real/meaningful
    if not dict.check(word):
        print("The word is not an English word. Try again!")
        continue
    #checking if the word contains only described alphabets
    for alphabet in word:
        if alphabet not in myletters:
            word_score = 0
            print("word does not contain the allowed letters")
            break
        #calculating points for that word
        letter_score = myletters[alphabet]
        word_score = word_score + letter_score
    #Following checks if every letter is utilized
    flag1 = True
    for key in myletters:
        if key not in word:
            flag1 = False
    #increments score by 50 if every letter is utilized
    if flag1 == True:
        word_score = word_score + 50
    #increments the total score
    total_score = total_score + word_score
    print("The score for this word is:", word_score)
    word_score =0

    ask_user = input("Do you want to continue?[Y/y]")
    if ask_user == 'Y' or ask_user == 'y':
        continue
    else:
        print("Thank You for playing!")
        print("Total Score:", total_score)
        break

'''import enchant
dict = enchant.Dict("en_US")


while True:
    try:
        no_of_letters = int(input("Enter no. of letters in your word [range: 3-15] \n"))
        if (no_of_letters >2 and no_of_letters<16):
            break
        else:
            print("Number out of range!")
            continue
    except ValueError:
        print("Invalid value. Please enter a number!")
myletters = {}

while (len(myletters)<= no_of_letters):
    #entering character
    while True:
        letter = input("Enter a character \n").lower()
        try:
            if not letter.isalpha():
                print("Invalid value. Please enter a letter")
                continue
            if (letter in myletters):
                print("You entered an existing value. Please re-enter!")
                continue
            else:
                break
        except ValueError:
            print("Invalid value. Please enter a letter!")
            
    #entering number
    while True:
        try:
            letter_num = int(input("Enter the importance of the character [1-9]"))
            if (letter_num >0 and letter_num<10):
                break
            else:
                print("Number out of range!")
                continue
        except ValueError:
            print("Invalid value. Please enter a number!")    
    myletters[letter]=letter_num
print(myletters)

letter_score = 0
word_score = 0
total_score = 0

flag=True
#loop runs for every other word
while flag == True:
    while True:
        try:
            word = input("Enter your word \n")
            break
        except ValueError:
            print("Invalid word. Please enter a correct word")
    #checking if user entered a number
    if (word.isnumeric()):
        flag = False
        continue
    #checking if the word is real/meaningful
    if not dict.check(word):
        print("The word is not an English word. Try again!")
        continue
    #checking if the word contains only described alphabets
    for alphabet in word:
        if alphabet not in myletters:
            word_score = 0
            print("word does not contain the allowed letters")
            break
        #calculating points for that word
        letter_score = myletters[alphabet]
        word_score = word_score + letter_score
    #Following checks if every letter is utilized
    flag1 = True
    for key in myletters:
        if key not in word:
            flag1 = False
    #increments score by 50 if every letter is utilized
    if flag1 == True:
        word_score = word_score + 50
    #increments the total score
    total_score = total_score + word_score
    print("The score for this word is:", word_score)
    word_score =0

    ask_user = input("Do you want to continue?[Y/y]")
    if ask_user == 'Y' or ask_user == 'y':
        continue
    else:
        break    
print("Thank You for playing!")
print("Total Score:", total_score)'''