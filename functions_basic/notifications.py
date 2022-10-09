def show_success_message(operation, message):
    length = '=' * len(f'Successfully executed {operation}.')
    return f'Successfully executed {operation}.\n{length}\n{message}.\n'


def show_warning_message(message):
    length = '=' * len(f'Warning: {message}.')
    return f'Warning: {message}.\n{length}\n'


def show_error_message(operation, message, error_code):
    length = '=' * len(f'Error: Failed to execute {operation}.')
    return f'Error: Failed to execute {operation}.\n{length}\nReason: {message}.\nError code: {error_code}.\n'


def read_and_process_message():
    for line in range(number_lines):
        line_text = input()
        if line_text == 'success':
            operations = input()
            messages = input()
            print(show_success_message(operations, messages))
        elif line_text == 'warning':
            messages = input()
            print(show_warning_message(messages))
        elif line_text == 'error':
            operations = input()
            messages = input()
            error_codes = input()
            print(show_error_message(operations, messages, error_codes))


number_lines = int(input())

read_and_process_message()
