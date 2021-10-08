# import lib
import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import pyfirmata

# The following section has been comented out because is raspberry dependendant
# # Import the raspberry dedicated libraries
# import RPi.GPIO as GPIO
#
# GPIO setup
rele = 13 

board = pyfirmata.Arduino("/dev/ttyACM0")
# setup the acces to google sheet
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Tutorial_Python_Apps_Follow").sheet1

# Get all data from document
data = sheet.get_all_records()

#  Evaluate one cell
cell = sheet.cell(2, 2). value
if cell == "James":
    print("the thing is on")
    board.digital[rele].write(1)
    time.sleep(10)
    print("the thing is off")
    board.digital[rele].write(0)
    
