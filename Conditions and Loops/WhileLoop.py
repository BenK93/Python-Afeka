# Print i as long as i is less than 6:
i = 1
while i < 6:
    print(i)
    i += 1

print('---------------------------')
# Exit the loop when i is 3:
j = 1
while j < 6:
    print(j)
    if j == 3:
        break
    j += 1

print('---------------------------')
# Continue to the next iteration if i is 3:
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
