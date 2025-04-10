user_input = input()
while user_input != 'end':
    try:
        # Possible ValueError
        divisor = int(user_input)
        if divisor < 0:
            # Possible NameError because
            # compute() is not defined
            print(compute(divisor))
        else:
            # Possible ZeroDivisionError
            print(20 // divisor)     # Truncates to an integer
    except ValueError:
        print('v')
    except ZeroDivisionError:
        print('z')
    except:
        print('x')
    user_input = input()
print('OK')