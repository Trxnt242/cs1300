Problem 1

principal = float(input("Principal: "))
rate = float(input("Rate (%): "))
years = int(input("Years: "))

balance = principal

for year in range(1, years + 1):
    balance = balance * (1 + rate /100)
    print(f"Year {year}: $(balance:.2f}")

total_interest = balance - principal
print(f"Total interest earned: ${total_interest:.2f}")

Problem 2

def caeasar_encode(text, shift):
    result = ""

    for ch in text:
        if ch.islower():
            new_char = chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
            result += new_char
        elif ch.isupper():
            new_char = chr((ord(ch) - ord('A') + shift) % 26 + ord('A')
            result+= new_char
        else:
            result += ch

   return result


# Test cases
print(ceasar_encode("Hello, World!", 3))   #Khoor, Zroug!"
print(ceasar_encode("abc xyz", 2))          # "cde zab"
print(ceasar_encode("Python 3", 5))         # "Udymts 3"



Problem 5

def main():
    descriptions = []
    amounts = []

    while True:
        print("\n1. Add expense")
        print("2. View all expenses")
        print("3. Total spent")
        print("4. Largest expense")
        print("5. Remove expense (by number)")
        print("6. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(descriptions, amounts)
        elif choice == "2":
            view_expenses(descriptions, amounts)
        elif choice == "3":
            total_spent(amounts)
        elif choice == "4":
            largest_expense(descriptions, amounts)
        elif choice == "5":
            remove_expense(descriptions, amounts)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


def add_expense(descriptions, amounts):
    desc = input("Enter description: ")
    try:
        amt = float(input("Enter amount: "))
        if amt < 0:
            print("Amount must be non-negative.")
            return
        descriptions.append(desc)
        amounts.append(amt)
    except ValueError:
        print("Invalid amount.")


def view_expenses(descriptions, amounts):
    if not descriptions:
        print("No expenses recorded.")
        return

    for i in range(len(descriptions)):
        print(f"{i+1}. {descriptions[i]}: ${amounts[i]:.2f}")


def total_spent(amounts):
    total = sum(amounts)
    print(f"Total: ${total:.2f}")


def largest_expense(descriptions, amounts):
    if not amounts:
        print("No expenses to compare.")
        return

    max_amt = max(amounts)
    index = amounts.index(max_amt)
    print(f"Largest: {descriptions[index]} (${max_amt:.2f})")


def remove_expense(descriptions, amounts):
    if not descriptions:
        print("No expenses to remove.")
        return

    try:
        num = int(input("Enter expense number to remove: "))
        if 1 <= num <= len(descriptions):
            descriptions.pop(num - 1)
            amounts.pop(num - 1)
        else:
            print("Invalid number.")
    except ValueError:
        print("Invalid number.")


# Run program
main()

Problem 3

def transpose(matrix):
    result = []
    
    # Loop through columns
    for col in range(len(matrix[0])):
        new_row = []
        
        # Loop through rows
        for row in range(len(matrix)):
            new_row.append(matrix[row][col])
        
        result.append(new_row)
    
    return result


# TEST CASES
m1 = [[1, 2, 3],
      [4, 5, 6]]

print(transpose(m1))
# Expected: [[1, 4], [2, 5], [3, 6]]

m2 = [[1, 2],
      [3, 4],
      [5, 6]]

print(transpose(m2))
# Expected: [[1, 3, 5], [2, 4, 6]]


Problem 4

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    
    # Check for empty spaces
    for row in board:
        if " " in row:
            return "Ongoing"
    
    # If no winner and no spaces
    return "Draw"


# TEST CASES
board1 = [["X", "X", "X"],
          ["O", "O", " "],
          [" ", " ", " "]]

print(check_winner(board1))  # X

board2 = [["X", "O", "X"],
          ["X", "O", " "],
          [" ", "O", "X"]]

print(check_winner(board2))  # O

board3 = [["X", "O", "X"],
          ["X", "O", "O"],
          ["O", "X", "X"]]

print(check_winner(board3))  # Draw

board4 = [["X", "O", " "],
          [" ", "X", " "],
          ["O", " ", " "]]

print(check_winner(board4))  # Ongoing
   
