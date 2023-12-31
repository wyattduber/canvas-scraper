import sys
import logging

# logging
# LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s' # default format for reference
LOG_FORMAT = '%(levelname)s - %(message)s'

# debug, info, warning, error, or critical
FILE_LOG_LEVEL = logging.DEBUG
CONSOLE_LOG_LEVEL = logging.DEBUG
DEBUG_WIDGET_LOG_LEVEL = logging.DEBUG

# Log file location for different OS's (development)
if sys.platform == "win32":
    TEMP_DIR = "C:\\Temp"
    DEFAULT_LOG_FILE = f"C:\\Temp\\cydaq_current_log.log"
    DEFAULT_BB_DATA_FILE = f"C:\\Temp\\bb_data_file.csv"
else:
    TEMP_DIR = "/tmp"
    DEFAULT_LOG_FILE = f"/tmp/cydaq_current_log.log"
    DEFAULT_BB_DATA_FILE = f"/tmp/bb_data_file.csv"
TEMP_SAMPLE_LOCATION = 'C:\\Temp\\sample_{}.csv'  # the {} is where the time is calculated and placed

# Canvas Info
CANVAS_URL = "https://canvas.iastate.edu"
COURSE_ID = "97241"

# Driver Info
if sys.platform == "win32":
    DRIVER_PATH = "..\\drivers\\chromedriver.exe"
else:
    DRIVER_PATH = "../drivers/chromedriver" # TODO get a linux chrome driver