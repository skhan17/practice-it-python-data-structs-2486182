from collections import namedtuple, defaultdict
from csv import reader
from pprint import pprint

def main():
    #add code here
    res = defaultdict(int)

    with open("data/OrderItems.csv", "r") as open_csv:
        read = reader(open_csv)
        Item = namedtuple("Item", next(read))
        for line in read:
            item = Item(*line)
            res[item.ProductID] += int(item.Quantity)
    pprint(dict(res))
    return

# shows DES is most popular
# {'BEV001': 6,
#  'BEV002': 4,
#  'BEV003': 6,
#  'DES001': 11,
#  'DES002': 8,
#  'DES003': 1,
#  'DES004': 12,
#  'DES005': 7,
#  'ENT001': 3,
#  'ENT002': 6,
#  'ENT003': 2,
#  'ENT004': 10,
#  'ENT005': 5,
#  'SAL001': 5,
#  'SAL002': 5,
#  'SAL004': 5,
#  'STA001': 1,
#  'STA003': 6,
#  'STA004': 1,
#  'STA005': 8}

if __name__ == "__main__":
    main()