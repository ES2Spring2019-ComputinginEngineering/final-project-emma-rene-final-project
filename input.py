# functions file - create test point from user input

def testpoint():
    instructions = """For age, enter a number between 0 (meaning somewhere 
    between 1 month and  a year) and 100. For social class, enter 1 for first
    class, 2 for second class, and 3 for third class, or enter 0 for crew. For 
    sex, enter M for male or F for female."""
    print(instructions)
    agenumber = int(input("Enter age: "))
    if agenumber <= 16:
        age = 1
    else:
        age = 0
    socialclass = int(input("Enter social class: "))
    sexnumber = input("Enter sex: ")
    if sexnumber == 'M' or sexnumber == 'm':
        sex = 0
    else:
        sex = 1
    return sex, age, socialclass

sex, age, socialclass = testpoint()
