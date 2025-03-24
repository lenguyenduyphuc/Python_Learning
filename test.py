def pen(num):
    result = []
    for i in range(1, num + 1):
        number = int((3*i**2 - i)/2)
        result.append(number)
    return result

def hep(num):
    result = []
    for i in range(1, num + 1):
        number = int((5*i**2 - 3*i)/2)
        result.append(number)
    return result

def hen(num):
    result = []
    for i in range(1, num + 1):
        number = int((9*i**2 - 7*i)/2)
        result.append(number)
    return result

def main():
    print('''Welcome to the number sequence generator program\n
Here are your choices:\n
1. Pentagonal Sequence\n
2. Heptagonal Sequence\n
3. Hendecagonal Sequence\n''')
    inp = "yes"
    while inp.lower() == "yes":
        inp = input("Enter your choice (1-3): ")
        if inp.lower() == "no":
            break
        num = int(inp)
        while (num < 1 or num > 3):
            num = int(input("Invalid entry. Re-enter your choice (1-3): "))
        loops = int(input("Enter the value of the list (>=3): "))
        while loops < 3:
            loops = int(input("Invalid entry. Re-enter the value of the list (>=3): "))
        result = []
        shape = ""
        if num == 1:
            shape = "pentagonal"
            result = pen(loops)
        elif num == 2:
            shape = "heptagonal"
            result = hep(loops)
        elif num == 3:
            shape = "hendecagonal"
            result = hen(loops)
        print(f"Here is a list containing the first {loops} numbers of the {shape} sequences: {result}")
        odd = []
        for number in result:
            is_odd = lambda x:x % 2 != 0
            if (is_odd(number)):
                odd.append(number)
        print(f"And here is the list of odd {shape} numbers: {odd}")
        inp = input("Would you like to try again? Enter yes or no: ")
        while inp.lower() != "yes" and inp.lower() != "no":
            inp = input("Invalid. Would you like to try again? Enter yes or no: ")
    print("GoodBye")

if __name__ == "__main__":
    main()
