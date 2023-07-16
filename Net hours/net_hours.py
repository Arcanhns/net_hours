import os
import json
from termcolor import colored

def net_hours():
    global hours_bank
    global current_paycheck

    hours_bank += float(today_hours)
    current_paycheck = round(hours_bank * hourly_rate)
    
    print("-----------------------------------")
    print(colored("NET HOURS", "yellow").center(42))
    print("-----------------------------------")
    print("HOURS WORKED TODAY: ", today_hours)
    print("CURRENT HOURS BANK:", hours_bank)
    print("CURRENT SALARY: €" + str(current_paycheck))
    print("-----------------------------------")

if not os.path.exists("data.json"):
    data = {"hours_bank": 0, "current_paycheck": 0}
    with open("data.json", "w") as file:
        json.dump(data, file)

with open("data.json", "r") as file:
    data = json.load(file)
    hours_bank = float(data["hours_bank"])
    current_paycheck = float(data["current_paycheck"])

hourly_rate = None #<-- REPLACE NONE WITH UR HOURLY RATE
today_hours = 0

print("-----------------------------------")
print(colored("NET HOURS", "yellow").center(42))
print("-----------------------------------")
print("HOURS WORKED TODAY: ", today_hours)
print("CURRENT HOURS BANK:", hours_bank)
print("CURRENT SALARY: €" + str(current_paycheck))
print("-----------------------------------")

while True:
    today_hours = float(input("HOW MANY HOURS TODAY? "))
    os.system('cls')
    net_hours()

    data = {"hours_bank": hours_bank, "current_paycheck": current_paycheck}
    with open("data.json", "w") as file:
        json.dump(data, file)
