import tkinter as tk

class CustomerGUI():

    def __init__(self, root):
        self.root = root
        self.root.state("zoomed")




if __name__ == "__main__":
    root = tk.Tk()
    CustomerGUI(root)
    root.mainloop()