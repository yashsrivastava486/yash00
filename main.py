import tkinter as tk
import time
from threading import Timer

# Function to switch to the second window
def switch_to_continue_window():
    welcome_window.withdraw()
    continue_window.deiconify()

# Function to switch to the third window
def switch_to_tic_tac_toe():
    continue_window.withdraw()
    tic_tac_toe_window.deiconify()

# Function to create the Tic Tac Toe game
def create_tic_tac_toe_game():
    for i in range(3):
        for j in range(3):
            button = tk.Button(tic_tac_toe_window, text='', font='normal 20 bold', height=3, width=6,
                               command=lambda row=i, col=j: on_button_click(row, col))
            button.grid(row=i, column=j)
            buttons[i][j] = button

def on_button_click(row, col):
    global current_player, game_over
    if buttons[row][col]['text'] == '' and not game_over:
        buttons[row][col]['text'] = current_player
        if check_winner():
            game_status['text'] = f'Player {current_player} wins!'
            game_over = True
        elif all(buttons[i][j]['text'] != '' for i in range(3) for j in range(3)):
            game_status['text'] = 'Draw!'
            game_over = True
        else:
            current_player = 'O' if current_player == 'X' else 'X'
            game_status['text'] = f"Player {current_player}'s turn"

def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != '':
            return True
    for col in range(3):
        if buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] != '':
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        return True
    return False

# Initialize the first window
welcome_window = tk.Tk()
welcome_window.title("Welcome")
tk.Label(welcome_window, text="Welcome to My App", font=('Helvetica', 20)).pack(pady=50)

# Schedule to switch to the second window after 4 seconds
welcome_timer = Timer(4.0, switch_to_continue_window)
welcome_timer.start()

# Initialize the second window
continue_window = tk.Toplevel()
continue_window.title("Continue")
continue_window.withdraw()  # Hide the window initially
tk.Label(continue_window, text="Click 'Continue' to proceed", font=('Helvetica', 20)).pack(pady=50)
tk.Button(continue_window, text="Continue", command=switch_to_tic_tac_toe).pack()

# Initialize the third window (Tic Tac Toe game)
tic_tac_toe_window = tk.Toplevel()
tic_tac_toe_window.title("Tic Tac Toe")
tic_tac_toe_window.withdraw()  # Hide the window initially

# Create Tic Tac Toe grid and game status
buttons = [[None for _ in range(3)] for _ in range(3)]
game_status = tk.Label(tic_tac_toe_window, text="Player X's turn", font=('Helvetica', 20))
game_status.grid(row=3, column=0, columnspan=3)
current_player = 'X'
game_over = False
create_tic_tac_toe_game()

# Run the main event loop
welcome_window.mainloop()
