#  This is one of the simple python projects yet an exciting one. You 
#  can even call it a mini-game. Make a program in which the 
#  computer randomly chooses a number between 1 to 10, 1 to 100, or 
#  any range. Then give users a hint to guess the number. Every time 
#  the user guesses wrong, he gets another clue, and his score gets 
#  reduced. The clue can be multiples, divisible, greater or smaller, or a 
#  combination of all<



from random import randint


def case(x, y):
    comp_io = randint(x, y)
    agnst = randint(comp_io-2, comp_io+5)

    clues = {
    1:f"the number divided by 2 is {comp_io/2}", 
    2:f"This number multiplied by 3 is {comp_io*3}", 
    6:f"this number being greater than {agnst} is {comp_io>agnst}", 
    3:f"this number being lesser than {agnst} is {comp_io<agnst}", 
    4:f"this number being greater than {agnst} is ____ and divided by 2 is equal ___ .{comp_io>agnst, comp_io/2}", 
    5:f"You have really tried,  the number is {comp_io}"
    }
    itr = 4
    while itr > 0:
        user_io = int(input('Guess the number: '))
        if user_io == comp_io:
            print('congratulations you guessed correctly !!!')
            break
        elif itr > 1:
            print('Try again !! :: '+clues[itr]+'\n guess the number')
            itr = itr - 1
        else:
            print(f'you Lose!!, \n {clues[5]}, refresh program!! ')
            break

# def case()
task = "\n\tWELCOME\n\t\tTO THE\n\t\t\tNUMBER\n\t\t\t\tGUESSING\n\t\t\t\t\tGAME"+"\nPlease enter the corresponding range you want : 1(1-10), 11(11-30), 111(1-100), 1111(20-100): \n"

def start():
    use = input(task)
    l = len(use) # length
    if l == 1:
        case(1, 10)
    elif l == 2:
        case(11, 30)
    elif l == 3:
        case(1, 100)
    elif l == 4:
        case(20, 100)



start()