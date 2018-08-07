num_input = int(input("input:"))

input_list = list(range(num_input + 1))

output = []

for i in range(1, len(input_list)):
    if input_list[i]%3 != 0 and input_list[i]%5 != 0:
        output.append(input_list[i])
    elif input_list[i]%15 == 0:
        output.append(input_list[i])

print("output:" + str(len(output)))