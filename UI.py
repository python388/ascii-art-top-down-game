import replit

def printPrompt(prompt):
    if prompt == '':
        pass
    else:
        print(prompt)

def printMenu(menu, select, prompt):
    replit.clear()
    printPrompt(prompt)
    for index, value in enumerate(menu):
        if index == select:
            print('--> ' + str(value))
        else:
            print(value)

def dropDown(prompt, *options):
    select = 0
    while True:
        printMenu(options, select, prompt)
        action = input('')
        if action == 'w' and select > 0:
            select -= 1
        elif action == 's' and select < len(options) - 1:
            select += 1
        elif action == 'z':
            return options[select]

def dropDownNumber(prompt, *options):
    select = 0
    while True:
        printMenu(options, select, prompt)
        action = input('')
        if action == 'w' and select > 0:
            select -= 1
        elif action == 's' and select < len(options) - 1:
            select += 1
        elif action == 'z':
            return select

def display(text):
    dropDown(text, 'ok')