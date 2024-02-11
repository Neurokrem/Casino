import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROW = 3
COLUMN = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def victory_condition(colums, rows, bet, values):
    victories = 0
    victory_lines = []
    for line in range(rows):
        symbol = colums[0][line]
        for stupac in colums:
            symbol_to_check = stupac[line]
            if symbol != symbol_to_check:
                break
        else:
            victories += values[symbol] * bet
            victory_lines.append(line + 1)
    return victories

def get_slot_machine_spin(row, column, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(column):
        column = []
        current_symbol = all_symbols[:]
        for _ in range(row):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot(columns):
     #transponiranje matrice
     for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def depozit():
    while True:
        ammount = input("Ammount of Your deposit: ")
        if ammount.isdigit():
            ammount = int(ammount)
            if ammount > 0:
                break
            else:
                print("Betting ammount has to be higher than zero!")
        else:
            print("Please enter a number.")
    return ammount

def number_of_rows():
    while True:
        single_line = input("How many bet lines (1-"+ str(MAX_LINES) + ")? ")
        if single_line.isdigit():
            single_line = int(single_line)
            if 1 <= single_line <= MAX_LINES:
                break
            else:
                print("number of rows is between 1 and 3!")
        else:
            print("Please enter a number.")
    return single_line

def give_bet():
    while True:
        bet = input("How much are you willing to bet on every row? ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Ammount has to be between {MIN_BET}€ - {MAX_BET}€")
        else:
            print("Please enter a number.")
    return bet

def game(balance):
    row = number_of_rows()
    while True:
        bet = give_bet()
        total_bet = bet * row
        if total_bet > balance:
            print(f"You do not have enough money for betting! Your current balance is {balance}€")
        else:
            break
    
    print(f"You bet {bet}€ on {row} rows. Total bet ammount is {total_bet}€")
    slots = get_slot_machine_spin(ROW, COLUMN, symbol_count)
    print_slot(slots)
    rounds_won = victory_condition(slots, row, bet, symbol_value)
    print(f"You accumulated {rounds_won}€")
    #print(f"Pogodio si retke:", *pobjedne_linije)
    return rounds_won - total_bet

#### Ovdje je glavna funkcija ####
def main():
    balance = depozit()
    while True:
        print(f"Current ammount: {balance}€")
        answer = input("Press ENTER for new game (q to quit)")
        if answer == "q":
            break
        balance += game(balance)
        if balance == 0:
            break
    print(f"You walked away with {balance}€. Have a nice day!")
  
if __name__ == "__main__":
    main()