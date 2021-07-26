from tkinter import * 
from PIL import ImageTk, Image

root = Tk()

# defining the images 
kid_age = ImageTk.PhotoImage(Image.open("kid_age.jpeg"))
teenager_age = ImageTk.PhotoImage(Image.open("teenager_age.jpeg"))
adult_age = ImageTk.PhotoImage(Image.open("adult_age.jpeg"))
old_age = ImageTk.PhotoImage(Image.open("old_age.jpeg"))

kid_photo = Label(root, image=kid_age)
teenager_photo = Label(root, image=teenager_age)
adult_photo = Label(root, image=adult_age)
old_photo = Label(root, image=old_age)

# defining the function 

def born_year():
    user_year = int(age.get())
    current_year = 2021

    result = current_year - user_year
    
   
    my_label = Label(root, text=f"You are {result} years old")
    my_label.pack()

    if result > 3 and result < 11:
        kid_label = Label(root, text="You are a kid:")
        kid_label.pack()
        kid_photo.pack()
        
    if result > 11 and result < 20: 
        teenager_label = Label(root, text="You are a teenager:")
        teenager_label.pack()
        teenager_photo.pack()

    if result > 20 and result < 45:
        adult_label = Label(root, text="You are an adult:") 
        adult_label.pack()
        adult_photo.pack()

    if result > 45: 
        old_label = Label(root, text="You are old:")
        old_label.pack()
        old_photo.pack()

# Geting the user input

age = Entry(root)
age.pack()

my_label = Button(root, text="Click me",command=born_year)
my_label.pack()



root.mainloop()