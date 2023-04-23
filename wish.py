import random


def main():
    iwish()


def youwish(value:int = 0):
    # value: int = random.randint(1, 100)
    cnt = 0
    while value == num:
        cnt += 1
        # num: int = int(input(f"Probe {cnt} \nMy number: "))
        if value < num:
            return "Number is less"
            print("Number is less")
        elif value > num:
            return "Number is more"
            print("Number is more")
    
    return("You win!")



def iwish():
    first: int = 1
    last: int = 100

    list_entered: str = []
    value: int = random.randint(first, last)
    list_entered.append(value)
    print(f"Probe {len(list_entered)}\nMy number:", value)

    while True:
        pattern: str = input(
            f"Your hit (\"+\" - more or \"-\" - less or \"=\"):")

        if pattern == "+":
            first = value
        elif pattern == "-":
            last = value
        elif pattern == "=":
            print("I win!", "Probe count ", len(list_entered))
            break
        else:
            print("I dont undestand your hits")
            continue
        if last-first == 0:
            print("itis number", last)

        while True:
            value = random.randint(first, last)
            if value not in list_entered:
                break

        list_entered.append(value)
        print(f"Probe {len(list_entered)}\nMy number:", value)


if __name__ == "__main__":
    main()
