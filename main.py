import time, os

inventory = []

def prettyPrint(item):
  print()
  print(f"You have {inventory.count(item)} {item}")

try:
  f = open("inventory.txt", "r")
  inventory = eval(f.read())
  f.close()
except:
  print("There is no existing pizza list...we will use our own blank list.")
  time.sleep(1)
  os.system("clear")

while True:
  print("🌟RPG Inventory🌟")
  print()
  option = input("1:Add  2:Remove  3:View > ").strip().lower()
  print()
  
  if option == "add" or option == "1":
    item = input("What do you want to add? > ").capitalize()
    inventory.append(item)
    
  elif option == "remove" or option == "2":
    i = input("What do you want to remove? > ").capitalize()
    inventory.remove(i)
    
  elif option == "view" or option == "3":
    b = input("Which item would you like to view > ").capitalize()
    prettyPrint(b)

  f = open("inventory.txt", "w")
  f.write(str(inventory))
  f.close()

  time.sleep(1)
  os.system("clear")
