from tkinter import *
import os
import time
from tkinter import filedialog
from pdf2image import convert_from_path
import shutil




def import_file():
    current_location = os.getcwd()
    filename = filedialog.askopenfilename(filetypes=(("PDF Files", "*.pdf"),("All Files", "*.*")))
    if len(filename) != 0:
        keywordEntry.delete(0,END)
        keywordEntry.insert(0, filename)
        #file_name = os.path.basename(filename)
    elif len(filename) <= 0 :
        keywordEntry.delete(0, END)
        mylocation = os.getcwd()
        keywordEntry.insert(END, mylocation)






def coverter():
    try:
        file_name = os.path.basename(keywordEntry.get())
        save_to = filedialog.askdirectory()
        pages = convert_from_path((str(keywordEntry.get())))
        #locationandfilename = save_to+"/"+file_name
        #print(locationandfilename)
        #foldercreated = os.makedirs(locationandfilename)
        #os.makedirs(locationandfilename)
        #totalpages = len(pages)
        #print(totalpages)
        #d = os.getcwd(foldercreated)
        #print(d)
        for i in range(len(pages)):
            os.chdir(str(save_to))
            pages[i].save('page' + str(i) + '.png', 'PNG')
            complete_label = Label(root,font=("Consolas 10") ,bg="#282a36",fg='#FFFFFF', text="Completed").place(x=575, y=100, width=120, height=40)
    except:
        complete_label = Label(root, font=("Consolas 8"), bg="#282a36", fg='#FFFFFF', text="plz add valid PDF file").place(x=550,y=100,width=160,height=40)








def check():
    try:
        pages = convert_from_path((str(keywordEntry.get())))
        totalpages = len(pages)
        if totalpages >=1:
            labelforpages = Label(root,text="Pages: "+str(totalpages) ,font=("Consolas 10") ,fg="white", bg='#282a36')
            labelforpages.place(x=550,y=100,width=120 , height= 40)

        else:
            labelforerror = Label(root, text="ERROR", font=("Consolas 20"), fg="white", bg='#282a36')
    except:
        labelforerror = Label(root, text="Error,Select PDF", font=("Consolas 8"), fg="red", bg='#282a36')
        labelforerror.place(x=575, y=100, width=120, height=40)







def exitit():
    quit()






root = Tk()
root.geometry("700x200")
root.title('Files Converter')
root.resizable(False,False)
root.config(bg = '#282a36')

#root.iconbitmap(r'icon1.png')
#application_icon = PhotoImage(file ='icon.png')
#root.iconphoto(True,application_icon)

#convert_button = PhotoImage(file ='icon.png',height=10, width=20)
#root.iconphoto(True,application_icon)
#quit_button = PhotoImage(file ='quit.png',)
#root.iconphoto(True,application_icon)




keywordEntry = Entry(root, bg="#FFFFFF")
keywordEntry.place(x=30,y=70,width=500)
keywordEntry.delete(0, END)
keywordEntry.insert(END, os.getcwd())
button = Button(root, text="..../", bg="#FFFFFF", command=import_file)
button.place(x=540,y=70,width=30 , height= 20)
button2 = Button(root,text="Convert",bg="#FFFFFF",command=coverter)
button2.place(x=550,y=140,width=120 , height= 40)
button4 = Button(root,text="Check",bg="#FFFFFF",command=check)
button4.place(x=415,y=140,width=120 , height= 40)
button3 = Button(root,text="Quit",bg="#FFFFFF",command=exitit,compound="top")
button3.place(x=280,y=140,width=120 , height= 40)
label2 = Label(root,text="PDF to PNG" ,font=("Consolas 20") ,fg="white", bg='#282a36')
label2.place(x=200,y=20,height=20 , width=200 )



root.mainloop()