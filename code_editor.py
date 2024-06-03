import tkinter 
from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog


def submit():
    file= filedialog.asksaveasfile(initialdir="c:\\Users\\ATIF TRADERS\\PycharmProjects\\pythonProject2",
                                   defaultextension=".py",
                                   filetypes= [
                                       ("Text file", ".txt"),
                                       ("HTML",".html"),
                                       ("all files", ".*"),
                                       ("python file", ".py")
                                   ])
    if file:

            content = text_scroll1.get("1.0", "end-1c")  # Get all content
            file.write(content + '\n')
    if file is None:
        return #it will prevent error
root= tkinter.Tk()
root.config(background='sky blue')
root.title("YouCode: An app of innovation")
def next_ques():
    new_window= Tk()
    # independent and does not get close when old window get closed
    root.destroy()#close out the old window


app_header= tkinter.Label(root,
                          text= "YOU CODE: Code Editor",
                          bg="pink",
                          fg="black",
                          bd=10,
                          relief=RAISED,
                          font= ("Georgia", 24))
app_header.pack()
ques= tkinter.Label(root,
                    text= "Edit any code snippet,project or any task.",
                    font= ("Georgia", 26),
                    bd=10,
                    relief=RAISED,
                    fg="black",
                    bg="pink")
ques.pack()
text_scroll1= scrolledtext.ScrolledText(root,
                                        wrap= tkinter.WORD,
                                        height=10,
                                        font=('arial',21),
                                        fg="brown",
                                        bg="sky blue")
text_scroll1.pack(fill= tkinter.BOTH, expand= True)
text_scroll2= scrolledtext.ScrolledText(root,
                                        wrap= tkinter.WORD,
                                        height= 10,
                                        font=('arial',21),
                                        fg="brown",
                                        bg="sky blue",
                                        state= tkinter.DISABLED)
text_scroll2.pack(fill= tkinter.BOTH, expand= True)
# button for submission
# Dphoto= PhotoImage(file= "upload.png")
submit_button =Button(text_scroll2,
               text= "Save",
               command= submit, #call back the function don't use ()
               font= ("Comic Sans", 12),#font and its size
               fg= "green",  #text color
               bg= "white", #background color
               activeforeground="green", #there is a foreground that's exhibited when the text is being pressed. let's make it green too
               activebackground="white",
               state=ACTIVE) #IT ALLOWS USER TO CLICK ON THIS BUTTON BUT CAN BE DISABLED USING state= DISABLED)
               # image= Dphoto, #display image on button
               # compound= 'left')

submit_button.pack()
# Button for next window
# Cphoto= PhotoImage(file= "check-list.png")
next_button =Button(text_scroll2,
               text= "Open File",
               command= next_ques, #call back the function don't use ()
               font= ("Comic Sans", 12),#font and its size
               fg= "green",  #text color
               bg= "white", #background color
               activeforeground="green", #there is a foreground that's exhibited when the text is being pressed. let's make it green too
               activebackground="white",
               state=ACTIVE,  #IT ALLOWS USER TO CLICK ON THIS BUTTON BUT CAN BE DISABLED USING state= DISABLED)
               # image= Cphoto, #display image on button
               compound= 'left')

next_button.pack()
root.mainloop()
# concepts:
# wrap: when i write a long  word it should not split in lines but instead should entirely move to  next line
