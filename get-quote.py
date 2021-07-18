import random
import sys


def primary():
    # print('keep it logically awesome')

    f = open("quotes.txt")
    quotes = [line.strip() for line in f.readlines()]
    f.close()

    last = len(quotes) - 1
    rnd = random.randint(0, last)
    rnd0 = random.randint(0, last)
    print(quotes[rnd])
    print(quotes[rnd0])


def addlines():
    str0 = str(input("Quote you want to add to file: "))
    f = open("quotes.txt", "a+")
    f.write(str0 + "\n")
    f.close()

def removeblank():
    output=""
    with open("quotes.txt") as d:
        for line in d:
            if not line.isspace():
                output+=line
    f = open("quotes.txt", "w")
    f.write(output)

if __name__ == "__main__":
    addlines()
    removeblank()
    primary()
