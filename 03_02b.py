from csv import reader
from collections import namedtuple


def main():
    # add code here
    # read data/Customer.csv
    lastName = []

    with open("data/Customer.csv", "r") as open_csv:
        read = reader(open_csv)
        Person = namedtuple("Person", next(read))
        for line in read:
            person = Person(*line)
            print(person)
            lastName.append(person.LastName)
            # if person.State == "PA":
            #     print(person)

    # Create workable objects with each line
    for l in lastName:
        print(l)

    return


if __name__ == "__main__":
    main()
