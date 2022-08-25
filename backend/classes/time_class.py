box_1: str
box_2: str
box_3: str 
box_4: str
box_5 = """ 

------------------------------------------------------- M O D U L E -----------------------------------------------------
|                                                                                                                       |    
|  summary: this module is used to help with basic operations in a very modular way with even a modifiable config file  |
|                                                                                                                       |    
------------------------------------------------------- M O D U L E -----------------------------------------------------

.........................................................................................................................................................................
- Name of the module: TimeFunctions
- Author: Dhruvan Kartik
- Date: 20/08/2022
- Time: 03:45 AM
- Version: 1.0
- Notes: None
.........................................................................................................................................................................


-------------------------------------------------------------- N O T E S ------------------------------------------------------------------------------------------------
|                                                                                                                                                                       |    
| # DO NOT MODIFY ANYTHING BELOW THIS BOX #            # IF YOU DO, CODE WILL BREAK AND CAUSE SYSTEM INSTABILITY #          # DO NOT MODIFY ANYTHING BELOW THIS BOX #   |
|                                                                                                                                                                       |    
---------------------------------------------------------- N O T E S   E N D --------------------------------------------------------------------------------------------                                                   """



import logging, time, glob, os, platform #importing the modules
from rich import console

"-------------------------------- E D I T   T H I S   I F   I N   Y O U R   P R O J E C T   D I R --------------------------------"
in_root_dir = False # set the in_root_dir variable to True if the current directory is the root directory of the project          |
"---------------------------------------------------------------------------------------------------------------------------------"

if __name__ == "__main__": # this is the main function that is run when the program is run directly
    if in_root_dir is True: # if in_root_dir is True then run the program from the root directory
        from backend.classes.file_class import file_opperations # import the file_opperations class from the file_class module
        logging.disable(logging.CRITICAL) # disable the logging for this module
    else: # if not in root dir then import the file_operations class from the backend folder
        from file_class import file_opperations # this is the file_operations class from the backend folder
        logging.disable(logging.CRITICAL) # disable the logging for this module
else: # if the module is imported then disable the logging
    from backend.classes.file_class import file_opperations # import the file_opperations class from the backend module


start: float # this is a function that returns the start time in seconds
current: float # this is a function that returns the current time in seconds
end: float # this is a function that returns the end time in seconds
runtime_path: str # this variable is used to store the latest file name and dir
osType: int = platform.system() # get the os type
clearcmd: str = "cls" if platform.system() == "Windows" else "clear" # clear command for windows and linux and mac
latest_file: str = None # this is the variable that will hold the latest file in the runtime directory
set_file_name = False # set the set_file_name variable to True
filecrated = False # set the filecrated variable to False
blob: bytes = b'a\x00\x00\x00d\x00\x00\x00m\x00\x00\x00i\x00\x00\x00n\x00\x00\x00' # this is a blob of bytes
color = console.Console() # console object

def FRFiP(path): # this is a function that returns the file name and dir of the latest file in the runtime directory
    global box_2 # this is the global variable that will hold the latest file in the runtime directory
    
    box_2 = """
    
    ------------------------------------------ F R F i P ------------------------------------------
    |                                                                                             |
    | summary: this function is used to find the last modifed file in the given runtime directory |
    |                                                                                             |
    | - Input: path - the path to the runtime directory                                           |
    | - Output: the last modified file in the runtime directory                                   |
    | - Exceptions: None                                                                          |
    | - Notes: None                                                                               |
    |                                                                                             |
    --------------------------------------- F U N C T I O N ---------------------------------------
    
    """
    
    global latest_file # this is the global variable that will hold the latest file in the runtime directory
    #check if there is anything in the latest_file variable
    if latest_file == None: # if there is nothing in the latest_file variable then
        try: # try to find the latest file in the runtime directory
            list_of_files = glob.glob(path) # * means all if need specific format then *.csv
            latest_file = max(list_of_files, key=os.path.getctime) # get the latest file from the list of files
            return latest_file # return the latest file
        except Exception as e: # if there is an error then
            logging.error(f'FRFiP function is throwing an error in file {__file__} error is : {e}') # logging is a function that logs messages to the console
            return path # return the path
    else: # if there is something in the latest_file variable then
        latest_file = path # set the latest_file variable to the path
        return path # return the path

FRFiP('frontend/data/*') # call the FRFiP function and pass the path to the runtime directory

class op: # opperations is a class
    global box_3 # this is the global variable that will hold the latest file in the runtime directory
    
    box_3 = """
    
    ------------------------------------------ O P A R A T I O N S ------------------------------------------
    |                                                                                                       |
    | summary: this is a class that contains all the functions that are used to read and write to the file  |
    |                                                                                                       |
    | -  W_S = Write Start Time                                                                             |
    | -  W_E = Write End Time                                                                               |
    | -  WR_C = Return the Current Time and Write it                                                        |
    | -  R_S = Read Start Time                                                                              |
    | -  R_E = Read End Time                                                                                |
    | -  E_S = Calulate the Diffrence Between Stored Start and End Times                                    |
    | -  C_S = Calulate the Diffrence Between The Current and Start Time                                    |
    |                                                                                                       |
    ----------------------------------------------- C L A S S -----------------------------------------------
    
    """
    
    def W_S(start_text): # write the start time to the file
        logging.info(f'W_S function is called in file {__file__}') # write the start time to the file
        global start, runtime_path # start is set to the start time
        path = FRFiP(runtime_path) # path is set to the path of the file
        with open(path, 'a') as f: # open the file in append mode
            logging.info(f'file {runtime_path} is opened') # open the file in append mode
            start = time.time() # start time is set to current time
            f.write(f'[S] {start_text} {start} \n') # write the start time to the file 
            f.close() # close the file
            logging.info(f'file {runtime_path} is closed') # return the start time
        logging.info(f'W_S function is finished in file {__file__}') # return the start time
        return start # return the start time
    
    def W_E(end_text): # write the end time to the file
        logging.info(f'W_E function is called in file {__file__}') # write the end time to the file
        global end, runtime_path # end is set to the end time
        path = FRFiP(runtime_path) # path is set to the path of the file
        with open(path, 'a') as f: # open the file in append mode
            logging.info(f'file {runtime_path} is opened')
            end = time.time() # end time is set to current time
            f.write(f'[E] {end_text} {end} \n') # write the end time to the file
            f.close() # close the file
            logging.info(f'file {runtime_path} is closed') # return the end time
        logging.info(f'W_E function is finished in file {__file__}') # return the end time
        return end # return the end time
    
    def WR_C(current_text): # write the current time to the file
        logging.info(f'W_C function is called in file {__file__}') # write the current time to the file
        global current, runtime_path # current is set to the current time
        path = FRFiP(runtime_path) # path is set to the path of the file
        with open(path, 'a') as f: # open the file in append mode
            logging.info(f'file {runtime_path} is opened') # open the file in append mode
            current = time.time() # current time is set to current time
            f.write(f'[C] {current_text} {current} \n') # write the current time to the file
            f.close() # close the file
            logging.info(f'file {runtime_path} is closed') # return the current time
        logging.info(f'W_C function is finished in file {__file__}') # return the current time
        return current # return the current time
            

    def R_S(): # read the start time from the file
        logging.info(f'R_S function is called in file {__file__}') # read the start time from the file
        global start # start is set to the start time
        path = FRFiP(runtime_path) # path is set to the path of the file
        if start is None or start == 0 or start == "": # if start is not set then set it to the current time
            with open(path, 'r') as f: # open the file in read mode
                logging.info(f'file {runtime_path} is opened') # open the file in read mode
                start = f.readline()[1] # read the line 2 from the file
                start = start.split(':')[1] # split the line at the :
                start = start.replace(' ', '') # remove the spaces from the string
                start = start.replace(';', '') # remove the spaces and ; from the start time
                start = float(start) # convert the string to float
                f.close() # close the file
                logging.info(f'file {runtime_path} is closed')
        logging.info(f'R_S function is finished in file {__file__}') # return the start time
        return start # return the start time
 
    def R_E(): # read the end time from the file
        logging.info(f'R_E function is called in file {__file__}') # read the end time from the file
        global end # end is set to the end time
        path = FRFiP(runtime_path) # path is set to the path of the file
        if end is None or end == 0 or end == "": # if end is not set then set it to the current time
            with open(path, 'r') as f: # open the file in read mode
                logging.info(f'file {runtime_path} is opened') # open the file in read mode
                end = f.readline()[2] # read the line 3 from the file
                end = end.split(':')[1] # split the line at the :
                end = end.replace(' ', '') # remove the spaces
                end = end.replace(';', '') # remove the spaces and ; from the string
                end = float(end) # convert the string to float
                f.close() # close the file
                logging.info(f'file {runtime_path} is closed') # log close the file
        logging.info(f'R_E function is finished in file {__file__}') # return the end time
        return end # return the end time
    
    def E_S(recent_runtime, raw_Runtime): # end the current time and start the new one
        logging.info(f'E_S function is called in file {__file__}') # raw_Runtime is the raw runtime from the file
        global start, end # start is set to the start time
        path = FRFiP(runtime_path) # path is set to the path of the file
        
        with open(path, 'a+') as f: # open the file in append mode
            logging.info(f'file {runtime_path} is opened') # open the file in append mode
            if start is None or start == 0 or start == "": # if start is not set then set it to the current time
                start = f.readline()[1] # read the start time from the file
                start = start.split(':')[1] # split the string at the colon and take the second element
                start = start.replace(' ', '') # remove all spaces
                start = start.replace(';', '') # remove the spaces and ; from the string
                logging.info(f'start time is set {start}') # start time is set to the start time in the file
                
            if end is None or end == 0 or end == "": # if end time is not set then set it to the current time
                end = f.readline()[2] # read the end time from the file
                end = end.split(':')[1] # split the end time into a list
                end = end.replace(' ', '') # remove the spaces
                end = end.replace(';', '') # end time is set to the end time
                logging.info(f'end time is set {end}') # end time is set to the end time in the file
            
            if type(start) == str: # if the start time is a string
                start = float(start) # convert the start time to a float
                logging.info(f'start time: str has been converted to float') # logging is a function that logs messages to the console
            else: # if start is not a str then it is a float 
                logging.info(f'start time is already float') # if start time is already float then do nothing
                 
            if type(end) == str: # if end is a string
                end = float(end) # end time is converted to float
                logging.info(f'end time: str has been converted to float') # end time is converted to float
            else:
                logging.info(f'end time is already float') # end time is already float
            
            runtime: float = end - start # runtime is the difference between the start and end time
            exact_runtime: float = runtime # exact runtime is set to the runtime
            units = 'seconds' # units is set to seconds
            
            f.write(f'[E - S] {raw_Runtime} {exact_runtime} \n') # write the runtime to the file
            logging.info(f'[E - S] {raw_Runtime} {exact_runtime} has been written to the file') # log the runtime to the file
            
            if runtime < 1: # if runtime less than 1 second then convert to milliseconds
                runtime = runtime * 1000 # convert to milliseconds
                runtime = round(runtime, 3) # roundedtotal is set to the total time run rounded to 3 decimal places
                units = 'ms' # unit is set to 'ms'
                
                logging.info(f'total time run is getting set to {runtime}ms in file {runtime_path}') # logging is a function that logs messages to the console
            else: # if end time is greater than start time, then total is in seconds
                logging.info(f'total time run is getting set to {runtime}seconds in file {runtime_path}') # logging is a function that logs messages to the console
                
                runtime = round(runtime, 3) # round to 3 decimal places
                units = 'seconds' # unit is set to 'seconds'        
            
            f.write(f'[E - S] {recent_runtime} {runtime} {units} (Converted Values... NOT EXACT) \n') # write the total time run to the file
            logging.info(f'[E - S] {recent_runtime} {runtime} {units} (Converted Values... NOT EXACT) has been written to the file') # logging is a function that logs messages to the console
            
            f.close() # close the file
            logging.info(f'file {runtime_path} is closed') # close the file
        
        logging.info(f'E_S function is finished in file {__file__}') # logging is a function that logs messages to the console
        return runtime, units, exact_runtime # return the total time run and the units of time run
    
    def C_S(recent_runtime, raw_Runtime): # write the current time to the file
        logging.info(f'C_S function is called in file {__file__}') # logging is a function that logs messages to the console
        global start, current # set the start and current time to the global variables
        current = time.time() # set the current time to the current time
        path = FRFiP(runtime_path) # get the path to the file
        with open(path, 'a+') as f: # open the file in append+ mode
            logging.info(f'file {runtime_path} is opened') # log open the file
            if start is None or start == 0 or start == "": # if start time is not set, then set it to the current time
                start = f.readline()[1] # read the start time from the file from the second line
                start = start.split(':')[1] # split the start time from the file and get the second value
                start = start.replace(' ', '') # remove spaces
                start = start.replace(';', '') # remove the semi-colons      
            
            if current is None or current == 0 or current == "": # if current is None or current == 0 or current == "":
                current = f.readline()[2] # read the current time from the file from the third line
                current = current.split(':')[1] # split the current time from the file and get the second value
                current = current.replace(' ', '') # remove spaces
                current = current.replace(';', '') # remove semi-colons                 
             
            if type(start) == str: # if start time is a string then convert to float
                start = float(start) # convert start time to float
            else: # if end time is greater than start time, then total is in seconds
                logging.info(f'start time is already float') # logging is a function that logs messages to the console
                
            if type(current) == str: # if current time is a string then convert to float
                current = float(current) # convert current time to float
            else: # if end time is greater than start time, then total is in seconds
                logging.info(f'current time is already float') # logging is a function that logs messages to the console
            
            runtime: float = current - start # get the total time run
            exact_runtime: float = runtime # exact runtime is set to the runtime
            units = 'seconds' # unit is set to 'seconds'
            
            f.write(f'[C - S] {raw_Runtime} {exact_runtime} \n') # write the runtime to the file
            logging.info(f'[C - S] {raw_Runtime} {exact_runtime} has been written to the file') # logging is a function that logs messages to the console
            
            if runtime < 1: # if runtime less than 1 second then convert to milliseconds
                runtime = runtime * 1000 # convert to milliseconds
                runtime = round(runtime, 3) # roundedtotal is set to the total time run rounded to 3 decimal places
                units = 'ms' # unit is set to 'ms'
                
                logging.info(f'total time run is getting set to {runtime}ms in file {runtime_path}') # logging is a function that logs messages to the console
            else: # if current time is greater than start time, then total is in seconds
                logging.info(f'total time run is getting set to {runtime}seconds in file {runtime_path}') # logging is a function that logs messages to the console
                
                runtime = round(runtime, 3) # round to 3 decimal places
                units = 'seconds' # unit is set to 'seconds'        
            
            f.write(f'[C - S] {recent_runtime} {runtime} {units} (Converted Values... NOT EXACT) \n') # write the total time run to the file
            logging.info(f'[C - S] {recent_runtime} {runtime} {units} (Converted Values... NOT EXACT) has been written to the file') # logging is a function that logs messages to the console
            
            f.close() # close the file
            logging.info(f'file {runtime_path} is closed') # logging is a function that logs messages to the console
        
        logging.info(f'C_S function is finished in file {__file__}') # logging is a function that logs messages to the console
        return runtime, units, exact_runtime # return the total time run and the units of time run


class main: # main is a class
    global box_4
    box_4 = """
    --------------------------------------------------- T I M E   F U N C T I O N ---------------------------------------------------
    |                                                                                                                               |
    | summary: This class is used to get do a few time realated opperations based on the inputs given to the function __init__      |
    |                                                                                                                               |
    | -  mytime = Used to Convert the State and Position to an equvalvent integer if the given input is a string                    |
    | -  __init__ = Used to initialize the class and variables and also point to the right function to use based on the inputs given|
    | -  Input: State and Position                                                                                                  |
    | -  Output: The converted integer and the units of the integer along with the exact value                                      |
    | -  Notes: None                                                                                                                |
    |                                                                                                                               |
    ----------------------------------------------------------- C L A S S -----------------------------------------------------------
    """
    
    def mytime(orgstate: str, orgposition: str, runtime_path: str): # mytime is a function in the class main
        this_file = __file__ # __file__ is a variable that holds the name of the current file
        
        logging.info(f'mytime function is called in file {this_file}') # logging is a function that logs messages to the console
        logging.info(f'string state given is {state}, string position given is {orgposition}') # logging is a function that logs messages to the console
        
        if orgstate == 'write': # if state is write, then write to the file
            if orgposition == 'start': # if the position is start, then write the start time to the file
                state, position = 1, 0 # state is set to 1 and position is set to 0
                logging.info(f'state and position are set to {state}, {position}') # logging is a function that logs messages to the console
        
        elif orgstate == 'write': # if state is write
            if orgposition == 'end': # if the position is end, then set the state and position to 2 and 1 respectively
                state, position = 1, 1 # state is set to 1 and position is set to 1
                logging.info(f'state and position are set to {state}, {position}') # logging is a function that logs messages to the console
        
        elif orgstate == 'readWrite': # if state is readWrite then set state to read and position to 0
            if orgposition == 'current': # if the state is readWrite and the position is current, then set the state and position to 2 and 0 respectively
                state, position = 1, 2 # state and position are set to 1 and 2
                logging.info(f'state and position are set to {state}, {position}') # logging is a function that logs messages to the console
        
        if orgstate == 'read': # if state is read
            if orgposition == 'start': # if the state is read and the position is start, then set the state and position to 0
                state, position = 0, 0 # state and position are set to 0
                logging.info(f'state and position are set to {state}, {position}') # logging is a function that logs messages to the console
        
        
        elif orgstate == 'read': # if state is read
            if orgposition == 'end': # if the state is read and the position is end, then set the state and position to 0 and 1 respectively
                state, position = 0, 1 # set the state and position to 0 and 1
                logging.info(f'state and position are set to {state}, {position}') # logging is a function that logs messages to the console
        
        elif orgstate == 'read': # if state is read and position is current
            if orgposition == 'fixed': # if the position is fixed, then the state is set to 0 and the position is set to 2
                state, position = 0, 2 # state is set to 0, position is set to 2
                logging.info(f'state and position are set to {state}, {position}') # logging is a function that logs messages to the console
        
        elif orgstate == 'read': # if state is read, then position is fixed
            if orgposition == 'current': # if the position is current, then the state is read and the position is current
                state, position = 0, 3 # state and position are set to 0, 3
                logging.info(f'state and position are set to {state}, {position}') # logging is a function that logs messages to the console
        
        else: # if state is not read, then position is fixed
            logging.error(f'mytime function FAILED with error this file is {this_file}') # logging is a function that logs messages to the console
            print(f'Error with state: {orgstate}, position: {orgposition}') # print the error message
            state, position = None, None # state and position are set to None
            main.time_read_write(state, position, runtime_path) # call the time_read_write function

        main.time_read_write(state, position, runtime_path) # call the time_read_write function
    
    def innit(state = None, position = None, input_path_save: str = None, config_path: str = None): # __innit__ is a function that initializes the class
        global runtime_path, set_file_name, filecrated # runtime_path is a global variable that holds the path to the file that will be used to save the runtime
        
        if state == None and position == None:
            return '0x404' # return 0x404 if state and position are None
        
        if type(state) == str: # if state is a string
            state, position, runtime_path = main.mytime(state, position, runtime_path) # main.mytime is a function that sets the state and position of the time funciton
         
        logging.warning(f'__innit__ is starting in file {__file__}') # logging is a function that logs messages to the console
        
        if config_path is None: # if config_path is None then set config_path to the default config_path
            config_path = 'config\\config.json' # config_path is set to the path of the config file
        
        program_start_text, program_end_text, program_current_text, recent_runtime, raw_Runtime, date_format, runtime_file_path, ignore, max_files, make_runtime_files = file_opperations.read_runtime_config(config_path) # read_runtime_config is a function that reads the runtime config file
        
        if make_runtime_files is False: # if make_runtime_files is false then do not make runtime files 
            max_files = 0 # if make_runtime_files is false, then set max_files to 0
        
        
        if input_path_save != None: # if input_path_save is not None then set the runtime_path to the input_path_save
            runtime_file_path = input_path_save # set the runtime_file_path to the input_path_save
        
        if set_file_name is False: # if set_file_name is false then set the file name to the current date and time
            runtime_path = runtime_file_path # set the runtime_path to the runtime_file_path
            set_file_name = True # set the set_file_name to True

        if runtime_path is None: # if runtime_path is None then set the runtime_path to the runtime_file_path
            print('runtime_path is None') # print is a function that prints messages to the console
            print('please use a runtime_path') # print a message to the console
            print('will be using default runtime_path "./runtime.s"') # logging is a function that logs messages to the console
            runtime_path = 'DEFAULT_runtime.s' # default runtime_path is set to './runtime.s'
         
        #if __name__ == '__main__': # if the file is being run directly then run the following code
            #print(f"everything = {program_start_text}, {program_end_text}, {recent_runtime}, {raw_Runtime}, {date_format}, {runtime_file_path}, {ignore}, {max_files}, {make_runtime_files}") # print the values of the variables
            
        if filecrated is False: # if filecrated is false then create the file
            try: # try to open the file
                with open(runtime_path, 'w') as f: # open is a function that creates the file
                    f.write('--------------- THIS IS THE RUNTIME STATISTICS FILE (DO NOT EDIT) ---------------\n') # write to the file
                    filecrated = True # filecrated is set to true
                    
            except FileNotFoundError as e: # if the file is not found then print the error
                logging.error(f'FileDirNotFoundError with file {runtime_path} with error : {e}') # logging is a function that logs messages to the console
        
        output = 404 # output is set to 404
        
        if state == 1 and position == 0: # if state is 1 and position is 0, then write to the start of the file
            output = op.W_S(program_start_text) # W_S is a function that writes the program start text to the file
            
        elif state == 1 and position == 1: # if state is 1 and position is 1, then write the end time to the file
            output = op.W_E(program_end_text) # output is a variable that holds the output of the function
            
        elif state == 1 and position == 2: # state is 10 and position is 2
            output = op.WR_C(program_current_text) # WR_C is a function that writes and outputs the current time
        
        elif state == 0 and position == 0: # if state is 0 and position is 0, then write the start time to the file
            output = op.R_S() # read start
        
        elif state == 0 and position == 1: # if state is 0 and position is 1, then write the end time to the file
            output = op.R_E() # read end
            
        elif state == 0 and position == 2: # if state is 0 and position is 2, then write the current time to the file
            output = op.E_S(recent_runtime, raw_Runtime) # write the total time run to the file
            
        elif state == 0 and position == 3: # if state is 0 and position is 3, then write the current time to the file
            output = op.C_S(recent_runtime, raw_Runtime) # C_S is a function that writes the current runtime to the file
        
        return output # return the output
        
            
def runtests(password = None): # runtests is a function
    global blob, box_1, box_2, box_3, box_4, box_5, clearcmd, color
    os.system(clearcmd) # clear the screen
    
    divider = '|'  # divider is a variable that holds the divider
    space = ' ' # space is a variable that holds a space
    
    if password == blob.decode('utf-32le'): # if the password is admin

        logging.warning(f'runtests function is starting in file {__file__}') # logging is a function that logs messages to the console
        
        print("[WARNING] - testing mode active") # print to console that testing mode is active
        time.sleep(1) # sleep for 1 second
        color.print(f'[bold]{box_5} \n{box_2} \n{box_3} \n{box_4} \n', style= "green") # print the box_1 variable
        time.sleep(4) # sleep for 2 second
        os.system(clearcmd) # clear the screen
        
        tf = main.innit # create a variable that is equal to the time_read_write function
        
        one = tf(1, 0) # one is a variable that is equal to the output of the tf function
        two = tf(1, 1) # two is a variable that is equal to the output of the tf function
        three = tf(1, 2) # three is a variable that is equal to the output of the tf function
        four = tf(0, 0) # four is a variable that is equal to the output of the tf function
        five = tf(0, 1) # five is a variable that is equal to the output of the tf function
        six = tf(0, 2) # six is a variable that is equal to the output of the tf function
        seven = tf(0, 3) # seven is a variable that is equal to the output of the tf function
        
        box_1 = f"""
    ------------------------------------------------------------------ R U N   T E S T S ----------------------------------------------------------------
    |                                                                                                                                                   |
    | summary: this function is used to run the tests for the main module if the password is correct or is being directly run                           |
    |                                                                                                                                                   |
    | - Inputs: password - the password that is used to run the tests                                                                                   |
    | - Outputs: None                                                                                                                                   |
    |                                                                                                                                                   |
    |   Given inputs:                    Expected Outputs:                           Write to file:            Outputs:                                 |
    |                                                                                                                                                   |
    |   State = 1 | Position = 0         Output = (Start time)                       True                      {one}{space * (41 - len(str(one)))}|
    |   State = 1 | Position = 1         Output = (End time)                         True                      {two}{space * (41 - len(str(two)))}|
    |   State = 1 | Position = 2         Output = (Current time)                     True                      {three}{space * (41 - len(str(three)))}|
    |   State = 0 | Position = 0         Output = (Start time)                       False                     {four}{space * (41 - len(str(four)))}|
    |   State = 0 | Position = 1         Output = (End time)                         False                     {five}{space * (41 - len(str(five)))}|
    |   State = 0 | Position = 2         Output = (Total time [End - Start])         False                     {six}{space * (41 - len(str(six)))}|
    |   State = 0 | Position = 3         Output = (Total time [Current - Start])     False                     {seven}{space * (41 - len(str(seven)))}|
    |                                                                                                                                                   |
    ------------------------------------------------------------------- F U N C T I O N -----------------------------------------------------------------
    """ 
        os.system(clearcmd) # clear the screen
        color.print(f"[bold]{box_1}", style='red') # print the box_1 variable
    
    
    else:
        print("testing mode not active") # print to console that testing mode is not active
        print("password is incorrect") # print to console that the password is incorrect
    
           
if __name__ == '__main__': # if this is the main file, then run the following code
    if in_root_dir is False:
        print("testing mode active") # print to console that testing mode is active
        runtests('admin') # run the runtests function with the password 'admin'
    else:
        FRFiP("frontend/data/*") # run the FRFiP function with the path "frontend/data/"