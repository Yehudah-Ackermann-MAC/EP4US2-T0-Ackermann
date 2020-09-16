import random
options=('R','P','S')
print("Enter R for ROCK, P for PAPER, S for SCISSORS")
user=input("ROCK-PAPER-SCISSORS-SHOOT")
if user not in options:
    print("invalid entry. YOU LOSE!")
    quit()
comp=random.choice(options)
print(comp)

if user=='R':
    if comp=='R':
        print("TIE GAME. YOU LOSE!")
    elif comp=='P':
        print("PAPER BEATS ROCK. YOU LOSE!")
    elif comp=='S':
        print("ROCK BEATS SCISSORS...YOU STILL LOSE!")
    quit()

if user=='P':
    if comp=='R':
        print("PAPER BEATS ROCK...YOU STILL LOSE!")
    elif comp=='P':
        print("TIE GAME. YOU LOSE!")
    elif comp=='S':
        print("SCISSORS BEATS PAPER. YOU LOSE!")
    quit()

if user=='S':
    if comp=='R':
        print("ROCK BEATS SCISSORS.YOU LOSE!")
    elif comp=='P':
        print("SCISSORS BEATS PAPER...YOU STILL LOSE!")
    elif comp=='S':
        print("TIE GAME. YOU LOSE!")
    quit()