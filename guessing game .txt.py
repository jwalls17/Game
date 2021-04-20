import random

def pick_num ():
    high=int(input("Please input a number" '\n'))
    low=int(input("Please input a number lower than the first" '\n'))
    computedNum= random.randint(low+1,high-1)
# the rand.int function includes the max and min values in the random selection
#of an integer, so I made it low+1 and max-1 in order to make it select a vlue
#less than the max and greater than the min
    return high, low, computedNum

def first_guess ():
    print("I am thinking of a number..." '\n')
    guess=int(input("Guess what number I am thinking of" '\n'))
    return guess

def check_answer(computedNum,user_Guess):
    if computedNum == user_Guess:
        print( "Correct! You win!" '\n')
        return True
    elif computedNum > user_Guess:
        print("Think bigger!"'\n')
        return False
    elif computedNum < user_Guess:
        print("Go smaller!" '\n')
        return False 

def main():
    high, low, computedNum = pick_num()
    gameRun=0
    while gameRun==0:
        user_Guess=first_guess()
        gameRun=check_answer(computedNum,user_Guess)
main()
