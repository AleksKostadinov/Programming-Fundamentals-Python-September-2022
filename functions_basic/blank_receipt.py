def receipt_header():
    return f'CASH RECEIPT\n------------------------------'


def receipt_body():
    return f'Charged to____________________\nReceived by___________________'


def receipt_footer():
    return f'------------------------------\n(c) SoftUni'


def receipt():
    print(receipt_header())
    print(receipt_body())
    print(receipt_footer())


request = input()
receipt()