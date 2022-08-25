"""
This will be the syntax checker for the frontend terminal.
    
"""

from rich import console
import os, platform, time, logging
from backend.classes.file_class import file_opperations, JSON_read

print = console.Console().print # print function
cleard: str = "cls" if platform.system() == "Windows" else "clear" # clear command for windows and linux and mac
color = JSON_read.read_color_hex # read the color hex from the config file
print = console.Console().print # print function

class Help_Functions__Base:
    def __init__(self):
        pass
    
    def __call__(self, *args, **kwargs):
        pass
    
    def __str__(self):
        pass
    
    def __repr__(self):
        pass
    
    def __len__(self):
        pass
    
    def help(shell_color: str = 'secondary', pallate: int = 0):
        print("All terminal commands are listed below: \n", style=color(shell_color, pallate))
        
        shell_color = 'main'
        pallate = 0
        
        print("help - this command", style=color(shell_color, pallate))
        print("exit - exits the program", style=color(shell_color, pallate))
        print("clear - clears the screen", style=color(shell_color, pallate))
        print("reset - resets the terminal", style=color(shell_color, pallate))
        print("version - shows the version of the program", style=color(shell_color, pallate))
        print("license [full] [lcN] - shows the license of the program", style=color(shell_color, pallate))
        print("author [0] [1] - shows the author of the program", style=color(shell_color, pallate))
        print("platform - shows the platform of the program", style=color(shell_color, pallate))
        print("Cython - shows the Cython version of the program", style=color(shell_color, pallate))
        print("netshell [e] [i] - opens the netshell", style=color(shell_color, pallate))
        print("tx <path> - opens the tx text editor", style=color(shell_color, pallate))
        print("sudo - opens the sudo terminal", style=color(shell_color, pallate))
        print("cdir <payh> - changes the current directory", style=color(shell_color, pallate))
        print("color <color> <pallate> - changes the color of the terminal", style=color(shell_color, pallate))
        print("you can put 'help' followed by a command to get help on that command", style=color(shell_color, pallate))
        stats = "success"
        
        logging.info(f'help command is finished in file {__file__}')
        
        return stats
    
    def ip_help(shell_color: str = 'secondary', pallate: int = 0, args: str = None):
        print("ip - shows the ip of the computer", style=color(shell_color, pallate))
    
    def cdir_help(shell_color: str = 'secondary', pallate: int = 0, args: str = None):
        print("Type 'cdir' along with a path to direct the terminal to...\nIf you wish to use default paths you can do comands like 'cdir apps' or if you wmat to specify a path do 'cdir C:/etc..'", style=color(shell_color, pallate))
        
    def color_help(shell_color: str = 'secondary', pallate: int = 0, args: str = None):
        print("Type 'color' along with a color and a pallate to change the color of the terminal.\nExamples: 'color main 0' or 'color red 1' the pallate has 1 and 0 the values of wich can be found in the config file", style=color(shell_color, pallate))
        
    def exit_help(shell_color: str = 'secondary', pallate: int = 0, args: str = None):
        print("Type 'exit' to exit the program.\nYou can put extra args such as 'exit 2' wich will exit the program in 2 seoncds or do 'exit i' wich will instantly exit", style=color(shell_color, pallate))
        
    def tx_help(shell_color: str = 'secondary', pallate: int = 0, args: str = None):
        print("Type 'tx' along with which mode to open in, there are 2 modes -o (for opening a file) and -n (to create a new file)\nTo use -o you have to follow it with a path or filename, by default it goes to data/docs, you can also add a -t argument in the end to change the theme.\n-n will just work.\nExamples: tx -o file.txt, tx -n", style=color(shell_color, pallate))
    
    def sudo_help(shell_color: str = 'secondary', pallate: int = 0, args: str = None):
        print("Type 'sudo' to open the sudo terminal", style=color(shell_color, pallate))
    
    