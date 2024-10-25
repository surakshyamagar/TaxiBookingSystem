import tkinter as tk
from PIL import Image, ImageTk
from tkinter import Frame
from register import Registraion
from tkinter import messagebox
from customerdashboard import CustomerGUI


# wimdow=tk

class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x600+200+100")
        self.root.title("Login form")
       

       # # Create a frame for the entire registration page
        self.registration_frame_container = tk.Frame(self.root, bg="lightgreen")
        self.registration_frame_container.pack(expand=True, fill="both")


    #  sidebar
        self.sidebar=Frame(self.root)
        self.sidebar.place(x=45, y=50, width=750, height=600)

        


        # Call the method to create widgets
        self.image = Image.open(r"C:\Users\renum\OneDrive\Desktop\nice.jpeg")
        self.photo = ImageTk.PhotoImage(self.image)
        image_label = tk.Label(self.root, image=self.photo)
        image_label.place(x=40, y=50, width="345", height="600")


        # Username entry
        label_username = tk.Label(self.root, text="Username:", font=("Arial",15, "bold"))
        label_username.place(x=420, y=150)
        self.entry_username = tk.Entry(self.root, font=("Arial",15, "bold"))
        self.entry_username.place(x=540, y=150)

        # Password entry
        label_password = tk.Label(self.root, text="Password:", font=("Arial",15, "bold"))
        label_password.place(x=420, y=200)
        self.entry_password = tk.Entry(self.root, font=("Arial",15, "bold"))
        self.entry_password.place(x=540, y=200)

        # Login button
        login_button = tk.Button(self.root, text="Login",width=10, command=self.login,font=("Arial",15, "bold" ), bg="lightblue")
        login_button.place(x=520, y=300)

        # Register button (assuming you have the open_register_page function)
        register_button = tk.Button(self.root, text="Register",width=12, command=self.open_register_page,font=("Arial",15, "bold"), bg="lightblue")
        register_button.place(x=519, y=350)


    def open_register_page(self):
                # Define the function or code to open the register page here
            
            self.root.destroy()
            regsiter =tk. Tk()
            Registraion(regsiter)
            regsiter.mainloop()


    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        
        if username == "admin" and password== "pass":
             messagebox.showinfo("Success","Login Successfull")

             app = tk.Tk()
             CustomerGUI(app)
             app.mainloop()

    

if __name__ == "__main__":
    root = tk.Tk()  # Fix the syntax error here
    app = Login(root)
    root.mainloop()
