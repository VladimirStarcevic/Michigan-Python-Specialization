from typing import Dict,List, Any

def process_shopping_list(dict_in: Dict, list_in: List) -> Any:
    availableItems = []
    unavailableItems = []
    total_cost = 0

    for item in list_in:
        if item in dict_in and dict_in[item]["Stock"] > 0:
            availableItems.append(item)
            total_cost += dict_in[item]["Price"]
            dict_in[item]["Stock"] -= 1
        else:
            unavailableItems.append(item)

    print(f"availableItems = {availableItems}")
    print(f"unavailableItems = {unavailableItems}")
    print(f"totalCost = {total_cost}")


groceryList=["Apples", "Eggs", "Milk", "Avocados", "Broccoli", "Celery", "Cherries"]

inventory = {"Apples": {"Price": 1.50, "Stock": 10}, "Bananas": {"Price": 1.00, "Stock": 12},
             "Eggs": {"Price": 3.00, "Stock": 7}, "Milk": {"Price": 3.50, "Stock": 20},
             "Oranges": {"Price": 0.75, "Stock": 35}, "Avocados": {"Price": 2.50, "Stock": 5},
             "Celery": {"Price": 1.25, "Stock": 15}}

process_shopping_list(inventory, groceryList)
