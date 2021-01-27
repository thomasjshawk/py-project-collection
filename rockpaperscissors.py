import random
import time


#player selection process
def choose():

    #define global variable and attempt to select
    global you
    you = input("Rock(r), paper(p), scissors(s)? ")

    #check for incorrect slection and loop till fixed
    while(you != "r" and you != "p" and you != "s"):
        print("Invalid entry! Choose 'r', 'p', or 's'!")
        you = input("Rock (r), paper (p), scissors (s)? ")

    #rock selected 
    if you == "r":
        print("You chose rock!")
        time.sleep(2)

    #paper selected     
    elif you == "p":
        print("You chose paper!")
        time.sleep(2)

    #scissors selected
    else:
        print("You chose scissors!")
        time.sleep(2)


#computer selection fucntion
def selector():

    #define global variable and randomly select
    global computer
    computer = random.randint(1, 3)

    #rock chosen
    if computer == 1:
        computer = "r"
        print("Computer chose rock!")
        time.sleep(2)

    #paper chosen
    elif computer == 2:
        computer = "p"
        print("Computer chose paper!")
        time.sleep(2)

    #scissors chosen
    else:
        computer = "s"
        print("Computer chose scissors!")
        time.sleep(2)  
    

#determine winner based on selections
def winner(you, computer):

    #all winning results
    if (you == "s" and computer == "p") or (you == "p" and computer == "r") or (you == "r" and computer == "s"):
        print("You win!")

    #all losing results
    elif (you == "p" and computer == "s") or (you == "r" and computer == "p") or (you == "s" and computer == "r"):
        print("You lose!")

    #all ties
    else:
        print("It's a tie!")


#main function structure
def main():

    #welcome and establish looping variable
    print("Welcome to rock, paper, scissors!")
    newGame = 'Y'
    
    #while loop to allow user to exit the calculator when finished
    while(newGame != "N" and newGame != "n"):
        choose()

        selector()

        winner(you, computer)

        #asking if they want to play again, changing variable to break while loop if desired
        newGame = input("Would you like to play again?(Y/N): ")
        while(newGame != "Y" and newGame != "y" and newGame != "N" and newGame != "n"):
            print("Please enter Y or N")
            newGame = input("Would you like to play again?(Y/N): ")
                
    else:
        print("Goodbye!")


if __name__ == "__main__":
    main()
    













    
