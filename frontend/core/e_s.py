MAX_CASCADES = 600
MAX_COLS = 20
FRAME_DELAY = 0.03

MAX_SPEED  = 5

import os
import shutil, sys, time
import threading # doit()
from random import choice, randrange, paretovariate # Colors

CSI = "\x1b[" # Control Sequence Introducer
pr = lambda command: print("\x1b[", command, sep="", end="")
getchars = lambda start, end: [chr(i) for i in range(start, end)]

do_once = False
l = 0

black, green, white = "30", "32", "37"

latin = getchars(0x30, 0x80)
greek = getchars(0x390, 0x3d0)
hebrew = getchars(0x5d0, 0x5eb)
cyrillic = getchars(0x400, 0x50)

chars= latin + greek + hebrew + cyrillic

class MyThread():
  
    def pareto(limit):
        scale = lines // 2
        number = (paretovariate(1.16) - 1) * scale
        return max(0, limit - number)

    def init():
        global cols, lines
        cols, lines = shutil.get_terminal_size()
        pr("?25l")  # Hides cursor
        pr("s")  # Saves cursor position

    def end():
        pr("m")   # reset attributes
        pr("2J")  # clear screen
        pr("u")  # Restores cursor position
        pr("?25h")  # Show cursor

    def print_at(char, x, y, color="", bright="0"):
        pr("%d;%df" % (y, x))
        pr(bright + ";" + color + "m")
        print(char, end="", flush=True)
        text_in_the_middle()

    def update_line(speed, counter, line):
        counter += 1
        if counter >= speed:
            line += 1
            counter = 0
        return counter, line

    def cascade(col):
        print = console.Console().print
        global l
        speed = randrange(1, MAX_SPEED)
        espeed = randrange(1, MAX_SPEED)
        line = counter = ecounter = 0
        oldline = eline = -1
        erasing = False
        bright = "1"
        limit = MyThread.pareto(lines)
        
        while True:
            counter, line = MyThread.update_line(speed , counter, line)
            if randrange(10 * speed) < 1:
                bright = "0"
            if line > 1 and line <= limit and oldline != line:
                MyThread.print_at(choice(chars),col, line-1, green, bright)
            if line < limit:
                MyThread.print_at(choice(chars),col, line, white, "1")
            if erasing:
                ecounter, eline = MyThread.update_line(espeed, ecounter, eline)
                MyThread.print_at(" ",col, eline, black)
                if l == 100000:
                    print("[red]Codes are correct, will launch to the next step", justify="center")
                    time.sleep(5)
                    raise ValueError('Used to break the program to exit cleanly and not cause BSOD')
                l += 1
            else:
                erasing = randrange(line + 1) > (lines / 2)
                eline = 0
            yield None
            oldline = line
            if eline >= limit:
                MyThread.print_at(" ", col, oldline, black)
                break
                
        

    def main():
        cascading = set()
        added_new = True
        while True:
            while MyThread.add_new(cascading): pass
            stopped = MyThread.iterate(cascading)
            sys.stdout.flush()
            cascading.difference_update(stopped)
            time.sleep(FRAME_DELAY)
            
        
    def add_new(cascading):
        if randrange(MAX_CASCADES + 1) > len(cascading):
            col = randrange(cols)
            for i in range(randrange(MAX_COLS)):
                cascading.add(MyThread.cascade((col + i) % cols))
            return True
        return False

    def iterate(cascading):
        stopped = set()
        for c in cascading:
            try:
                next(c)
            except StopIteration:
                stopped.add(c)
        return stopped

    def run():
        try:
            MyThread.init()
            MyThread.main()
            
        except ValueError:
            
            pass
        finally:
            MyThread.end()

import os, platform
from rich import console


def random_delay():
    delay = randrange(1, 5)
    time.sleep(delay)
    
    

def text_in_the_middle():
    global do_once
    if do_once == False:
        do_once = True
        print = console.Console().print
        size = os.get_terminal_size() # get the size of the terminal
        size = str(size)
        lines = list(size.split('lines'))[1] # get the number of rows
        lines = str(lines[1:3])
        lines = int(lines) # convert to int
        lines = round(lines / 4 -2)        
        colors = 'red'
        for i in range(6):
            os.system('cls' if platform.system() == 'Windows' else 'clear')
            
            for z in range(lines):
                print('\n')
            
            if i % 2 == 0:
                colors = 'red'
            else:
                colors = 'black'
            
            print("""
  ██████╗ ██████╗ ██████╗ ███████╗███████╗     █████╗  ██████╗████████╗██╗██╗   ██╗███████╗
 ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝    ██╔══██╗██╔════╝╚══██╔══╝██║██║   ██║██╔════╝
██║     ██║   ██║██║  ██║█████╗  ███████╗    ███████║██║        ██║   ██║██║   ██║█████╗  
██║     ██║   ██║██║  ██║██╔══╝  ╚════██║    ██╔══██║██║        ██║   ██║╚██╗ ██╔╝██╔══╝  
 ╚██████╗╚██████╔╝██████╔╝███████╗███████║    ██║  ██║╚██████╗   ██║   ██║ ╚████╔╝ ███████╗
  ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚══════╝    ╚═╝  ╚═╝ ╚═════╝   ╚═╝   ╚═╝  ╚═══╝  ╚══════╝""",style= colors, justify = "center")
            time.sleep (1)
    

MyThread.run()