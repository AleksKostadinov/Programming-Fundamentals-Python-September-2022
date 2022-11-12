def is_winning_ticket(ticket_):
    if len(ticket_) != 20:
        return 'invalid ticket'
    symbols = '@', '#', '$', '^'
    left_side = ticket_[:10]
    right_side = ticket_[10:]
    for symbol in symbols:
        for sequence in range(10, 5, -1):
            win_symbol = sequence * symbol
            if win_symbol in left_side and win_symbol in right_side:
                if sequence == 10:
                    return f'ticket "{ticket_}" - {sequence}{symbol} Jackpot!'
                return f'ticket "{ticket_}" - {sequence}{symbol}'
    return f'ticket "{ticket_}" - no match'


tickets = [ticket.strip() for ticket in input().split(',')]
[print(is_winning_ticket(ticket)) for ticket in tickets]
