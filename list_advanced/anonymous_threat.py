def merge(list_data, start, end):
    if start < 0:
        start = 0
    if end >= len(list_data):
        end = len(list_data) - 1
    current_merge = list_data[start:end + 1]
    new_merged_list = ["".join(current_merge)]
    new_string = list_data[:start] + new_merged_list + list_data[end + 1:]
    return new_string
    

def divide(list_data, start_index, end_index):
    divided_word = list_data[start_index]
    new_word = []
    part = len(divided_word) // end_index
    start = 0
    end = part
    for i in range(end_index - 1):
        new_word.append(divided_word[start:end])
        start += part
        end += part
    new_word.append(divided_word[start:])
    new_string = list_data[:start_index] + new_word + list_data[start_index + 1:]
    return new_string


input_data = input().split()
command = input()

while command != "3:1":
    command = command.split()
    action = command[0]
    start_index = int(command[1])
    end_index = int(command[2])
    if action == "merge":
        input_data = merge(input_data, start_index, end_index)
    elif action == "divide":
        input_data = divide(input_data, start_index, end_index)
    command = input()
print(*input_data)
