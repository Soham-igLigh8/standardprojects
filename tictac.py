import tkinter as tk
"""import tkinter.messagebox as msgbox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")

        self.current_player = "X"
        self.board = [["", "", ""] for _ in range(3)]
        self.buttons = []

        self.create_board()

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window, text="", width=10, height=5, 
                                   command=lambda row=i, col=j: self.on_click(row, col))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def on_click(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.check_winner():
                msgbox.showinfo("Game Over lavde lag gaye ", f"{self.current_player} wins maa chudao!")
                self.reset_game()
            elif self.check_draw():
                msgbox.showinfo("Game Over", "It's a draw!jhoome jo pathan")
                self.reset_game()
            else:
                self.switch_player()

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        for row in self.board:
            if all(cell == self.current_player for cell in row):
                return True
        for col in range(3):
            if all(self.board[row][col] == self.current_player for row in range(3)):
                return True
        if (self.board[0][0] == self.current_player and self.board[1][1] == self.current_player and self.board[2][2] == self.current_player) or \
           (self.board[0][2] == self.current_player and self.board[1][1] == self.current_player and self.board[2][0] == self.current_player):
            return True

        return False

    def check_draw(self):
        return all(cell != "" for row in self.board for cell in row)

    def reset_game(self):
        self.current_player = "X"
        self.board = [["", "", ""] for _ in range(3)]
        for row in self.buttons:
            for button in row:
                button.config(text="")

game = TicTacToe()
game.window.mainloop()"""