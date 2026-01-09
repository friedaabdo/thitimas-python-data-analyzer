#create a function save_numbers(numbers, filename="data.json")
#it should save the list of numbers to a JSON file as a dictionary with key "numbers"
#use indent = 2
#overwrite the file if it already exists
#do not print anything in this function
import json
def save_numbers(numbers, filename="data.json"):
    with open(filename, "w") as f:
        json.dump({"numbers": numbers}, f, indent=2)
#end of storage.py

