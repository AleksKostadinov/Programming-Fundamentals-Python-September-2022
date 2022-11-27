text = [x for x in input()]
odd_text = []
command = input()
while command != 'Done':
    command_list = command.split()
    action = command_list[0]
    if action == 'TakeOdd':
        for char in range(1, len(text), 2):
            odd_text += text[char]
        text = odd_text
        print(*text, sep='')
    elif action == 'Cut':
        start_index = int(command_list[1])
        end_index = int(command_list[2]) + start_index
        if 0 <= start_index <= end_index < len(text):
            text = text[:start_index] + text[end_index:]
            print(*text, sep='')
    elif action == 'Substitute':
        substring = command_list[1]
        substitute = command_list[2]
        text = ''.join(text)
        if substring in text:
            text = text.replace(substring, substitute)
            print(*text, sep='')
        else:
            print("Nothing to replace!")

    command = input()
print(f"Your password is: {''.join(text)}")
