t = 0

for k in range(1, 1160567):  # 1 to 1,160,566 inclusive
    if k % 6 == 0 or k % 7 == 0 or k % 11 == 0:
        t += 1

print(t)
