# 30 / 100
# list_of_numbers = [int(number) for number in input().split()]
# command = input()
#
# while command != 'end':
#     command = command.split()
#     command_type = command[0]
#     string_command = command[-1]
#     counter = 0
#     max_number_list = []
#     min_number_list = []
#     first_counter = []
#     last_counter = []
#     if command_type == 'exchange':
#         index_command = int(command[1])
#         length = len(list_of_numbers)
#         if 0 <= index_command < length:
#             list_of_numbers = list_of_numbers[index_command + 1:] + list_of_numbers[:index_command + 1]
#         else:
#             print('Invalid index')
#
#     elif command_type == 'max':
#         if string_command == 'even':
#             for even in list_of_numbers:
#                 if even % 2 == 0:
#                     max_number_list.append(even)
#         elif string_command == 'odd':
#             for odd in list_of_numbers:
#                 if odd % 2 != 0:
#                     max_number_list.append(odd)
#         if max_number_list:
#             max_number = max(max_number_list)
#             max_list_counter = min_number_list.count(max_number)
#             if max_list_counter > 1:
#                 max_indexes = [index for index, digit in enumerate(list_of_numbers) if digit == max_number]
#                 print(max_indexes[-1])
#             else:
#                 max_number_list = list_of_numbers.index(max_number)
#                 print(max_number_list)
#         else:
#             print("No matches")
#     elif command_type == 'min':
#         if string_command == 'even':
#             for even in list_of_numbers:
#                 if even % 2 == 0:
#                     min_number_list.append(even)
#         elif string_command == 'odd':
#             for odd in list_of_numbers:
#                 if odd % 2 != 0:
#                     min_number_list.append(odd)
#         if min_number_list:
#             min_number = min(min_number_list)
#             min_list_counter = min_number_list.count(min_number)
#             if min_list_counter > 1:
#                 min_indexes = [index for index, digit in enumerate(list_of_numbers) if digit == min_number]
#                 print(min_number_list[-1])
#             else:
#                 min_number_list = list_of_numbers.index(min_number)
#                 print(min_number_list)
#         else:
#             print("No matches")
#     elif command_type == 'first':
#         index_command = int(command[1])
#         length = len(list_of_numbers)
#         if index_command > length:
#             print('Invalid count')
#         elif string_command == 'even':
#             for i in range(index_command):
#                 for even_counter in list_of_numbers:
#                     if even_counter % 2 == 0:
#                         counter += 1
#                         first_counter.append(even_counter)
#                         if counter == index_command:
#                             break
#                 if first_counter:
#                     print(first_counter)
#                 else:
#                     print('[]')
#         elif string_command == 'odd':
#             for odd_counter in list_of_numbers:
#                 if odd_counter % 2 != 0:
#                     counter += 1
#                     first_counter.append(odd_counter)
#                     if counter == index_command:
#                         break
#             if first_counter:
#                 print(first_counter)
#             else:
#                 print('[]')
#     elif command_type == 'last':
#         index_command = int(command[1])
#         length = len(list_of_numbers)
#         if index_command > length:
#             print('Invalid count')
#         elif string_command == 'even':
#             for even_counter in reversed(list_of_numbers):
#                 if even_counter % 2 == 0:
#                     counter += 1
#                     last_counter.append(even_counter)
#                     if counter == index_command:
#                         break
#             if last_counter:
#                 print(last_counter)
#             else:
#                 print('[]')
#         elif string_command == 'odd':
#             for odd_counter in reversed(list_of_numbers):
#                 if odd_counter % 2 != 0:
#                     counter += 1
#                     last_counter.append(odd_counter)
#                     if counter == index_command:
#                         break
#             if last_counter:
#                 print(last_counter)
#             else:
#                 print('[]')
#     command = input()
# print(list_of_numbers)