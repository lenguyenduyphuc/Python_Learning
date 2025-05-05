import math
from tabulate import tabulate

def totient(n):
    temp, res = n, n
    prime_factors = [1]
    for i in range (2, math.floor(math.sqrt(n))):
        while (temp % i == 0):
            if (i > prime_factors[-1]):
                prime_factors.append(i)
            temp //= i
    if (temp > 1):
        prime_factors.append(temp)
    for i in prime_factors:
        if (i > 1):
            res -= res // i
    return res

def bin_exp(a, b, mod):
    if (b < 2):
        return a ** b % mod
    return bin_exp(a, b // 2, mod) * bin_exp(a, b // 2, mod) * (1 + (b % 2) * (a - 1)) % mod
def bin_exp_plus(a, b, mod):
    digits = []
    powers = []
    modulo = []
    result = 1
    bb = b
    while (bb > 0):
        digits.append(bb % 2)
        if (len(powers) == 0):
            powers.append(1)
            modulo.append(a)
        else:
            powers.append(powers[-1] * 2)
            modulo.append(modulo[-1] * modulo[-1] % mod)
        bb //= 2
    print(tabulate([[f"e^{powers[i]} mod {mod}", modulo[i]] for i in range (len(digits))]))
    print(f"φ(φ(n)) - 1 = ", end = '')
    for i in range (len(digits) - 1):
        if (digits[i] > 0):
            result = result * modulo[i] % mod
            print(powers[i], end = " + ")
    print(powers[-1])
    result = result * modulo[-1] % mod
    for i in range (len(digits)):
        if (digits[i] > 0):
            print(f"(e^{powers[i]})", end = '')

    print(f"\ne^(φ(φ(n))-1) mod φ(n) = {result}\nEuler's Theorem")
    return result

print("Welcome to the COT3100 Mini-Project Instant Answer!\nThis code was made possible by Neutral.")
print("Every line here is original work. Or is it?!")
print("You're free to do whatever you want with it. Learn from it, edit it, revise it, butcher it, publish it and claim it as your work\n")
print("Just input the numbers that you have, and the code will instantly give you all the results you need!\n")

p = int(input("Enter your p here: "))
q = int(input("Enter your q here: "))
e = int(input("Enter your e here: "))
n = p * q
phi_n = totient(n)
phi_phi_n = totient(phi_n)
print("P1")
print('-' * 50)
print(f"n = {n}")
print(f"φ(n) = {phi_n}")
print(f"E(x) = x^{e} mod {n}")

quo, rem, x, y = [0, 0], [phi_n, e], [1, 0], [0, 1]
while (rem[-1] > 0):
    l = len(quo)
    quo.append(rem[l - 2] // rem[l - 1])
    rem.append(rem[l - 2] % rem[l - 1])
    x.append(x[l - 2] - x[l - 1] * quo[l])
    y.append(y[l - 2] - y[l - 1] * quo[l])
print(tabulate([[i, quo[i + 1], rem[i + 1], x[i + 1], y[i + 1]] for i in range (-1, len(quo) - 1)]))
print("Footnote: This table has an extra line. Don't worry about that, so just ignore the last line!")
print(f"d = {y[-2]} = {phi_n + y[-2]} mod φ(n)")
print('-' * 50)
print("P2")
print('-' * 50)
print(f"φ(φ(n)) = {phi_phi_n}")
print(f"φ(φ(n)) - 1 = No, your dumbass can subtract 1 by yourself. I have many more hard calculations coming up")
d = bin_exp_plus(e, phi_phi_n - 1, phi_n)

print("\nHuh. I don't think we've interacted with each other for a while")
print("(Maybe it has only been a couple of milliseconds for you, but for me it's been millions of calculations)")
print("Well, here we go, the final stretch")
print('-' * 50)
print("P3")
print('-' * 50)
id = input("Enter your U-Number (without the U, this is important!!): ")
print(f"D(x) = x^{d} mod {n}")
print(tabulate([i + 1, dig := ord(id[i]) - 48, 10 * (i + 1) + dig, bin_exp(10 * (i + 1) + dig, d, n)] for i in range(8)))
print('-' * 50)
bye = input("You have all the answers now!\nThank you!\nIs there anything you wanna say to me, or to my creator Neutral?\n(Don't let him know this, but I hate him)\n")