# ------------------------- I M P O R T S ---------------------------#
import os, platform, time, logging #                                 |
from rich import console #                                           |
# -------------------------------------------------------------------|
from frontend.core.help_sh import Help_Functions__Base as HFSh #     |
from frontend.core.exit_sh import exit_sh as ExitSh #                |
from frontend.core.color_sh import color_sh as ColorSh #             |
from frontend.core.cdir_sh import cdir_sh as CdirSh #                |
from frontend.core.netshell_sh import netshell_sh as NshellSh #      |
from frontend.core.sudo_sh import sudo_sh as SudoSh #                |
from frontend.core.tx_sh import tx_sh as TxSh #                      |
from frontend.core.e_s import MyThread as e_s #                      |
# -------------------------------------------------------------------|
#                                                                    |
from backend.classes.file_class import file_opperations, JSON_read # |
# ------------------------- I M P O R T S ---------------------------#

def args_sorter(shell_color: str = 'secondary', pallate: int = 0, args_arr: str = None):
    color = JSON_read.read_color_hex # read the color hex from the config file
    print = console.Console().print # print function
    cleard: str = "cls" if platform.system() == "Windows" else "clear" # clear command for windows and linux and mac
    out = 'reset'
    
    if args_arr[0] == 'help':
        if args_arr[1] == 'ip':
            HFSh.ip_help(shell_color, pallate)
            out = 'success'
        elif args_arr[1] == 'cdir':
            HFSh.cdir_help(shell_color, pallate)
            out = 'success'
        elif args_arr[1] == 'exit':
            HFSh.exit_help(shell_color, pallate)
            out = 'success'
        elif args_arr[1] == 'color':
            HFSh.color_help(shell_color, pallate)
            out = 'success'
        elif args_arr[1] == 'tx':
            HFSh.tx_help(shell_color, pallate)
            out = 'success'
    
    if args_arr[0] == 'exit':
        if args_arr[1] == 'i' or args_arr[1] == 'I':
            ExitSh(shell_color, pallate, args_arr[1])
        elif int(args_arr[1]) > 0:
            val = int(args_arr[1])
            ExitSh(shell_color, pallate, val)
    
    if args_arr[0] == 'tx':
        if args_arr[-1] == '-o':
            print("-o should have a valid file path", style = color('main', 0))
            return 'reset'
        if args_arr[-1] == '-n':
            out = TxSh(shell_color, pallate, args_arr)
            return out
            
        out = TxSh(shell_color, pallate, args_arr)
    
    return out



def sort_and_cleaner(shell_color: str = 'secondary', pallate: int = 0, userinput: str = None):
    st_out = None
    color = JSON_read.read_color_hex # read the color hex from the config file
    print = console.Console().print # print function
    cleard: str = "cls" if platform.system() == "Windows" else "clear" # clear command for windows and linux and mac
    
    args_arr = list(userinput.split(" "))
    if len(args_arr) > 1:
        st_out = args_sorter(shell_color, pallate, args_arr)
    
    if st_out == 'success':
        out1 = 'dont clear'
        return out1
    
    if st_out == 'reset':
        out1 = 'dont clear'
        print("\nHelp command not found, try again with valid [args]\n", style = color('main', 0))
        return out1
    
    if userinput == 'exit':
        ExitSh('main', pallate)
    
    elif userinput == 'help':
        out = HFSh.help(shell_color, pallate)
        if out == 'success':
            out = 'reset'
            print(" ", style=color(shell_color, pallate))
            out1 = 'dont clear'
            return out1
        else:
            print("execption has ocured in help command", style=color('main', 0))
    else:
        print("\nCommand not found, try again.\n", style = color('main', 0))
    
    out1 = 'dont clear'
    return out1



