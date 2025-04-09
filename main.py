import tkinter as tk

# --- Constants ---
WINDOW_TITLE = "Center Finder"
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 400
CANVAS_BG = "white"
DOT_COLOR = "blue"
DOT_RADIUS = 4 # The radius for the oval representing the dot
CENTER_COLOR = "red"
CENTER_X_SIZE = 6 # Half the length of the lines forming the 'X'

class CenterFinderApp:
    """
    An interactive application to place dots on a canvas and find their center.
    """
    def __init__(self, master):
        """
        Initialize the application.
        Args:
            master: The root tkinter window.
        """
        self.master = master
        self.master.title(WINDOW_TITLE)
        # Prevent resizing which might complicate coordinates if not handled
        self.master.resizable(False, False)

        self.dots = [] # List to store (x, y) coordinates of dots
        self.center = None # Stores the calculated center (x, y) or None

        # Create the canvas widget
        self.canvas = tk.Canvas(
            master,
            width=CANVAS_WIDTH,
            height=CANVAS_HEIGHT,
            bg=CANVAS_BG
        )
        self.canvas.pack(pady=10, padx=10) # Add some padding around the canvas

        # Bind the left mouse click event (<Button-1>) on the canvas
        self.canvas.bind("<Button-1>", self.handle_click)

        # Initial draw (empty canvas)
        self.redraw_canvas()

        print("Center Finder Application Started.")
        print("Click on the white canvas to place blue dots.")
        print("A red 'X' will mark the center of all placed dots.")


    def handle_click(self, event):
        """
        Callback function executed when the canvas is clicked.
        Args:
            event: The tkinter event object containing click details (event.x, event.y).
        """
        x, y = event.x, event.y
        print(f"Dot placed at: ({x}, {y})")
        self.dots.append((x, y))
        self.calculate_center()
        self.redraw_canvas()

    def calculate_center(self):
        """
        Calculates the geometric center (centroid) of all placed dots.
        Updates the self.center attribute.
        """
        num_dots = len(self.dots)
        if num_dots == 0:
            self.center = None # No center if no dots
            return

        sum_x = 0
        sum_y = 0
        for x, y in self.dots:
            sum_x += x
            sum_y += y

        center_x = sum_x / num_dots
        center_y = sum_y / num_dots
        self.center = (center_x, center_y)
        print(f"Calculated center at: ({center_x:.2f}, {center_y:.2f})")

    def redraw_canvas(self):
        """
        Clears the canvas and redraws all dots and the center 'X'.
        """
        # Clear the entire canvas
        self.canvas.delete("all")

        # Draw all the blue dots
        for x, y in self.dots:
            # Calculate bounding box for the oval
            x1 = x - DOT_RADIUS
            y1 = y - DOT_RADIUS
            x2 = x + DOT_RADIUS
            y2 = y + DOT_RADIUS
            self.canvas.create_oval(x1, y1, x2, y2, fill=DOT_COLOR, outline=DOT_COLOR)

        # Draw the red center 'X' if it exists
        if self.center:
            cx, cy = self.center
            # Draw the two lines forming the 'X'
            self.canvas.create_line(
                cx - CENTER_X_SIZE, cy - CENTER_X_SIZE,
                cx + CENTER_X_SIZE, cy + CENTER_X_SIZE,
                fill=CENTER_COLOR, width=2 # width controls line thickness
            )
            self.canvas.create_line(
                cx - CENTER_X_SIZE, cy + CENTER_X_SIZE,
                cx + CENTER_X_SIZE, cy - CENTER_X_SIZE,
                fill=CENTER_COLOR, width=2
            )

# --- Main Execution ---
if __name__ == "__main__":
    root = tk.Tk() # Create the main application window
    app = CenterFinderApp(root) # Instantiate our application class
    root.mainloop() # Start the tkinter event loop