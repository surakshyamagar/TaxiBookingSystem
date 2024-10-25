from tkinter import *
from PIL import Image, ImageTk

class Dashboard:
    def __init__(self, window):
        self.window = window
        self.window.title('Taxi Booking System')
        self.window.geometry("1366x768")
        self.window.state('zoomed')

        self.header = Frame(self.window, bg='#009df4')
        self.header.place(x=300, y=15, width=910, height=50)

        # Correcting the assignment of font attributes
        # self.header.configure(bg="skyblue")
        

        # Add a label for the system name in the header
        system_name_label = Label(self.header, text='Taxi Booking System', font=("", 22, "bold"), bg='#009df4', fg='black')
        system_name_label.place(x=300, y=5)

        # self.header = Frame(self.window, bg='#009df4')
        self.header.place(x=300, y=15, width=905, height=120)

        self.logout_text = Button(self.window, text='LOG OUT', bg='#32cf8e', font=("", 13, "bold"), bd=1, fg='black', cursor='hand2', activebackground='#32cf8e')
        self.logout_text.place(x=1110, y=27)

        self.Dashboard_text = Button(self.window, text='Dashboard', bg='#32cf8e', font=("", 13, "bold"), bd=1, fg='black', cursor='hand2', activebackground='#32cf8e')
        self.Dashboard_text.place(x=300, y=26)

        self.image_frame()
        self.driver_info_frame()

    def image_frame(self):
        self.window.configure(bg="white")

        image_path1 = r"C:\Users\renum\OneDrive\Desktop\r.jpg"
        background_image1 = Image.open(image_path1)
        background_image1 = background_image1.resize((260, 260))

        circular_image1= Image.new('RGBA', (267, 245), (0, 0, 0, 0))
        circular_image1.paste(background_image1, (10, 10))

        circular_photo1 = ImageTk.PhotoImage(circular_image1)

        background_label1 = Label(self.window, image=circular_photo1, background='white')
        background_label1.image = circular_photo1
        background_label1.place(x=29, y=2)

        # Second Image
        image_path2 = r"C:\Users\renum\OneDrive\Desktop\er.jpeg"  # Add the path to your second image
        background_image2 = Image.open(image_path2)
        background_image2 = background_image2.resize((900, 700))

        circular_image2 = Image.new('RGBA', (8000, 7094), (0, 0, 0, 0))
        circular_image2.paste(background_image2, (10, 10))

        circular_photo2 = ImageTk.PhotoImage(circular_image2)

        background_label2 = Label(self.window, image=circular_photo2, background='white')
        background_label2.image = circular_photo2
        background_label2.place(x=293, y=60)  # Adjust the x-coordinate as needed

        #  # third Image
        
        # image_path3 = r"C:\Users\renum\OneDrive\Desktop\r.jpg"  
        # background_image3 = Image.open(image_path3)
        # background_image3 = background_image3.resize((40, 40))
        # self.photo3 = ImageTk. PhotoImage(background_image3)

        # self.background_label3 = Label(self.image_frame, image=self.photo3, bg='lightblue')
        # self.background_label3.image = self.photo3
        # self.background_label3.place(x=10, y=210)

        # # circular_image3 = Image.new('RGBA', (8000, 7094), (0, 0, 0, 0))
        # circular_image3.paste(background_image3, (10, 10))

        # circular_photo3 = ImageTk.PhotoImage(circular_image3)

        # background_label3 = Label(self.window, image=circular_photo3)
        # background_label3.image = circular_photo3
        # background_label3.place(x=123, y=60)

    def driver_info_frame(self):
        # Create a new frame for driver information
        driver_info_frame = Frame(self.window, bg='green')
        driver_info_frame.place(x=42, y=250, width=257, height=522)

        # # Display driver information in the new frame
        self.driver_name_label = Button(driver_info_frame, text="Driver Name: John Doe", font=("Arial", 14), bg="lightgreen", fg="black")
        self.driver_name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.driver_name_label.place(x=10, y=55)


        self.driver_History = Button(driver_info_frame, text="Driver History", font=("Arial", 14), bg="skyblue", fg="black")
        self.driver_History.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.driver_History.place(x=10, y=110)


        self.driver_id_label = Button(driver_info_frame, text="Driver ID: 12345", font=("Arial", 14), bg="lightgreen", fg="black")
        self.driver_id_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.driver_id_label.place(x=10, y=162)


        self.manage_profile = Button(driver_info_frame, text="manage profile", font=("Arial", 14), bg="skyblue", fg="black")
        self.manage_profile.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.manage_profile.place(x=10, y=215)


        self.exit_text=Button(self.window, text='exit',bg= '#32cf8e', font=("", 13, "bold"), bd=1, fg='black', cursor='hand2', activebackground='#32cf8e')
        self.exit_text.place(x=250, y=730)

        
        # self.manage_profile=Button(self.window, text='Manage profile' ,bg='#32cf8e', font = ("", 13, "bold"), bd=1, fg='Black',cursor='hand2', activebackground='#32cf8e')
        # self.manage_profile.place(x=10, y=390)




if __name__ == "__main__":
    window = Tk()
    dashboard = Dashboard(window)
    window.mainloop()