import random

answer_sports=["Sports","sports"]
answer_animals=["Animals","animals"]
answer_bts_members=["BTS members","bts members"]

required_category=("Please pick a category")
number_of_guess=0

def guessing_game():
    enter=(input("Welcome to the guessing game! Press Enter to continue"))
    print("""choose your category:
    Sports
    Animals
    BTS members""")
    choice=input()
    if choice in answer_sports:
        category_sports()
    elif choice in answer_animals:
        category_animals()
    elif choice in answer_bts_members:
        category_bts_members()
    else:
        print(required_category)
        guessing_game()

def category_sports():
    number_of_guess=0
    #answer_baseball=["Baseball"]
    #answer_basketball=["Basketball"]
    #answer_football=["Football"]
    #answer_soccer=["Soccer"] 
    #answer_golf=["Golf"]
    f_answer_sports=random.choice(["Baseball","Basketball","Football","Soccer","Golf"])
    #print("f_answer_sports", f_answer_sports)
    print("""Spelling counts! Here are the possible answers:
    Baseball
    Basketball
    Football
    Soccer
    Golf
Before we get into hints, what sport do you think I am thinking about?:""")
#'here is the first hint!
#Finishedneed to make command that runs hint: to do that, i need to make command that knows what sport the program chose and output the hints for that sport
#Finishedmake hint_all and put all hints into that variable
    hint_baseball=(["You use a bat","Gloves are used in this game"])
    hint_basketball=(["You use your hands to hold the ball","The ball must end up through the net"])
    hint_football=(["The court is marked by yardlines","Helmets are used to protect the player's head"])
    hint_soccer=(["The players use their feet to move the ball","This sport has many names if you are in the UK or the US"])
    hint_golf=(["This sport is considered a rich person's sport","For this sport, you want to score the lowest amount of points to win"])
    #sports_hints=random.choice([hint_baseball,hint_basketball,hint_football,hint_soccer,hint_golf])
    #print(sports_hints)
    #for f_answer_sports in hint_baseball:
    def sport_hints():
        if f_answer_sports=="Baseball":
            print(random.choices(hint_baseball))
            #print(hint_baseball[1])
        #if guess != f_answer_sports:
            #print(hint_baseball[1])
        elif f_answer_sports=="Basketball":
            print(random.choices(hint_basketball))
        #if guess != f_answer_sports:
            #print(hint_basketball[1])
        elif f_answer_sports=="Football":
            print(random.choices(hint_football))
        #if guess != f_answer_sports:
            #print(hint_football[1])
        elif f_answer_sports=="Soccer":
            print(random.choices(hint_soccer))
        #if guess != f_answer_sports:
            #print(hint_soccer[1])
        elif f_answer_sports=="Golf":
            print(random.choices(hint_golf))
        #if guess != f_answer_sports:
            #print(hint_golf[1])
    while number_of_guess < 5:
        guess=input()
        number_of_guess += 1
        if guess==f_answer_sports:
            break
        if guess!=f_answer_sports:
            print("Wrong guess! Here is a hint:")
            sport_hints()
            #print(sports_hints)
    if guess == (f_answer_sports):
        print("Congratulations, you guessed the sport I am thinking of!")
    else:
        print("You didn't guess the sport. The answer is " +f_answer_sports)

def category_animals():
    number_of_guess=0
    f_answer_animals=random.choice(["Giraffe","Octopus","Lion","Turtle","Sea Otter"])
    #print("f_answer_animals", f_answer_animals)
    print("""Spelling counts! Here are the possible answers:
    Giraffe
    Octopus
    Lion
    Turtle
    Sea Otter
Before we get into hints, what sport do you think I am thinking about?:""")
#'here is the first hint!'
#Finished! need to make command that runs hint: to do that, i need to make command that knows what sport the program chose and output the hints for that sport
#Finished! make hint_all and put all hints into that variable
    hint_giraffe=(["This is the tallest mammal in the world","The females give birth standing up"])
    hint_octopus=(["This animal has three hearts","These animals are very good at camouflage"])
    hint_lion=(["These animals live in groups called prides","Females do most of the hunting"])
    hint_turtle=(["These animals lay their eggs in the sand","These animals can stay underwater for a long period of time before having to come back up for air"])
    hint_sea_otter=(["These animals have a pocket to keep their rock in","These animals are known as a Keystone species"])
    def animal_hints():
        if f_answer_animals=="Giraffe":
            print(random.choices(hint_giraffe))
        elif f_answer_animals=="Octopus":
            print(random.choices(hint_octopus))
        elif f_answer_animals=="Lion":
            print(random.choices(hint_lion))
        elif f_answer_animals=="Turtle":
            print(random.choices(hint_turtle))
        elif f_answer_animals=="Sea Otter":
            print(random.choices(hint_sea_otter))
    while number_of_guess < 5:
        guess=input()
        number_of_guess += 1
        if guess==f_answer_animals:
            break
        if guess!=f_answer_animals:
            print("Wrong guess! Here is a hint:")
            animal_hints()
            #print(sports_hints)
    if guess == (f_answer_animals):
        print("Congratulations, you guessed the sport I am thinking of!")
    else:
        print("You didn't guess the sport. The answer is " +f_answer_animals)

def category_bts_members():
    number_of_guess=0
    f_answer_bts_members=random.choice(["RM","V","J-Hope","Jimin","Suga","Jungkook","Jin"])
    #print("f_answer_bts_member", f_answer_bts_member)
    print("""Spelling counts! Here are the possible answers:
    RM
    V
    J-Hope
    Jimin
    Suga
    Jungkook
    Jin
Before we get into hints, what sport do you think I am thinking about?:""")
#'here is the first hint!'
#Finished! need to make command that runs hint: to do that, i need to make command that knows what sport the program chose and output the hints for that sport
#Finished! make hint_all and put all hints into that variable
    hint_rm=(["This member taught himself how to speak english by watching Friends","This member was the first to join BTS"])
    hint_v=(["This member takes pictures under the name Vante","This member speaks Japanese very well"])
    hint_j_hope=(["This member was well know in the Gwangju dance underground","This member first auditioned at JYP"])
    hint_jimin=(["This member was the top student in modern dance","This member is often teased about his height"])
    hint_suga=(["This member also goes by Agust D","This member dog's name is Holly"])
    hint_jungkook=(["This member is the youngest of the group","This member has lots of tattoos on his body"])
    hint_jin=(["This member's nickname is Worldwide Handsome","This member often plays Maplystory"])
    def bts_members_hints():
        if f_answer_bts_members=="RM":
            print(random.choices(hint_rm))
        elif f_answer_bts_members=="V":
            print(random.choices(hint_v))
        elif f_answer_bts_members=="J-Hope":
            print(random.choices(hint_j_hope))
        elif f_answer_bts_members=="Jimin":
            print(random.choices(hint_jimin))
        elif f_answer_bts_members=="Suga":
            print(random.choices(hint_suga))
        elif f_answer_bts_members=="Jungkook":
            print(random.choices(hint_jungkook))
        elif f_answer_bts_members=="Jin":
            print(random.choices(hint_jin))
    while number_of_guess < 7:
        guess=input()
        number_of_guess += 1
        if guess==f_answer_bts_members:
            break
        if guess!=f_answer_bts_members:
            print("Wrong guess! Here is a hint:")
            bts_members_hints()
            #print(sports_hints)
    if guess == (f_answer_bts_members):
        print("Congratulations, you guessed the sport I am thinking of!")
    else:
        print("You didn't guess the sport. The answer is " +f_answer_bts_members)

guessing_game()