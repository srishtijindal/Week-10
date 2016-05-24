#create a new type of exception
class Low_Inventory_Exception(Exception):
    def __init__(self):
        print("The inventory is low!")

def test():
    inventory = 1
    if inventory < 10:
        raise Low_Inventory_Exception

try:
    test()
except(Low_Inventory_Exception):
    print("Something is not right.")
else:
    print("Inventory is full.")
finally:
    print("Inventory will soon be filled up")