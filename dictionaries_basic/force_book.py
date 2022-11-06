command = input()
force_dict = {}
while command != 'Lumpawaroo':
    if '|' in command:
        force_side, force_user = command.split(' | ')
        user_is_part_of_the_force = False
        for key, value in force_dict.items():
            if force_user in value:
                user_is_part_of_the_force = True
                break
        if not user_is_part_of_the_force:
            if force_side not in force_dict.keys():
                force_dict[force_side] = [force_user]
            else:
                force_dict[force_side].append(force_user)
    else:
        force_user, force_side = command.split(' -> ')
        for key, value in force_dict.items():
            if force_user in value:
                force_dict.pop(key)
                break
        if force_side not in force_dict.keys():
            force_dict[force_side] = [force_user]
        else:
            force_dict[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
    command = input()
for key, value in force_dict.items():
    print(f'Side: {key}, Members: {len(value)}')
    for user in value:
        print(f"! {user}")
