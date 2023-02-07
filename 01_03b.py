from collections import Counter


def main():
    # Add code here
    inventory = Counter(STA001=10, SAL002=20, ENT004=13)
    print("Original Inventory", inventory)
    # sell 5 starters, 3 salads, and 3 entrees
    sell_inventory = Counter(STA001=5, SAL002=3, ENT004=3)
    inventory.subtract(sell_inventory)
    print("Sold Inventory", inventory)
    # make 9 more starters and 1 more entree
    add_inventory = Counter(STA001=9, SAL002=0, ENT004=1)
    # or as dictionary:
    # add_inventory = {"STA001":9, "ENT004":1}
    inventory.update(add_inventory)
    print("Updated Inventory", inventory)


if __name__ == "__main__":
    main()
