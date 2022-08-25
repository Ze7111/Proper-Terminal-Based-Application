"""

This is what everyone will see when they run the program.

"""

from rich import console
import os, platform, time
from backend.classes.file_class import file_opperations, JSON_read
from frontend.core.help_sh import Help_Functions__Base as HFB
from frontend.client.sort_script import sort_and_cleaner as SAC

color = JSON_read.read_color_hex # read the color hex from the config file
print = console.Console().print # print function
cleard: str = "cls" if platform.system() == "Windows" else "clear" # clear command for windows and linux and mac
shell_color = 'quaternary'
pallate = 0


class CMDInterface:
    def Input_Interface(condition: str = None):
        if condition == 'dont clear':
            pass
        else:
            os.system(cleard)
            
        print(f" ", style=color(shell_color, pallate))
        print(f"┌─── ({__file__}) - ['admin']  ", style=color(shell_color, pallate))
        print(f"└── $ ", style=color(shell_color, pallate), end='')
        userinput = input("")

        SAC(shell_color, pallate, userinput)
            
        CMDInterface.Input_Interface('dont clear')
            
        
        
    def Output_Interface():
        pass


if __name__ == '__main__':
    CMDInterface.Input_Interface()
    



