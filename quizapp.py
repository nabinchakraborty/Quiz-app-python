from tkinter import *
from tkinter import messagebox as mb
import json


root = Tk()
root.title("Quiz Master")
root.state('zoomed')
root.config(background="#ffffff")
root.resizable(0,0)

def quizstart():
    class Quiz:
        def __init__(self):
            self.qn = 0
            self.ques = self.question(self.qn)
            self.opt_selected = IntVar()
            self.opts = self.radiobtns()
            self.display_options(self.qn)
            self.buttons()
            self.correct = 0

        def question(self, qn):
            t = Label(root, text="Quiz Application in Python", width=100, bg="orange", fg="white", font=("times", 20, "bold"))
            t.place(x=0, y=2)
            qn = Label(root, text=q[qn], width=60, background="#ffffff", font=("times", 32, "bold"), anchor="w")
            qn.place(x=130, y=100)
            return qn

        def radiobtns(self):
            val = 0
            b = []
            yp = 220
            while val < 4:
                btn = Radiobutton(root, text=" ", variable=self.opt_selected, value=val + 1, background="#ffffff", font=("times", 25))
                b.append(btn)
                btn.place(x=250, y=yp)
                val += 1
                yp += 100
            return b

        def display_options(self, qn):
            val = 0
            self.opt_selected.set(0)
            self.ques['text'] = q[qn]
            for op in options[qn]:
                self.opts[val]['text'] = op
                val += 1

        def buttons(self):
            nbutton = Button(root, text="Next",command=self.nextbtn, width=10, bg="green",fg="white",font=("times",16,"bold"))
            nbutton.place(x=200,y=700)
            quitbutton = Button(root, text="Quit", command=root.destroy,width=10,bg="red",fg="white", font=("times",16,"bold"))
            quitbutton.place(x=1200,y=700)

        def checkans(self, qn):
            if self.opt_selected.get() == a[qn]:
              return True
        
        def nextbtn(self):
            if self.checkans(self.qn):
                self.correct += 1
            self.qn += 1
            if self.qn == len(q):
                self.display_result()
            else:
                self.display_options(self.qn)       
        

        def display_result(self):
            score = int(self.correct / len(q) * 100)
            result = "Score: " + str(score) + "%"
            wc = len(q) - self.correct
            correct = "No. of correct answers: " + str(self.correct)
            wrong = "No. of wrong answers: " + str(wc)
            mb.showinfo("Result", "\n".join([result, correct, wrong]))

    quiz= Quiz()
    
def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    btnStart.destroy()
    btnrules.destroy()
    quizstart()
  


def popup():
    mb.showinfo("Rules","This quiz contains 5 questions\nOnce you select a radio button, click Next\nClick on Quit to close the quiz.")

img1 = PhotoImage(file="quiz.png")

labelimage = Label(
    root,
    image = img1,
    background = "#ffffff",
)
labelimage.pack(pady=(40,0))

labeltext = Label(
    root,
    text = "Quiz Master",
    font = ("Comic sans MS",40,"bold"),
    background = "#ffffff",
)
labeltext.pack(pady=(0,35))

img2 = PhotoImage(file="start.png")

btnStart = Button(
    root,
    image = img2,
    relief = FLAT,
    border = 0,
    command = startIspressed,
    background="#ffffff",
)
btnStart.pack()

pic = PhotoImage(file="rules.png")
btnrules = Button(
    root, 
    image=pic, 
    command=popup,
    relief = FLAT,
    background="#ffffff")
btnrules.pack(side=RIGHT, pady=(0,0))



lblInstruction = Label(
    root,
    text = "Read The Rules And\nClick Start Once You Are ready",
    background = "#ffffff",
    font = ("Consolas",14),
    justify = "center",
)

lblInstruction.pack(pady=(0,0), side=LEFT)

with open('quiz.json') as f:
    obj = json.load(f)
q = (obj['ques'])
options = (obj['options'])
a = (obj['ans'])
   
root.mainloop()










