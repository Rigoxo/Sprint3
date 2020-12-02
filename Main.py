__author__ = 'Rigoberto Diaz'

#  This program is basically a math study application, The user will select a specific subject in math
# and the program will send the users question till the user masters the subject.# The user masters a subject once
# they get at least 7 question right without hitting the limit of wrongs, the user only has 3 freebies before the
# whole progress is restarted# ##Citations###
import math
import random


def main():
    username = input("Please enter your name to begin: ")
    print("Hello " + username + " Welcome to GURU\nThis program will help you improve your skills in math in no time.")
    subjectselection(username)


def subjectselection(username):
    print("Please pick a subject in math you'd like to work on: ")
    subjectarray = ['Addition', 'Subtraction', 'Multiplication',
                    'Division', 'Multiplication by exponents', 'Even or Odd', 'Between the numbers']
    # This Array will carry all of the subjects that the user can be tested on#
    # This for function lists off all of the subjects for the user#
    for x in range(7):
        print(str(x + 1) + '. ' + str(subjectarray[x]))  # The + string operator concatenates two strings together#
    subjectchoice = input()
    while subjectchoice:
        try:
            subjectchoice = int(subjectchoice)
            # These if statements lead the user to different defined functions that will test the user until mastery#
            if subjectchoice == 1:  # The relational operators == checks if the two variables are equal and if so,
                # the condition becomes true#
                print("You chose addition!")
                addition(username)
            elif subjectchoice == 2:
                print("You chose subtraction!")
                subtraction(username)
            elif subjectchoice == 3:
                print("You chose multiplication!")
                multiplication(username)
            elif subjectchoice == 4:
                print("You chose division!")
                print("This subject can include decimals, Please round to the nearest hundredth.")
                division(username)
            elif subjectchoice == 5:
                print("You chose multiplication by exponents!")
                mbe(username)
            elif subjectchoice == 6:
                print("You chose Even or Odd!")
                print("This subject will ask you if the given number is even or odd.")
                eoo(username)
            elif subjectchoice == 7:
                print("You chose Between the numbers!")
                print("This subject will ask you to give a number between the given numbers")
                btn(username)
        except ValueError:
            print('not a valid input, please enter a number')
            subjectselection(username)


# This function will task the user to answer addition problems till mastery#
def addition(username):
    useranswer = 1
    wrongs = 0
    # This while function checks if the input by the user is an integer and resets if not#
    while useranswer:
        try:
            for progression in range(10):
                var1 = random.randint(1, 100)
                var2 = random.randint(1, 100)
                sumofequation = var1 + var2
                print("Question " + str(progression + 1) + ": " + str(var1) + " + " + str(
                    var2) + " = ?")  # The + numeric operator adds two variables together getting the sum#
                useranswer = int(input("Answer: "))
                if sumofequation == useranswer:
                    print("Good job!")
                else:
                    wrongs = wrongs + 1  # everytime the user gets the answer wrong, the number goes up by 1 till it
                    # resets
                    # back to 0 if it hits 3#
                    print('incorrect, strike #' + str(wrongs))
                    if wrongs == 3:  # this resets the progress by stopping the for loop and calling the function again#
                        print("Progression restarted")
                        addition(username)
            print("Congratulations " + username + " you have mastered this subject\nReturning to subject Selection...")
            subjectselection(username)
        except ValueError:
            wrongs = wrongs + 1
            print('incorrect, strike #' + str(wrongs))
            if wrongs == 3:  # this resets the progress by stopping the for loop and calling the function again#
                print("Progression restarted")
                addition(username)


# This function will task the user to answer subtraction problems till mastery#
def subtraction(username):
    useranswer = 1
    wrongs = 0
    while useranswer:
        try:
            for progression in range(10):
                var1 = random.randint(1, 100)
                var2 = random.randint(1, 100)
                sumofequation = var1 - var2
                print("Question " + str(progression + 1) + ": " + str(var1) + " - " + str(
                    var2) + " = ?")  # The - numeric operator subtracts the second variable from the first variable#
                useranswer = int(input("Answer: "))
                if sumofequation == useranswer:
                    print("Good job!")
                else:
                    wrongs = wrongs + 1
                    print('incorrect, strike #' + str(wrongs))
                    if wrongs == 3:
                        print("Progression restarted")
                        subtraction(username)
            print("Congratulations " + username + " you have mastered this subject\nReturning to subject Selection...")
            subjectselection(username)
        except ValueError:
            wrongs = wrongs + 1
            print('incorrect, strike #' + str(wrongs))
            if wrongs == 3:  # this resets the progress by stopping the for loop and calling the function again#
                print("Progression restarted")
                subtraction(username)


# This function will task the user to answer multiplication problems till mastery#
def multiplication(username):
    useranswer = 1
    wrongs = 0
    while useranswer:
        try:
            for progression in range(10):
                var1 = random.randint(1, 100)
                var2 = random.randint(1, 100)
                sumofequation = var1 * var2
                print("Question " + str(progression + 1) + ": " + str(var1) + " * " + str(
                    var2) + " = ?")  # The * numeric operator multiples both of the variables#
                useranswer = int(input("Answer: "))
                if sumofequation == useranswer:
                    print("Good job!")
                else:
                    wrongs = wrongs + 1
                    print('incorrect, strike #' + str(wrongs))
                    if wrongs == 3:
                        print("Progression restarted")
                        multiplication(username)
            print("Congratulations " + username + " you have mastered this subject\nReturning to subject Selection...")
            subjectselection(username)
        except ValueError:
            wrongs = wrongs + 1
            print('incorrect, strike #' + str(wrongs))
            if wrongs == 3:  # this resets the progress by stopping the for loop and calling the function again#
                print("Progression restarted")
                multiplication(username)


# This function will task the user to answer division problems till mastery#
def division(username):
    useranswer = 1
    wrongs = 0
    while useranswer:
        try:
            for progression in range(10):
                var1 = random.randint(1, 100)
                var2 = random.randint(1, 100)
                sumofequation = round((var1 / var2),
                                    2)  # This rounding function will round the number to the hundredth decimal#
                print("Question " + str(progression + 1) + ": " + str(var1) + " / " + str(
                    var2) + " = ?")  # The / numeric operator divides the first variable by the second variable#
                useranswer = float(input("Answer: "))
                if sumofequation == useranswer:
                    print("Good job!")
                else:
                    wrongs = wrongs + 1
                    print('incorrect, strike #' + str(wrongs))
                    if wrongs == 3:
                        print("Progression restarted")
                        division(username)
            print("Congratulations " + username + " you have mastered this subject\nReturning to subject Selection...")
            subjectselection(username)
        except ValueError:
            wrongs = wrongs + 1
            print('incorrect, strike #' + str(wrongs))
            if wrongs == 3:  # this resets the progress by stopping the for loop and calling the function again#
                print("Progression restarted")
                division(username)


# This function will task the user to answer multiplication by exponents till mastery#
def mbe(username):
    useranswer = 1
    wrongs = 0
    while useranswer:
        try:
            for progression in range(10):
                var1 = random.randint(1, 12)
                var2 = random.randint(2, 3)
                sumofequation = math.pow(var1, var2)
                print("Question " + str(progression + 1) + ": " + str(var1) + " to the power of " + str(
                    var2) + " = ?")  # The ** numeric operator multiplies the first variable number to the power of the
                # second variable#
                useranswer = int(input("Answer: "))
                if sumofequation == useranswer:
                    print("Good job!")
                else:
                    wrongs = wrongs + 1
                    print('incorrect, strike #' + str(wrongs))
                    if wrongs == 3:
                        print("Progression restarted")
                        mbe(username)
            print("Congratulations " + username + " you have mastered this subject\nReturning to subject Selection...")
            subjectselection(username)
        except ValueError:
            wrongs = wrongs + 1
            print('incorrect, strike #' + str(wrongs))
            if wrongs == 3:  # this resets the progress by stopping the for loop and calling the function again#
                print("Progression restarted")
                mbe(username)


# This function will ask the user if the given number is even or odd till mastery#
def eoo(username):
    wrongs = 0
    for progression in range(10):
        var1 = random.randint(1, 1000)
        if (
                var1 % 2 != 0):  # The numeric operator % divides the first variable by the second variable and
            # returns the remainder The relational operators != checks if the values of both sides are equal,
            # and if not equal, it'll return as true#
            sumofequation = 'odd'
        else:
            sumofequation = 'even'
        print("Question " + str(progression + 1) + ": Is " + str(
            var1) + " even or odd?")  # The ** numeric operator multiplies the first variable number to the power of
        # the second variable#
        useranswer = input("Answer: ")
        if sumofequation == useranswer:
            print("Good job!")
        else:
            wrongs = wrongs + 1
            print('incorrect, strike #' + str(wrongs))
            if wrongs == 3:
                print("Progression restarted")
                mbe(username)
    print("Congratulations " + username + " you have mastered this subject\nReturning to subject Selection...")
    subjectselection(username)


# This function will ask the user if the given number is even or odd till mastery#
def btn(username):
    wrongs = 0
    for progression in range(10):
        var1 = random.randint(1, 500)
        var2 = random.randint(1, 500)
        while var2 > var1:
            var2 = random.randint(1, 500)
        print("Question " + str(progression + 1) + ": Enter a number that's greater than " + str(
            var2) + " and less than " + str(
            var1))  # The ** numeric operator multiplies the first variable number to the power of the second variable#
        useranswer = int(input("Answer: "))
        if var1 >= useranswer >= var2:  # This checks if the number given by the user is actually between both
            # of them
            print("Good job!")
        else:
            wrongs = wrongs + 1
            print('incorrect, strike #' + str(wrongs))
            if wrongs == 3:
                print("Progression restarted")
                btn(username)
    print("Congratulations " + username + " you have mastered this subject\nReturning to subject Selection...")
    subjectselection(username)


# This starts the program calling the main function#
main()
