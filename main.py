
# Main Menu screen, runs on program start
def mainMenu():
    print('*****************************************************')
    print('****************WELCOME TO GOOBER BANK***************')
    print('*****************************************************')
    print('******Please select a menu option********************')
    print('*****************************************************')
    print('******1. Check Balance*******************************')
    print('******2. Withdrawal**********************************')
    print('******3. Deposit*************************************')
    print('*****************************************************')
    print('*****************************************************')


def checkInput():
    selection = int((input('Option: ')))
    if selection not in [1,2,3]:
        print('Please select a valid option')
    else:
        if selection == 1:
            #check balance
            print('checking balance')
        elif selection == 2:
            #withdrawal
            print('withdrawal')
        elif selection == 3:
            #deposit
            print('deposit')


# calls mainMenu screen
mainMenu()

# calls checkInput for selection
checkInput()