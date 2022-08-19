import logging
import time

# -------------------------------------------------------------- N O T E S --------------------------------------------------------------

# state = 0 for read, state = 1 for write
# position = 0 for start, position = 1 for end, position = 2 for end - start, position = 3 for current time - start
        
# ---------------------------------------------------------- N O T E S   E N D ----------------------------------------------------------

class timefunc: # timefunc is a class
    def mytime(orgstate: str, orgposition: str, runtime_path: str):
        this_file = __file__ # __file__ is a variable that holds the name of the current file
        
        if orgstate == 'read':
            if orgposition == 'start':
                state, position = 0, 0
        
        elif orgstate == 'write':
            if orgposition == 'start':
                state, position = 1, 0
        
        elif orgstate == 'read':
            if orgposition == 'end':
                state, position = 0, 1
        
        elif orgstate == 'write':
            if orgposition == 'end':
                state, position = 1, 1
        
        elif orgstate == 'read':
            if orgposition == 'fixed':
                state, position = 0, 2
        
        elif orgstate == 'read':
            if orgposition == 'current':
                state, position = 0, 3
        
        else:
            logging.error(f'mytime function FAILED with error this file is {this_file}')
            print(f'Error with state: {orgstate}, position: {orgposition}')
            state, position = None, None
            timefunc.time_read_write(state, position, runtime_path)

        timefunc.time_read_write(state, position, runtime_path)
    
    
    def time_read_write(state, position, runtime_path = None): # time_read_write is a function

        if runtime_path is None:
            print('runtime_path is None')
            print('please use a runtime_path')
            print('will be using default runtime_path "./runtime.s"')
            runtime_path = 'runtime.s'
            
        if type(state) == str:
            timefunc.mytime(state, position, runtime_path)
        
        this_file = __file__ # __file__ is a variable that holds the name of the current file
        
        logging.info(f'time_read_write function is starting in file {this_file}') # logging is a function that logs messages to the console
        
        start = None # start is a variable that holds the start time
        end = None # end is a variable that holds the end time
                
        if state == 1 and position == 0: # if state is 1 and position is 0
            start = time.time() # start is set to the current time
            logging.info(f'start time is getting set to {start} in file {runtime_path}') # logging is a function that logs messages to the console
            try: # try is a statement that tries to do something
                with open(runtime_path, 'w') as f: # with is a statement that opens a file
                    f.write(f"PG_start_time : {start} \n") # f.write is a function that writes to a file
                    
                    f.close() # f.close is a function that closes a file
                return start # return is a statement that returns a value

            except Exception as e: # except is a statement that handles an exception
                logging.error(f'time_read_write function FAILED to write to {runtime_path} with error: {e}') # logging is a function that logs messages to the console
                return 0 # return is a statement that returns a value

        
        elif state == 1 and position == 1: # if state is 1 and position is 1
            end = time.time() # end is set to the current time
             
            logging.info(f'end time is getting set to {end} in file {runtime_path}') # logging is a function that logs messages to the console
            
            try: # try is a statement that tries to do something
                with open(runtime_path, 'a') as f: # with is a statement that opens a file
                    f.write(f"PG_end_time: {end}") # f.write is a function that writes to a file
                    f.close() # f.close is a function that closes a file
                return end # return is a statement that returns a value
            
            except Exception as e: # except is a statement that handles an exception
                logging.error(f'time_read_write function FAILED to write to {runtime_path} with error: {e}') # logging is a function that logs messages to the console
                return 0 # return is a statement that returns a value
        
        
        elif state == 0 and position == 0: # if state is 0 and position is 0
            logging.info(f'time_read_write function is starting to read from file {runtime_path}') # logging is a function that logs messages to the console
            
            try: # try is a statement that tries to do something
                with open(runtime_path, 'r') as f: # with is a statement that opens a file
                    for line in f: # for is a statement that iterates over a collection
                        if 'PG_start_time' in line: # if PG_start_time is in line
                            start = line.split(':')[1] # start is set to the start time
                        
                            logging.info(f'start time is getting set to {start} in file {runtime_path}') # logging is a function that logs messages to the console
                        
                        return start # return is a statement that returns a value
                            
            except Exception as e: # except is a statement that handles an exception
                logging.error(f'time_read_write function FAILED to read from file {runtime_path} with error: {e}') # logging is a function that logs messages to the console
                return 0 # return is a statement that returns a value
        
         
        elif state == 0 and position == 1: # if state is 0 and position is 1
            logging.info(f'time_read_write function is starting to read from file {runtime_path}') # logging is a function that logs messages to the console
            
            try: # try is a statement that tries to do something
                with open(runtime_path, 'r') as f: # with is a statement that opens a file
                    for line in f: # for is a statement that iterates over a collection
                        if 'PG_end_time' in line: # if PG_end_time is in line
                            end = line.split(':')[1] # end is set to the end time
                            
                            logging.info(f'end time is getting set to {end} in file {runtime_path}') # logging is a function that logs messages to the console
                        
                        return end # return is a statement that returns a value
                        
            except Exception as e: # except is a statement that handles an exception
                logging.error(f'time_read_write function FAILED to read from file {runtime_path} with error: {e}') # logging is a function that logs messages to the console
                return 0 # return is a statement that returns a value
        
        
        elif state == 0 and position == 2: # if state is 0 and position is 2
            logging.info(f'time_read_write function is starting to read from file {runtime_path}, state = 0 and position = 2') # logging is a function that logs messages to the console
            try: # try is a statement that tries to do something
                with open(runtime_path, 'r') as f: # with is a statement that opens a file
                    allLines = f.readlines() # allLines is set to the lines in the file
                    
                    startline = allLines[0] # startline is set to the first line in the file
                    endline = allLines[1] # endline is set to the second line in the file
                    
                    alrset = False # alrset is a variable that is set to False
                    
                    for i in range(len(allLines)): # for is a statement that iterates over a collection
                        #check if a line contains 'PG_total_runtime'
                        if 'PG_total_runtime' in allLines[i]:
                            alrset = True # alrset is set to True
                        else:
                            alrset = False # alrset is set to False
                    
                    newobj1 = startline.split(':')[1] # newobj1 gets split by the ':' and set to the first element in the list
                    newobj1 = newobj1.split('\n')[0] # newobj1 gets split by the '\n' and set to the first element in the list
                    newobj1 = newobj1.replace(' ', '') # newobj1 gets all ' ' replaced by ''
 
                    newobj2 = endline.split(':')[1] # newobj2 gets split by the ':' and set to the first element in the list
                    newobj2 = newobj2.replace(' ', '') # newobj2 gets all ' ' replaced by ''

                    start, end = newobj1, newobj2 # start and end are set to newobj1 and newobj2
                    
                    logging.info(f'start time is getting set to {start} in file {runtime_path}') # logging is a function that logs messages to the console
                    logging.info(f'end time is getting set to {end} in file {runtime_path}') # logging is a function that logs messages to the console

                    total = float(end) - float(start) # total is set to the difference of end and start
                    msOnly: bool = False # msOnly is set to false
                    
                    unit = 'seconds' # unit is set to 'seconds'
                    
                    if total < 1: # if end time is less than start time, then total is negative 
                        msOnly: bool = True # msOnly is set to true
                        
                        total = total * 1000 # convert to milliseconds
                        
                        logging.info(f'total time run is getting set to {total}ms in file {runtime_path}') # logging is a function that logs messages to the console
                        
                        roundedtotal = round(total, 3) # roundedtotal is set to the total time run rounded to 3 decimal places
                        
                        unit = 'ms' # unit is set to 'ms'
                        
                    else: # if end time is greater than start time, then total is positive
                        logging.info(f'total time run is getting set to {total}seconds in file {runtime_path}') # logging is a function that logs messages to the console
                        
                        roundedtotal = round(total, 3) # round to 3 decimal places
                        
                        unit = 'seconds' # unit is set to 'seconds'
                    f.close # f.close is a function that closes a file
                
                with open(runtime_path, 'a') as f: # with is a statement that opens a file
                    if alrset == False: # if the third line in the file is empty
                        if msOnly is True: # if msOnly is true
                            f.write(f"\nPG_total_runtime : {total} ms") # f.write is a function that writes to a file
                        
                        else: # if msOnly is false
                            f.write(f"\nPG_total_runtime : {total} seconds") # f.write is a function that writes to a file
                        f.close() # f.close is a function that closes a file
                    
                    else:
                        f.close() # f.close is a function that closes a file
                        
                return roundedtotal, unit # return is a statement that returns a value
            
            except Exception as e: # except is a statement that handles an exception
                logging.error(f'time_read_write state set is : {state}, {position} function FAILED with error: {e}') # logging is a function that logs messages to the console
                return 0 # return is a statement that returns a value      


        elif state == 0 and position == 3: # if state is 0 and position is 3
            logging.info(f'time_read_write function is starting to read from file {runtime_path}, state = 0 and position = 3') # logging is a function that logs messages to the console
            try: # try is a statement that tries to do something
                with open(runtime_path, 'r') as f: # with is a statement that opens a file
                    
                    allLines = f.readlines() # allLines is set to the lines in the file
                    
                    startline = allLines[0] # startline is set to the first line in the file
                    endline = allLines[1] # endline is set to the second line in the file
                    
                    alrset = False # alrset is a variable that is set to False
                    
                    for i in range(len(allLines)): # for is a statement that iterates over a collection
                        #check if a line contains 'PG_total_runtime'
                        if 'PG_total_runtime' in allLines[i]:
                            alrset = True # alrset is set to True
                        else:
                            alrset = False # alrset is set to False
                    
                    newobj1 = startline.split(':')[1] # newobj1 gets split by the ':' and set to the first element in the list
                    newobj1 = newobj1.split('\n')[0] # newobj1 gets split by the '\n' and set to the first element in the list
                    newobj1 = newobj1.replace(' ', '') # newobj1 gets all ' ' replaced by ''
                    
                    newobj2 = time.time() # newobj2 is set to the current time
                    
                    start, end = newobj1, newobj2 # start and end are set to newobj1 and newobj2
                    
                    logging.info(f'start time is getting set to {start} in file {runtime_path}') # logging is a function that logs messages to the console
                    logging.info(f'end time is getting set to {end} in file {runtime_path}') # logging is a function that logs messages to the console

                    total = float(end) - float(start) # total is set to the difference of end and start
                    msOnly: bool = False # msOnly is set to false
                    
                    unit = 'seconds' # unit is set to 'seconds'
                    
                    if total < 1: # if end time is less than start time, then total is negative 
                        msOnly: bool = True # msOnly is set to true
                        total = total * 1000 # convert to milliseconds
                        
                        logging.info(f'total time run is getting set to {total} ms in file {runtime_path}') # logging is a function that logs messages to the console
                        
                        roundedtotal = round(total, 3) # roundedtotal is set to the total time run rounded to 3 decimal places
                        
                        unit = 'ms' # unit is set to 'ms'
                        
                    else: # if end time is greater than start time, then total is positive
                        logging.info(f'total time run is getting set to {total}seconds in file {runtime_path}') # logging is a function that logs messages to the console
                        
                        roundedtotal = round(total, 3) # round to 3 decimal places
                        
                        unit = 'seconds' # unit is set to 'seconds'
                    f.close # close file
                
                with open(runtime_path, 'a') as f: # with is a statement that opens a file
                    if alrset == False: # if the third line in the file is empty
                        if msOnly is True: # if msOnly is true
                            f.write(f"\nPG_total_runtime : {total} ms") # f.write is a function that writes to a file
                        
                        else: # if msOnly is false
                            f.write(f"\nPG_total_runtime : {total} seconds") # f.write is a function that writes to a file
                        f.close() # f.close is a function that closes a file
                    
                    else:
                        f.close() # f.close is a function that closes a file
                        
                return roundedtotal, unit # return is a statement that returns a value
            
            except Exception as e: # if there is an error, return 0
                logging.error(f'time_read_write state set is : {state}, {position} function FAILED with error: {e}') # log error message
                return 0 # return 0 if there is an error
        
        elif state == None and position == None: # if state and position are None, then this is the first time the function is called
            return 0 # if state and position are None, then return None
            
    def runtests(password = None):
        if password == 'admin':
            print("testing mode active") # print to console that testing mode is active
            time.sleep(2) # sleep for 2 second
            
            tf = timefunc.time_read_write # create a variable that is equal to the time_read_write function
            
            outstate, outpos = 1, 0 # set the state and position variables to 1 and 0
            print(f"state {outstate}, pos is {outpos} : {tf(1, 0)}") # print the output of the time_read_write function with state 1 and position 0
            
            outstate, outpos = 1, 1 # set the state and position variables to 1 and 1
            print(f"state {outstate}, pos is {outpos} : {tf(1, 1)}") # print the output of the time_read_write function with state 1 and position 1
            
            outstate, outpos = 0, 0 # set the state and position variables to 0 and 0
            print(f"state {outstate}, pos is {outpos} : {tf(0, 0)}") # print the output of the time_read_write function with state 0 and position 0
            
            outstate, outpos = 0, 1 # set the state and position variables to 0 and 1
            print(f"state {outstate}, pos is {outpos} : {tf(0, 1)}") # print the output of the time_read_write function with state 0 and position 1
            
            outstate, outpos = 0, 2 # set the state and position variables to 0 and 2
            print(f"state {outstate}, pos is {outpos} : {tf(0, 2)}") # print the output of the time_read_write function with state 0 and position 2
            
            outstate, outpos = 0, 3 # set the state and position variables to 0 and 3
            print(f"state {outstate}, pos is {outpos} : {tf(0, 3)}") # print the output of the time_read_write function with state 0 and position 3
        else:
            print("testing mode not active") # print to console that testing mode is not active
            print("password is incorrect") # print to console that the password is incorrect
    
           
if __name__ == '__main__': # if this is the main file, then run the following code
     
    print("testing mode active") # print to console that testing mode is active
    
    tf = timefunc.time_read_write # create a variable that is equal to the time_read_write function
    
    outstate, outpos = 1, 0 # set the state and position variables to 1 and 0
    print(f"state {outstate}, pos is {outpos} : {tf(1, 0)}") # print the output of the time_read_write function with state 1 and position 0
    
    outstate, outpos = 1, 1 # set the state and position variables to 1 and 1
    print(f"state {outstate}, pos is {outpos} : {tf(1, 1)}") # print the output of the time_read_write function with state 1 and position 1
    
    outstate, outpos = 0, 0 # set the state and position variables to 0 and 0
    print(f"state {outstate}, pos is {outpos} : {tf(0, 0)}") # print the output of the time_read_write function with state 0 and position 0
    
    outstate, outpos = 0, 1 # set the state and position variables to 0 and 1
    print(f"state {outstate}, pos is {outpos} : {tf(0, 1)}") # print the output of the time_read_write function with state 0 and position 1
     
    outstate, outpos = 0, 2 # set the state and position variables to 0 and 2
    print(f"state {outstate}, pos is {outpos} : {tf(0, 2)}") # print the output of the time_read_write function with state 0 and position 2
    
    outstate, outpos = 0, 3 # set the state and position variables to 0 and 3
    print(f"state {outstate}, pos is {outpos} : {tf(0, 3)}") # print the output of the time_read_write function with state 0 and position 3