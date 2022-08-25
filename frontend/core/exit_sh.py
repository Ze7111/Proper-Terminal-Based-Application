import os, platform, time, logging
from rich import console
from backend.classes.file_class import file_opperations, JSON_read
 
def exit_sh(shell_color = 'secondary', pallate = 0, args = None):
    # var inizialization
    cleard = "cls" if platform.system() == "Windows" else "clear" # clear command for windows and linux and mac
    color = JSON_read.read_color_hex # read the color hex from the config file
    print = console.Console().print # print function
    seconds = 5 # seconds to wait before exit
    # var inizialization end
    
    if args != None:
        if type(args) == int:
            seconds = args
        elif args == 'i' or args == 'I':
            seconds = 0
        else:
            pass
    
    os.system(cleard) # clear the screen
    for i in range(seconds): # wait for seconds
        print(f"Exiting in {seconds} seconds...", style = color(shell_color, pallate)) # print the message
        time.sleep(1) # wait for 1 second
        os.system(cleard) # clear the screen
        seconds -= 1 # decrement the seconds
    exit() # exit the program