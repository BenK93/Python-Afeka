
def create_a_shift_abc(shift_num):
    starting_letter = 97
    starting_letter_shifted = 97 + (shift_num % 26)
    solution = {}  # same as dict()
    # solution = {chr(i):chr(starting_letter_shifted) for i in range(starting_letter, 123) starting_letter_shifted +=1}  # same as dict()
    for i in range(starting_letter, 123):
        letter = chr(i)
        solution[letter] = chr(starting_letter_shifted)
        starting_letter_shifted += 1
        if starting_letter_shifted == 123:
            starting_letter_shifted = 97
    return solution


print("Lets shift the ABC! yayyy!")
amount = input("How much would you like to shift (0-25)?? --> ")
amount_as_int = int(amount)
shift_abc = create_a_shift_abc(amount_as_int)
print(shift_abc)


