from tkinter import *



""" create tkinter window and size + name student """

root = Tk()
root.geometry("800x600+30+30") 
root.resizable(width=FALSE, height=FALSE)
root.title("Artium kot")



""" create background image """

filename = PhotoImage(file ="b.gif")
background_label = Label(root,image=filename)
background_label.place(x=0,y=0,relwidth=1,relheight=1)



  
""" show the information this program """

def info():
     lbl1.delete(0.0,END)
     lbl1.insert(END,"\tHey! The program is designed to show the user the amount of+"
                   "words he has typed in the initial input.Pleasant use :)!")




""" close the program """

def close():
    root.destroy()
    



""" count words + letters + space,from to show all data this input + check if have input or not """

def charcount():
    w = input_word.get()
    
    char=0
    word=1
    
    for i in w:

        if i!=' ':      
         char=char+1
        
        if i==' ':
         word=word+1


    if word==1 and char==0:
        lbl2.delete(0.0,END)
        lbl2.insert(END,"\t   you don't have nothing! ,please input text")
    else:
        lbl2.delete(0.0,END)
        lbl2.insert(END,"\t  "+
                "you typed " + " words: " + str(word) + " , letters: " + str(char) +
                " , spaces: " + str(word-1))
    



""" count words """

def words():
    w = input_word.get()

    word=1
    
    for i in w:
      
        if(i==' '):
         word=word+1

   
    lbl3.delete(0.0,END)
    lbl3.insert(END,"    Number of words: " + str(word))




""" count letters """

def letters():
    w = input_word.get()

    char=0
    
    for i in w:

        if i!=' ':      
         char=char+1


    lbl3.delete(0.0,END)
    lbl3.insert(END,"    Number of letters: " + str(char))




""" count spaces """

def spaces():
    w = input_word.get()
    
    word=1
    
    for i in w:
      
        if(i==' '):
         word=word+1


    lbl3.delete(0.0,END)
    lbl3.insert(END,"    Numbers of spaces: " + str(word-1))




""" title this program """

Label(root,bg="ForestGreen",fg="white",font="none 20",text="Welcome :)").grid(row=1,column=0,pady=20)




""" show the information + click to button """

btn1 = Button(root,bg="orange",font="none 10",text='Click See Information',command=info).grid(row=3,column=0,pady=10)

lbl1 = Text(root,bg="DarkOliveGreen",fg="white",width=115, height=1,font="none 10")
lbl1.grid(row=5,column=0,pady=10) 



""" input text + click to button for calculate """

Label(root,bg="Wheat",font="none 10",text="please input words here  :\n↓").grid(row=6,column=0,pady=10)

btn2 = Button(root,bg="orange",font="none 10",text='Click See Result', command=charcount).grid(row=8,column=0,pady=10)

input_word = Entry(root,bg="ForestGreen",fg="white",font="none 10",width=50)
input_word.grid(row=7,column=0,pady=10)



""" show result all date with input = count words,space,letters """

lbl2 = Text(root,bg="DarkOliveGreen",fg="white",width=55,height=1,font="none 10")
lbl2.grid(row=10,column=0,pady=10) 




""" here we create listBox + fuction to choice what you need = how much words or letters or spaces """

Label(root,bg="Wheat",font="none 10",text="Here you can search what you need find with your input.\nPlease choose what you need  :").grid(row=11,column=0,pady=10)

list_box = Listbox(root,height=3,width=16,font="none 9",bg="orange")
list_box.insert(0, "  View words count")
list_box.insert(1, "  View letters count")
list_box.insert(2, " View spaces count")
list_box.grid(row=12,column=0)


def list_box_options(item):

    w = item.widget
    index = int(w.curselection()[0])

    if index == 0:
        Button(root,bg="orange",font="none 10",text="Enter",width=8,command=words).grid(row=14,column=0)
    elif index == 1:
        Button(root,bg="orange",font="none 10",text="Enter",width=8,command=letters).grid(row=14,column=0)
    elif index == 2:
        Button(root,bg="orange",font="none 10",text="Enter",width=8,command=spaces).grid(row=14,column=0)


list_box.bind('<<ListboxSelect>>',list_box_options)

lbl3 = Text(root,bg="DarkOliveGreen",fg="white",width=23,height=1,font="none 10")
lbl3.grid(row=13,column=0,pady=10) 



""" click to button for exit this program """

btn3 = Button(root,font="none 10",bg="red",text='Exit',command=close).grid(row=15,column=0,pady=10)


root.mainloop()
