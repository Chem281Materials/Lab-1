import tkinter as tk
import random

class PuzzleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tile Puzzle Game")

        self.tiles = list(range(1, 9)) + [None]
        random.shuffle(self.tiles)

        self.buttons = []
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        # Move counter
        self.moves = 0
        self.move_label = tk.Label(self.root, text=f"Moves: {self.moves}", font=("Helvetica", 12))
        self.move_label.pack(pady=5)
        # Reset button
        self.reset_button = tk.Button(self.root, text="Reset Puzzle", command=self.reset_board)
        self.reset_button.pack(pady=10)

        self.draw_board()

    def draw_board(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                index = i * 3 + j
                value = self.tiles[index]
                if value is None:
                    btn = tk.Button(self.frame, text=" ", width=6, height=3,
                                    state="disabled", bg="lightgray")
                else:
                    btn = tk.Button(self.frame, text=str(value), width=6, height=3,
                                    command=lambda idx=index: self.move_tile(idx))
                btn.grid(row=i, column=j)
                row.append(btn)
            self.buttons.append(row)

    def update_move_label(self):
        self.move_label.config(text=f"Moves: {self.moves}")

    def reset_board(self):
        self.tiles = list(range(1, 9)) + [None]
        random.shuffle(self.tiles)
        self.draw_board()

    def move_tile(self, index):
        blank_index = self.tiles.index(None)
        if self.is_adjacent(index, blank_index):
            self.tiles[blank_index], self.tiles[index] = self.tiles[index], self.tiles[blank_index]
            self.draw_board()
            self.moves += 1
            self.update_move_label()
            if self.is_solved():
                self.show_victory()

    def is_adjacent(self, i1, i2):
        row1, col1 = divmod(i1, 3)
        row2, col2 = divmod(i2, 3)
        return abs(row1 - row2) <= 1 and abs(col1 - col2) <= 1

    def is_solved(self):
        return self.tiles == list(range(1, 9))

    def show_victory(self):
        victory = tk.Toplevel(self.root)
        victory.title("Victory!")
        tk.Label(victory, text="You solved it!").pack(padx=20, pady=20)
        tk.Button(victory, text="Close", command=victory.destroy).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    game = PuzzleGame(root)
    root.mainloop()
