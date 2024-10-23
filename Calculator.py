## CS 130 Coding Assignment 1 - Calculator.py

## Please enter the names of your group members here (or yours if you are working alone)

## [Jeramiah Mendodoza]
## [Seb]

## If working as part of a group, explain what parts of the assignment each member worked on

## [Insert your division of work here if working as a group]


## Welcome to your first full-fledged coding assignment. So far you have
## written code as smaller pieces geared towards a single task. This time
## around, you will be writing code that functions as parts of a larger
## program. Some parts of the program have already been written for you,
## while you have to fill in some of the other parts for this program.
## The sections in which you will have to write code are labeled as
## TODO, and these are the only sections where you have to write code.

## For this assignment, you will be implementing parts of a calculator program, that
## can perform the following operations:
##      1.Add numbers indefinitely
##      2.Multiply numbers indefinitely
##      3.Subtract numbers indefinitely
##      4.Divide numbers indefintely
## Each of these operations can process floats and int numbers. An operation should
## take values until the user types the word 'stop'. When the operation encounters
## 'stop' it RETURNS the final value from the operation back to the main calculator,
## which stores it for use in future operations. The calculator will stop execution
## when the user types the command to stop it.
## For each of these operations, you will be filling out their procedures to:
##      1. Take input from the user for numbers to perform the operation on.
##      2. Check that the input is valid (division by 0 is not allowed for instance)
##      3. Return the final result when the user wants to stop.


## This procedure runs the main calculator. It implements the menu and calls the other
## procedures depending upon the command entered by the user. DO NOT MODIFY THIS PROCEDURE.
def runCalculator():
    print('Welcome to the Python calculator!')
    running = True # this variable stores if the calculator has to still run
    data_store = 0 # this variable stores the results from operations that have been applied
    while running:
        ## print the currently stored value and print the menu for the user to select
        print('The current stored value is: ', data_store)
        print('Please select from the following options by typing the option number and pressing Enter:')
        print('\n')
        print('1. Add numbers to the current stored data.')
        print('2. Subtract numbers from the current stored data.')
        print('3. Multiply numbers with the current stored data.')
        print('4. Divide the currently stored data by some numbers.')
        print('5. Stop the calculator')

        ## take input from the user. The try-except code blocks here prevent incorrect entries
        ## from crashing the program.
        try:
            user_input = int(input('\nPlease enter your desired option number [1-5]: '))

            ## call operation procedure based on user input
            if   user_input == 1: ## add numbers
                data_store = runAdder(data_store)
            elif user_input == 2: ## subtract numbers
                data_store = runSubtractor(data_store)
            elif user_input == 3: ## multiply numbers
                data_store = runMultiplier(data_store)
            elif user_input == 4: ## divide numbers
                data_store = runDivider(data_store)
            elif user_input == 5: ## end program
                running = False
            else:
                print('You have entered an incorrect option, please enter the right option number')
        except:
            print('You have entered an incorrect option, please enter the right option number')
    print('The final result of your operations is: ', data_store)
    print('Have a nice rest of your day!')


## The procedures you have to complete are placed here:

def runAdder(data_store):
    ## TODO: add your code here to add numbers indefinitely to the input value until
    while data_store != 'stop':
        data_store = data_store +
    ## the user types 'stop'

    return 1 # change this line to return the final result of your operations

def runSubtractor(data_store):
    ## TODO: add your code here to subtract numbers indefinitely to the input value until
    ## the user types 'stop'

    return 1 # change this line to return the final result of your operations

def runMultiplier(data_store):
    ## TODO: add your code here to multiply numbers indefinitely with the input value until
    ## the user types 'stop'

    return 1 # change this line to return the final result of your operations

def runDivider(data_store):
    ## TODO: add your code here to divide the input value with numbers until
    ## the user types 'stop'.
    ## NOTE: your code should not let the user divide by zero. Bad things happen when you
    ## try to divide by zero.

    return 1 # change this line to return the final result of your operations




## Uncomment the following line to test your code

#runCalculator()
