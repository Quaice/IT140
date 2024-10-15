# main.py
import CheckPrime

def InputHandler(_func):
    if _func == "lf":
        print("lf : List Functions : Prints this helpful list of functions.")
        print("e : Exit Function : Returns you to the main prompt.")
        print("q : Quit : Terminates the program.")
        print("cp : Check Prime : Enter a number to check if it is a prime number.")
        print("sn : Scientific Notation : Converts a number to scientific notation and vice versa.")
        return
    if _func == "e":
        return True
    if _func == "q":
        quit("Program Terminated.")
    if _func == "cp":
        mode = 'cp'
        CheckPrime.CheckPrime().loop()
        return True



if __name__ == '__main__':
    mode = ''
    print("Enter 'lf' to list available functions. Otherwise, enter a function.")
    while True:
        if mode != '': print("MODE: {}".format(mode.upper()))
        InputHandler(input("[{}]> ").format(mode))
