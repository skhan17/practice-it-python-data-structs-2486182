from collections import deque

def main():
    # add code here
    foods = deque(maxlen=5)
    foods.append("STA001")
    ordered_food = ["STA003", "SAL002", "ENT004", "DES003"]
    deque(['STA003', 'SAL002', 'ENT004', 'DES003', 'DES002'], maxlen=5)
    foods.extend(ordered_food)
    foods.append("DES002")
    # deque(['STA003', 'SAL002', 'ENT004', 'DES003', 'DES002'], maxlen=5)
    # foods.appendleft("ENT004")
    # deque(['ENT004', 'STA003', 'SAL002', 'ENT004', 'DES003'], maxlen=5)
    print(foods)
    return

if __name__ == "__main__":
    main()
