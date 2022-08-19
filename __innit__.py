import logging
import os
import time
import json
import sys
import threading

from rich import console
from backend.classes.file_class import file_opperations, JSON_read
from backend.classes.time_class import timefunc
import backend.classes.time_class as ta

ti = timefunc.__innit__
z = console.Console()
this_file = os.path.basename(__file__)
conf_path: str = 'config/config.json'
color = JSON_read.read_color_hex
runtime_path = f"frontend/data/{time.strftime('%d-%m-%Y %H-%M-%S',time.localtime(time.time()))}.s"


class __innit__:
    def _innit_():
        os.system('clear')
        try:
            logging_status, logging_path, logging_level, logging_format, logging_datefmt, logging_maxFiles =  z.print("config file is missing information, please reinitialize config.json", style="red") if JSON_read.read_log_config(conf_path) is None else JSON_read.read_log_config(conf_path)
            logging.basicConfig(level=logging.NOTSET,filename=logging_path, filemode='w', format=logging_format, datefmt=logging_datefmt) # set up logging

        except Exception as e:
            z.print(f'Error reading config file: {e}', style='red')
            exit()
        
        if logging_status is True:
            logging.warning(f'_innit_ function is starting in file {this_file}') # log start
            logging.info(f"sucessfully loaded the logging config file with values:\n'Logging Status': {logging_status} \n'Logging Path': '{logging_path}' \n'Logging Level': '{logging_level}' \n'Logging Date Format': '{logging_datefmt}' \n'Max Number of Log Files Allowed': {logging_maxFiles}\n") # log start
            ta.runtests('admin')
            ti(1, 0, runtime_path)
        else:
            logging.critical('Logging is disabled in config file')
            logging.disable(logging.CRITICAL)
            ti(1, 0, runtime_path)
            os.system('clear')
            z.print('WARNING Logging is disabled in config file', style = color('main', 0))
            time.sleep(3)
            os.system('clear')

        
        logging.warning(f'_innit_ function is finished in file {this_file}') # log finish
        __innit__._main_()
        
        
    def _main_():
        try:
            logging_maxFiles =  z.print("config file is missing information, please reinitialize config.json", style="red") if JSON_read.read_log_config(conf_path)[5] is None else JSON_read.read_log_config(conf_path)[5]
        except Exception as e:
            logging.error(f'_main_ function FAILED reading config file with error: {e}')
            z.print(f'Error reading config file: {e}', style='red')
            exit()
        
        logging.warning(f'_main_ function is starting in file {this_file}') # log start
        
        current_time = time.time() # Get current time
        current_time_date = time.strftime('It is currently the %d of %b in %Y, the time is %I %p, %M minutes and %S seconds',time.localtime(current_time)) # %Y-%m-%d-%H-%M-%S
        

        z.print(current_time_date, style = color('main', 0)) # print current time
        
        if len(file_opperations.count_log_files('logs')) >= logging_maxFiles: # if number of files in ./logs is greater than 10
            
            logging.info(f"Number of log files in ./logs is {len(file_opperations.count_log_files('logs'))} before deletion") # log number of files ./logs
            
            while len(file_opperations.count_log_files('logs')) > logging_maxFiles:
                oldest_file = min(file_opperations.count_log_files('logs'), key=os.path.getctime) # get oldest file in ./logs
                os.remove(oldest_file) # remove oldest file in ./logs
                logging.info(f"Removed log file {oldest_file} in ./logs") # log number of files ./logs
            
            logging.info(f"Number of log files in ./logs is {len(file_opperations.count_log_files('logs'))} after deletion") # log number of files ./logs
            
        
        ti(1, 1, runtime_path)
        
        z.print(f"Time to run this file: {ti(0, 2, runtime_path)[0]} {ti(0, 2, runtime_path)[1]}", style = color('secondary', 0)) # print time to run this file
                
                
                
                
                
        logging.warning(f'_main_ function is finished in file {this_file}') # log finish
        
        
if __name__ == "__main__":
    __innit__._innit_()