from SCTracker import GUI
from SCTracker.constants import config_file

if __name__ == "__main__":
    # creates file if it doesn't exist
    with open(config_file, 'a') as f:
        print('loading config file')
    
    gui = GUI.GUI(None)