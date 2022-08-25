#import backend.functions.TimeFunctions as ogtf
import logging, os, time, platform, random, sys, threading; from backend.functions.TimeFunctions import main as tf; from rich import console; from backend.classes.file_class import file_opperations, JSON_read; from rich.progress import track; from frontend.client.base_shell import CMDInterface as cli

#include <stdio.h>

osType: int = platform.system() # get the os type
clearcmd: str = "cls" if platform.system() == "Windows" else "clear" # clear command for windows and linux and mac
bootloader_speed = 0.1 # bootloader speed in seconds
ti = tf.innit # innit the time functions
z = console.Console() # console object
this_file = os.path.basename(__file__) # get the name of the current file
conf_path: str = 'config/config.json' # path to the config file
color = JSON_read.read_color_hex # read the color hex from the config file
runtime_path = f"frontend/data/{time.strftime('%d-%m-%Y %H-%M-%S',time.localtime(time.time()))}.s" # runtime path
ver = "0.8" # version

skipbootloader = True # skip the bootloader ------------------------------------------------------------------------ C H A N G E   T H I S -------------------------------------------------------------

class __innit__:
    
    def _innit_():
        global bootloader_speed
        
        speed = bootloader_speed;
        
        os.system(clearcmd)
        try:
            logging_status, logging_path, logging_level, logging_format, logging_datefmt, logging_maxFiles =  z.print("config file is missing information, please reinitialize config.json", style="red") if JSON_read.read_log_config(conf_path) is None else JSON_read.read_log_config(conf_path)
            logging.basicConfig(level=logging.NOTSET,filename=logging_path, filemode='w', format=logging_format, datefmt=logging_datefmt) # set up logging

        except Exception:
            z.print(f'Error reading config file', style='red')
            exit()
        
        if logging_status is True:
            logging.warning(f'_innit_ function is starting in file {this_file}') # log start
            logging.info(f"sucessfully loaded the logging config file with values:\n'Logging Status': {logging_status} \n'Logging Path': '{logging_path}' \n'Logging Level': '{logging_level}' \n'Logging Date Format': '{logging_datefmt}' \n'Max Number of Log Files Allowed': {logging_maxFiles}\n") # log start
            ti(1, 0, runtime_path)
            
        else:
            logging.critical('Logging is disabled in config file')
            logging.disable(logging.CRITICAL)
            ti(1, 0, runtime_path)
            os.system(clearcmd)
            z.print('WARNING Logging is disabled in config file', style = color('main', 0))
            time.sleep(3)
            os.system(clearcmd)

        
        logging.warning(f'_innit_ function is finished in file {this_file}') # log finish
        __innit__.bootloader(speed)
        __innit__._main_()
        
    
    def bootloader(speed):
        if skipbootloader is True:
            return
        
        global conf_path, ver
        os.system(clearcmd)
        z.print(f"OMEGA BOOTLOADER", style = color('tertiary', 0))
        logging.debug(f'bootloader function is starting in file {this_file}') # log start
        time.sleep(0.8)
        z.print(f"- Version {ver}", style = color('main', 0))
        time.sleep(0.1)
        z.print(f"- Date: {time.strftime('%d-%m-%Y',time.localtime(time.time()))}", style = color('main', 0))
        time.sleep(0.1)
        z.print(f"- Time: {time.strftime('%H:%M:%S',time.localtime(time.time()))}", style = color('main', 0))
        time.sleep(0.1)
        z.print(f"- Logging: {JSON_read.read_log_config(conf_path)[0]}", style = color('main', 0))
        time.sleep(2)
        os.system(clearcmd)
        z.print(f"- Beginning bootloader initalization...", style = color('secondary', 0))
        time.sleep(0.1)
        z.print("[blink]Initializing...", style = color('main', 0))
        time.sleep(random.randint(1,5))
        os.system(clearcmd)
        for i in track(range(random.randint(15, 38)), description = "[red][bold]Loading Shell..", style = color('gray', 1)):
            time.sleep(speed)  # Simulate work being done
        logging.debug(f'bootloader function is finished in file {this_file}') # log finish
    
    def _main_():
        try:
            logging_maxFiles =  z.print("config file is missing information, please reinitialize config.json", style="red") if JSON_read.read_log_config(conf_path)[5] is None else JSON_read.read_log_config(conf_path)[5]
        except Exception as e:
            logging.error(f'_main_ function FAILED reading config file with error: {e}')
            z.print(f'Error reading config file: {e}', style='red')
            exit()
        
        logging.warning(f'_main_ function is starting in file {this_file}') # log start
        
        current_time = time.time() # Get current time
        current_time_date = time.strftime('It is currently the %d of %b, %Y, the time is %I:%M:%S %p',time.localtime(current_time)) # %Y-%m-%d-%H-%M-%S
        
        if len(file_opperations.count_log_files('logs')) >= logging_maxFiles: # if number of files in ./logs is greater than 10
            
            logging.info(f"Number of log files in ./logs is {len(file_opperations.count_log_files('logs'))} before deletion") # log number of files ./logs
            
            while len(file_opperations.count_log_files('logs')) > logging_maxFiles:
                oldest_file = min(file_opperations.count_log_files('logs'), key=os.path.getctime) # get oldest file in ./logs
                os.remove(oldest_file) # remove oldest file in ./logs
                logging.info(f"Removed log file {oldest_file} in ./logs") # log number of files ./logs
            
            logging.info(f"Number of log files in ./logs is {len(file_opperations.count_log_files('logs'))} after deletion") # log number of files ./logs
            
        
        ti(1, 1, runtime_path)
        
        
        os.system(clearcmd)
        
        z.print(current_time_date, style = color('main', 0)) # print current time
        
        z.print(f"Boot time is: {ti(0, 2, runtime_path)[0]} {ti(0, 2, runtime_path)[1]}", style = color('main', 0)) # print time to run this file
                     
        out = cli.Input_Interface('dont clear') # run cli
                
        logging.warning(f'_main_ function is finished in file {this_file}') # log finish
        

def func2():
    x = random.randint(1,1000)
    for i in range(10000000):
        time.sleep(0.3)
        if x == i:
            z.print("[red][blink]CODES FOR LAUNCH IS 109-283-292, please contact omega if you need help")
            break
    z.print('type launch codes in the terminal')
        
        
__innit__._innit_()

"""if __name__=='__main__':
    Thread1 = threading.Thread(target=__innit__._innit_)
    Thread2 = threading.Thread(target=func2)
    Thread1.start()
    Thread2.start()
    Thread1.join()
    Thread2.join()
    
usa_phone_number = '+1 (555) 555-5555'"""
    
#__innit__._innit_()