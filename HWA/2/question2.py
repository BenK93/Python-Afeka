
number = int(input("Give me integer smaller or equal to 256: "))

def solve(number):
    binary = convert_to_binary(number)
    solution_arr = [0 for i in range(8)]
    # [0,0,0,0,0,0,0,0] --> [0,0,0,0,1,1,0,1]
    # binary = 1101
    for i, num in enumerate(binary):
        index = len(binary) + i
        solution_arr[index] = int(num)
    print(solution_arr)



def convert_to_binary(number):
    binary = ""
    while number > 0:
        origin = number
        divided = number // 2
        if divided <= 1 or origin % divided == 1:
            binary += "1"
        elif divided > 1:
            binary += "0"
        number = number // 2
    return binary[::-1]


if number <= 255 and number >= 0:
    solve(number)
    # print(convert_to_binary(88))
else:
    print("try again")

