import tkinter as tk
from tkinter import ttk

# Constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40

class GridEraserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🖌️ Grid Eraser App")
        self.root.configure(bg="#f0f4f8")

        # Heading
        heading = tk.Label(root, text="🎨 Paint & Erase Grid", font=("Helvetica", 16, "bold"), bg="#f0f4f8")
        heading.pack(pady=10)

        # Canvas Frame
        canvas_frame = tk.Frame(root, bg="#f0f4f8")
        canvas_frame.pack(pady=10)

        # Canvas Widget
        self.canvas = tk.Canvas(canvas_frame, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white", highlightthickness=2, highlightbackground="#888")
        self.canvas.pack()

        # Create grid
        self.grid = self.create_grid()

        # Bind erasing event
        self.canvas.bind("<B1-Motion>", self.erase)

        # Footer Label
        footer = tk.Label(root, text="Hold Left Mouse Button to Erase Cells", font=("Arial", 10), bg="#f0f4f8", fg="#555")
        footer.pack(pady=5)

    def create_grid(self):
        """Creates a grid of purple cells on the canvas."""
        cells = []
        for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
            row_cells = []
            for col in range(0, CANVAS_WIDTH, CELL_SIZE):
                rect = self.canvas.create_rectangle(
                    col, row, col + CELL_SIZE, row + CELL_SIZE,
                    fill="#b366ff", outline="black"  # Purple shade
                )
                row_cells.append(rect)
            cells.append(row_cells)
        return cells

    def erase(self, event):
        """Erases a cell by changing its color to white."""
        x, y = event.x, event.y
        row = y // CELL_SIZE
        col = x // CELL_SIZE

        if 0 <= row < len(self.grid) and 0 <= col < len(self.grid[0]):
            self.canvas.itemconfig(self.grid[row][col], fill="white")

def main():
    root = tk.Tk()
    app = GridEraserApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
