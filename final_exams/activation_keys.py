text = input()
command = input()

while command != 'Generate':
    action, *other = (int(x) if x.isdigit() else x for x in command.split('>>>'))
    if action == 'Contains':
        substring = str(other[0])
        if substring in text:
            print(f"{text} contains {substring}")
        else:
            print("Substring not found!")
    elif action == 'Flip':
        upper_lower, start_index, end_index = other
        if upper_lower == 'Upper':
            text = text[:start_index] + (text[start_index:end_index]).upper() + text[end_index:]
        elif upper_lower == 'Lower':
            text = text[:start_index] + (text[start_index:end_index]).lower() + text[end_index:]
        print(text)
    elif action == 'Slice':
        start_index, end_index = other
        text = text[:start_index] + text[end_index:]
        print(text)
    command = input()
print(f'Your activation key is: {text}')
