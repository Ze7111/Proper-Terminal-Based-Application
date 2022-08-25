import logging, os, time, json
from random import randrange as r
from rich import console


this_file: str = os.path.basename(__file__)
rundone: bool = False
runtimerundone: bool = False
runtimelogdone: bool = False

class file_opperations:
    global this_file
    def count_files(directory: str) -> int:
        logging.info(f'count_files function is starting in file {this_file}')
        
        try:
            x = len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))])
        except Exception as e:
            logging.error(f'count_files function FAILED in file {this_file} with error: {e}')
            return None
        
        logging.info(f'count_files function is finished in file {this_file}')
        return x
    
    def count_log_files(directory):
        global rundone
        if rundone is not True:
            logging.info(f'count_log_files function is starting in file {this_file}')
        try:
            list_of_files = os.listdir(directory)
            log_files_path = ["logs/{0}".format(x) for x in list_of_files]
        except Exception as e:
            logging.error(f'count_log_files function FAILED in file {this_file} with error: {e}')
            return None
        if rundone is not True:
            logging.info(f'count_log_files function is finsihed in file {this_file}')
            rundone = True
        return log_files_path      
    
    def count_runtime_files(directory: str) -> int:
        global runtimerundone
        if runtimerundone is not True:
            logging.info(f'count_log_files function is starting in file {this_file}')
        try:
            list_of_files = os.listdir(directory)
            runtime_files_path = [directory+"{0}".format(x) for x in list_of_files]
        except Exception as e:
            logging.error(f'count_runtime_files function FAILED in file {this_file} with error: {e}')
            return None
        if runtimerundone  is not True:
            logging.info(f'count_lruntime_files function is finsihed in file {this_file}')
            runtimerundone = True
        return runtime_files_path
    
    def read_runtime_config(conf_path: str):
        global this_file, runtimelogdone
        logging.info(f'read_runtime_config function is starting in file {this_file}')
        
        try:
            with open(conf_path) as json_file:
                logging.info(f"openning config file {conf_path} in file {this_file}")
                
                data = json.load(json_file)
                runtime_config_data = data['RuntimeConfig']
                runtime_config_data = runtime_config_data[0]
                
                logging.info(f'Successfully read base indentation from config file')
                
                program_start_text: str = runtime_config_data['StartText']
                program_end_text: str = runtime_config_data['EndText']
                program_current_text: str = runtime_config_data['CurrentText']
                recent_runtime: str = runtime_config_data['RecentRuntime']
                raw_Runtime: str = runtime_config_data['RawRuntime']
                file_name_format: str = runtime_config_data['FileNameFormat']
                base_file_path: str = runtime_config_data['FilePath']
                file_name: str = runtime_config_data['FileName']
                max_files: int = runtime_config_data['MaxFiles']
                make_runtime_files: bool = runtime_config_data['MakeRuntimeFile?']
                
                
                if make_runtime_files is False:
                    logging.info(f'Make Runtime File is set to False, so no runtime file will be made')
                    max_files = 0

                file_name = file_name.replace('<date.time>', time.strftime('%d-%m-%Y %H-%M-%S',time.localtime()))
                file_path = f"{base_file_path}{file_name}"
                
                if runtimelogdone is not True:
                    logging.info(f"runtime config data loaded with values:\n'Start Text' = '{program_start_text}'\n'End Text' = '{program_end_text}'\n'Recent Runtime Text' = '{recent_runtime}'\n'File Name Format' = '{file_name_format}'\n'File Path' = '{file_path}'\n'File Name' = '{file_name}'\n'Max Runtime Files' = {max_files}\n'Make Runtime File' = {make_runtime_files}")
                    runtimelogdone = True
                    
                if len(file_opperations.count_runtime_files(base_file_path)) >= max_files: # if number of files in ./logs is greater than 10
            
                    logging.info(f"Number of runtime files in .\{base_file_path} is {len(file_opperations.count_runtime_files(base_file_path))} before deletion") # log number of files ./logs
                    
                    while len(file_opperations.count_runtime_files(base_file_path)) > max_files:
                        oldest_file = min(file_opperations.count_runtime_files(base_file_path), key=os.path.getctime) # get oldest file in ./logs
                        os.remove(oldest_file) # remove oldest file in ./logs
                        logging.info(f"Removed runtime file {oldest_file} in .\{base_file_path}") # log number of files ./logs
                    
                    logging.info(f"Number of runtime files in .\{base_file_path} is {len(file_opperations.count_runtime_files('logs'))} after deletion") # log number of files ./logs

                logging.info(f'read_runtime_config function is finished in file {this_file}')
                
                json_file.close()
                return program_start_text, program_end_text, program_current_text, recent_runtime, raw_Runtime, file_name_format, file_path, file_name, max_files, make_runtime_files
        except Exception as e:
            logging.error(f'read_runtime_config function FAILED in file {this_file} with error : {e}')
            return None
    
    def red_codes():
        Codes = 'Codes File'
        with open('/data/codes.bf', 'w') as f:
            f.write(f'{Codes:-^80}')
            s1 = r(1000, 9999)
            s2 = r(1000, 9999)
            s3 = r(100, 999)
            f.write(f'{s1}-{s2}-{s3}')
            f.close()
            
    
class JSON_read:
    global this_file
    def read_log_config(conf_path: str):
        # ------------------- CAN NOT LOG THIS FUNCTION -------------------
        if conf_path is None:
            return None
        try:
            with open(conf_path) as json_file:
                data = json.load(json_file)
                logging_Config_Data = data['LoggingConfig']
                logging_Config_Data = logging_Config_Data[0]
                
                logging_status: bool = logging_Config_Data['logging']
                logging_level: str = logging_Config_Data['level']
                logging_path: str = logging_Config_Data['path']
                logging_format: str = logging_Config_Data['format']
                logging_datefmt: str = logging_Config_Data['datefmt']
                logging_maxFiles: int = logging_Config_Data['maxFiles']
                deleteallonrun: bool = logging_Config_Data['deleteAllonRun?']
                
                if deleteallonrun is True:
                    logging_maxFiles = 1
        
                logging_path = logging_path.replace('<date.time>', time.strftime('%d-%m-%Y %H-%M-%S',time.localtime()))
                
                if logging_status is False:
                    logging_path = logging_path.split('.')[0] + '.disabled.log'
                
                json_file.close()
                return logging_status, logging_path, logging_level, logging_format, logging_datefmt, logging_maxFiles                
        except Exception:
            return None
        
    def read_color_hex(color: str, pallate: int):
        conf_path: str = "config\\config.json" #config\\config.json -------------------------------------------------------------- conf path
        # 2 Palletes: 0 for 4 colors and 1 for 22 colors
        if conf_path is None:
            return "#ffffff"
        if pallate is None:
            return "#ffffff"
        try:
            with open(conf_path) as json_file:
                data = json.load(json_file)
                color_hex_data = data['Colors']
                color_hex_data = color_hex_data[pallate]
                
                color_hex: str = color_hex_data[color]
                
                json_file.close()
                return color_hex

        except Exception as e:
            logging.error(f"conf Error : {e}")
            exit()