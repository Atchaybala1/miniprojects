import random
lst=['s','w','g']

chance=10
no_of_chance=0
computer_point=0
human_point=0

print("\t\t\t\t\t snake,water,gun game \n\n")
print("s for snake \n w for water \n g for gun \n")

#iterate chances with while

while no_of_chance<chance:
    _input=input("snake,water,gun")
    _random=random.choice(lst)

    if _input==_random:
        print("tie both \n")

    elif _input=='s' and _random=='g':
        computer_point=computer_point + 1
        print(f"your guess is {_input} and computer score is {_random}\n")
        print("computer wins this time \n")
        print(f"computer point is {computer_point} and your point is {human_point}")
    
    elif _input=='s' and _random=='w':
        human_point += 1
        print(f"your guess is {_input} and computer guess is {_random} \n")
        print(f"you win this time")
        print(f"computer point is {computer_point} and your point is {human_point} \n")
    
    elif _input=='w' and _random=='g':
        human_point += 1
        print(f"your guess is {_input} and computer score is {_random} \n")
        print(f"you win this time\n")
        print(f"computer score is {computer_point} and human score is {human_point}\n")

    elif _input=='w' and _random=='s':
        computer_point+=1
        print(f"your guess is {_input} and computer guess is {_random} \n")
        print(f"computer wins this time \n")
        print(f"computer point is {computer_point} and your point is {human_point} \n")

    elif _input=='w' and _random=='g':
        human_point+=1
        print(f"your guess is {_input} and computer guess is {_random}\n")
        print("you win this time \n")
        print(f"the computer score is {computer_point} and your score is {human_point} \n")
    #for g
    elif _input=='g' and _random=='s':
        human_point+=1
        print(f"your guess is {_input} and computer guess is {_random} \n")
        print("ypu win this time \n")
        print(f"the computer score is {computer_point} and your score is {human_point} /n")

    elif _input=='g' and _random=='w':
        computer_point+=1
        print(f"your guess is {_input} and computer guess is {_random} \n")
        print("computer win this time \n")
        print(f"th computer score is {computer_point} and human score is {human_point} \n")

    else:
        print("you have a wrong input")

    no_of_chance+=1
    print(f"{chance - no_of_chance} is left out of {chance}")

print("game over")

if human_point==computer_point:
    print("THE GAME IS TIED")
elif human_point<computer_point:
    print("the computer wins")
else:
    print("the human wins")

print("FINALLY")
print(f"\t \t \t \t the overall score is: \n computer score: {computer_point} \n your score is: {human_point}")
