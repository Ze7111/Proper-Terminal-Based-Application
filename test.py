import os, platform, time
from rich import console

def print_innit_message():
    print = console.Console().print
    print("Initializing...",style='green', justify = "center")
    time.sleep(0.4)
    print("Validating...",style='green', justify = "center")
    time.sleep(0.4)
    print("Loading...",style='green', justify = "center")
    
    


def text_in_the_middle():
    for i in range(7):
        color = 'red' if i % 2 == 0 else 'black'
        print = console.Console().print
        size = os.get_terminal_size() # get the size of the terminal
        size = str(size)        
        lines = list(size.split('lines'))[1] # get the number of rows
        lines = str(lines[1:3])
        lines = int(lines) # convert to int
        lines = round(lines / 4 -3)
        print(lines)
        os.system('cls' if platform.system() == "Windows" else 'clear') # clear the screen
        for i in range(lines):
            print('\n')
        
        print("""
  ██████╗ ██████╗ ██████╗ ███████╗███████╗     █████╗  ██████╗████████╗██╗██╗   ██╗███████╗
 ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝    ██╔══██╗██╔════╝╚══██╔══╝██║██║   ██║██╔════╝
██║     ██║   ██║██║  ██║█████╗  ███████╗    ███████║██║        ██║   ██║██║   ██║█████╗  
██║     ██║   ██║██║  ██║██╔══╝  ╚════██║    ██╔══██║██║        ██║   ██║╚██╗ ██╔╝██╔══╝  
 ╚██████╗╚██████╔╝██████╔╝███████╗███████║    ██║  ██║╚██████╗   ██║   ██║ ╚████╔╝ ███████╗
  ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚══════╝    ╚═╝  ╚═╝ ╚═════╝   ╚═╝   ╚═╝  ╚═══╝  ╚══════╝""",style= color, justify = "center")
        for i in range(lines):
            print('\n')
        time.sleep(1)
    print_innit_message()
    

    
    
text_in_the_middle()