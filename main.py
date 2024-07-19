from tkinter import *
from tkinter import messagebox
import base64
import os



#colors and fonts
bg_color = "#fff"
button_color = "#38a3a5"
button_hover = "green"
button_active = "#2C3E50"
button_font = ("Arial", 12)
button_font_color = "#ECF0F1"
label_font = ("Arial", 12)
label_font_color = "#22577a"

# def on_enter(e, button):
#     button['background'] = button_hover  

# def on_leave(e, button):
#     button['background'] = button_color  

def encrypt(code, text1, text2, screen):
    password=code.get()

    if password=="123456":
        crpt_screen=Toplevel(screen)
        crpt_screen.geometry("400x300")
        crpt_screen.title("Encrypt")
        crpt_screen.configure(bg="#fff")

        message=text1.get(1.0, END)
        message_encoded=message.encode("ascii")
        base64_bytes=base64.b64encode(message_encoded)   
        encrypted_message=base64_bytes.decode("ascii")

        encrypt_label=Label(crpt_screen, text="Encrypted message", bg=bg_color, fg="black", font="Arial 15")
        encrypt_label.place(x=10, y=10)
        text2=Text(crpt_screen, font="Arial 15", bg="#fbc3bc", fg="black", bd=0, wrap=WORD, relief=GROOVE )
        text2.place(x=10, y=40, width=380, height=200)
        text2.insert(END, encrypted_message)
    elif password=="":
        messagebox.showerror("Error", "Please enter a key")
    elif password!="123456":
        messagebox.showerror("Error", "Wrong key")  


def decrypt(code, text1, text2, screen):
    password=code.get()

    if password=="123456":
        dcrpt_screen=Toplevel(screen)
        dcrpt_screen.geometry("400x300")
        dcrpt_screen.title("Decrypt")
        dcrpt_screen.configure(bg="#fff")

        message=text1.get(1.0, END)
        message_decoded=message.encode("ascii")
        base64_bytes=base64.b64decode(message_decoded)   
        decrypted_message=base64_bytes.decode("ascii")

        decrypt_label=Label(dcrpt_screen, text="Decrypted message", bg=bg_color, fg="black", font="Arial 15")
        decrypt_label.place(x=10, y=10)
        text2=Text(dcrpt_screen, font="Arial 15", bg="#b7e4c7", fg="black", bd=0, wrap=WORD, relief=GROOVE )
        text2.place(x=10, y=40, width=380, height=200)
        text2.insert(END, decrypted_message)
    elif password=="":
        messagebox.showerror("Error", "Please enter a key")
    elif password!="123456":
        messagebox.showerror("Error", "Wrong key")


def reset(code, text1):
    code.set("")
    text1.delete(1.0, END)


def main_screen():

    screen=Tk()
    screen.geometry("550x380")
    screen.title("MySecrets")
    screen.configure(bg=bg_color)
    screen.resizable(False, False)

    phrase1_label=Label(screen, text="Enter your message", bg=bg_color, fg=label_font_color, font=label_font)
    phrase1_label.place(x=10, y=10)
    text1=Text(screen,font="Robote 20", bg="#d5d0cd", fg="black", bd=0 , wrap=WORD, relief=GROOVE)
    text1.place(x=10, y=40, width=280, height=250)

    phrase2_label=Label(screen, text="Enter your key", bg=bg_color, fg=label_font_color, font=label_font)   
    phrase2_label.place(x=350, y=70)

    code = StringVar()

    keybox=Entry(screen, textvariable=code,font="Arial 25", bg="#d5d0cd", fg="black", bd=0, relief=GROOVE , show="*")
    keybox.place(x=350, y=100, width=180, height=40)


    button1=Button(screen, text="ENCRYPT", font=button_font, bg="#f07167", fg="#fff",  relief=FLAT , command=lambda: encrypt(code, text1, None, screen)  )
    button1.place(x=350, y=150, width=180, height=40)
    # button1.bind("<Enter>", lambda e: on_enter(e, button1))
    # button1.bind("<Leave>", lambda e: on_leave(e, button1))

    button2=Button(screen, text="DECRYPT", font=button_font, bg="#57cc99", fg="#fff", relief=FLAT , command=lambda: decrypt(code, text1, None, screen)  )
    button2.place(x=350, y=200, width=180, height=40)
    # button2.bind("<Enter>", lambda e: on_enter(e, button2))
    # button2.bind("<Leave>", lambda e: on_leave(e, button2))

    button3=Button(screen,text="RESET"  , font=button_font, bg=button_color, fg=button_font_color, relief=FLAT , command=lambda: reset(code ,text1) )
    button3.place(x=10, y=320, width=530, height=40)
    # button3.bind("<Enter>", lambda e: on_enter(e, button3))
    # button3.bind("<Leave>", lambda e: on_leave(e, button3))

    screen.mainloop()



main_screen()


