from tkinter import *
from tkinter import ttk
import random
import time

class Game_Setup():
    def __init__(self,widget):
        self.widget = widget
        with open("oop_hangman.txt", "r") as file:
            extract = file.read()
            self.words = list(map(str, extract.split()))
            self.word = random.choice(self.words)
        self.List_Creator(self.word)
        
    def List_Creator(self,value):
        self.wordlist = []
        self.answerlist = []
        self.usedletters = []
        self.lives = 6
        for i in value:
            self.wordlist.append(i)
            self.answerlist.append('_')
        self.Print_Gui()
    
    def Print_Gui(self):
        self.widget.config(state= "normal")
        self.widget.delete('1.0', END)
        self.widget.tag_configure("center", justify='center')
        for i in self.answerlist:
            self.widget.insert(END,i)
            self.widget.insert(END,' ')
        self.widget.tag_add("center", "1.0", "end")
        self.widget.config(state= "disabled")
        entry.delete(0, END)

class Game_Functions(Game_Setup):
    def __init__(self,widget):
        super().__init__(widget)
    def Scan(self,letter):
        self.letter = letter
        if letter in self.usedletters:
            self.Used_Letter()
        elif letter in self.wordlist:
            self.usedletters.append(letter)
            for i in range(len(self.wordlist)):
                if letter == self.wordlist[i]:
                    self.answerlist[i]=letter
                    self.Print_Gui()
        else:
            self.usedletters.append(letter)
            self.lives -= 1
            self.Incorrect()
            if self.lives < 0:
                self.Lost()
        if self.answerlist == self.wordlist:
            print(self.answerlist == self.wordlist)
            self.Win()

    def Incorrect(self):
        incorrect_window=Toplevel(root)
        incorrect_window.geometry("350x100")
        incorrect_window.title("Hangman by Rish")
        message = Label(incorrect_window,text=f'Ooops! {self.letter} is not what we are looking for!')
        message1 = Label(incorrect_window, text = f'The letters that you have already used are:')
        message2 = Label(incorrect_window,text = self.usedletters)
        message3 = Label(incorrect_window, text = f'The amount of lives that you have left are: {self.lives}')
        message.config(font=('Mclaren Bespoke Bold',10))
        message1.config(font=('Mclaren Bespoke',8))
        message2.config(font=('Mclaren Bespoke',8))
        message3.config(font=('Mclaren Bespoke',8))
        message.pack()
        message1.pack()
        message2.pack()
        message3.pack()

    def Used_Letter(self):
        usedletter_window=Toplevel(root)
        usedletter_window.geometry("350x100")
        usedletter_window.title("Hangman by Rish")
        message = Label(usedletter_window,text=f'Ooops! You have already used the letter: {self.letter}')
        message1 = Label(usedletter_window, text = f'The letters that you have already used are:')
        message2 = Label(usedletter_window,text = self.usedletters)
        message3 = Label(usedletter_window, text = f'The amount of lives that you have left are: {self.lives}')
        message.config(font=('Mclaren Bespoke Bold',10))
        message1.config(font=('Mclaren Bespoke',8))
        message2.config(font=('Mclaren Bespoke',8))
        message3.config(font=('Mclaren Bespoke',8))
        message.pack()
        message1.pack()
        message2.pack()
        message3.pack()

    def Information(self):
        info_window=Toplevel(root)
        info_window.geometry("350x120")
        info_window.title("Hangman by Rish")
        message = Label(info_window,text = "Game Information")
        message1 = Label(info_window, text = f"You have currently used the following letters:")
        if len(self.usedletters) == 0:
            letters = Label(info_window,text = 'None')
        else:   
            letters = Label(info_window,text=self.usedletters)
        message2 = Label(info_window,text=f"You have {self.lives} lives left.")
        message.config(font=('Mclaren Bespoke Bold',14))
        message1.config(font=('Mclaren Bespoke',10))
        letters.config(font=('Mclaren Bespoke',10))
        message2.config(font=('Mclaren Bespoke',10))
        message.pack()
        message1.pack()
        letters.pack()
        message2.pack()

    def Win(self):
        win_window=Toplevel(root)
        win_window.geometry("350x100")
        win_window.title("Hangman by Rish")
        message = Label(win_window,text = "Congratulations you have won!")
        message1 = Label(win_window, text = f"With {self.lives} lives left to spare!")
        message.config(font=('Mclaren Bespoke Bold',12))
        message1.config(font=('Mclaren Bespoke',12))
        message.pack()
        message1.pack()
        start = Game_Functions(self.widget)
    
    def Lost(self):
        lost_window=Toplevel(root)
        lost_window.geometry("350x120")
        lost_window.title("Hangman by Rish")
        message = Label(lost_window,text = "Unfortunately you have lost")
        message1 = Label(lost_window, text = "You have run out of lives")
        message2 = Label(lost_window,text = "The word you were looking for was:")
        word = Label(lost_window,text = self.word)
        message.config(font=('Mclaren Bespoke Bold',14))
        message1.config(font=('Mclaren Bespoke',10))
        message2.config(font=('Mclaren Bespoke',10))
        word.config(font=('Mclaren Bespoke Bold',12))
        message.pack()
        message1.pack()
        message2.pack()
        word.pack()
        start = Game_Functions(self.widget)
        
root = Tk()

root.title('Hangman by Rish')

title = ttk.Label(root,text = "Hangman")
title.config(font=('McLaren Bespoke Bold',24))

guess = Text(root,width=25, height=1)
guess.config(font=('McLaren Bespoke',20))

label = Label(root,text="Please enter a letter to begin guessing the word: ")
label.config(font=('Mclaren Bespoke',12))

entry = ttk.Entry(root,width=10)

submit = ttk.Button(root,text="Submit",command= lambda: start.Scan(entry.get()))

information = ttk.Button(root,text="i",width = 2,command= lambda: start.Information())

title.grid(row=0,column=0,columnspan=2,pady=10)
information.grid(row=0,column=1)
guess.grid(row=1,column=0,columnspan=2,pady=10,padx=10)
label.grid(row=2,column=0,sticky=E,padx=10,pady=10)
entry.grid(row=2,column=1,sticky=W,pady=10)
submit.grid(row=4,column=0,columnspan=2,pady=10)

start = Game_Functions(guess)

root.mainloop()



