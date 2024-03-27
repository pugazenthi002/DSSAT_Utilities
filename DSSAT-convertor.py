from utils import utils
from libs import wth_handler
from nasapo import ndown1
from gui import gui1
default_headers = ["DATE", "SRAD", "TMAX", "TMIN", "RAIN", "DEWP", "WIND", "PAR", "EVAP", "RHUM"]
input_headers=["DATE", "TMAX", "TMIN", "SRAD", "RAIN", "RHUM", "WIND", "EVAP", "PAR", "DEWP"]
#directory=r'C:\Users\ACRC\Desktop\boach\WTXC\weather\DSSAT-WTH-CREATOR-main\in'
#directory=r'/run/media/jeeva/DATA/code-fun/python/DSSAT-convertor-CLI/Renamed/Historical_IMD'

def main():

    csvs=utils.get_csv_files(dzz)
    for csv_file in csvs:
        print("input_file",csv_file)
        wth_handler.format_wth(dzz,csv_file,default_headers,input_headers)
        print("output",csv_file)

def down():
    ndown1.down()


"""
if __name__ == "__main__":
    gui1.gui.run()
    #down()
   # main()
"""