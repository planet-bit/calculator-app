from tkinter import Tk, Entry, Button, StringVar, Text , Scrollbar, Frame

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry("357x700+0+0")
        master.config(bg = "white")
        master.resizable(True, True)

        self.equation = StringVar()
        self.entry_value = ""

        self.entry = Entry(width = 30, bg ='white', font = ('Arial Bold',28), textvariable = self.equation).place(x = 0, y = 0)
        self.equation.trace("w", self.update_entry_value)
        self.history_text = ""
        self.result = ""

        Button(width = 11, height = 4,text = '(',relief = 'flat', bg = '#e8e8e8', command = lambda:self.show('(')).place(x=0,y=50)
        Button(width = 11, height = 4,text = ')',relief = 'flat', bg = '#e8e8e8', command = lambda:self.show(')')).place(x=90,y=50)
        Button(width = 11, height = 4,text = '%',relief = 'flat', bg = '#b2e7f5', command = lambda:self.show('%')).place(x=180,y=50)
        Button(width = 11, height = 4,text = '1',relief = 'flat', bg = '#e8e8e8', command = lambda:self.show(1)).place(x=0,y=125)
        Button(width = 11, height = 4,text = '2',relief = 'flat', bg = '#e8e8e8', command = lambda:self.show(2)).place(x=90,y=125)
        Button(width = 11, height = 4,text = '3',relief = 'flat', bg = '#e8e8e8', command = lambda:self.show(3)).place(x=180,y=125)
        Button(width = 11, height = 4,text = '4',relief = 'flat', bg = '#e8e8e8', command = lambda:self.show(4)).place(x=0,y=200)
        Button(width = 11, height = 4,text = '5',relief = 'flat', bg = '#e8e8e8', command = lambda:self.show(5)).place(x=90,y=200)
        Button(width = 11, height = 4,text = '6',relief = 'flat', bg = '#e8e8e8', command = lambda:self.show(6)).place(x=180,y=200)
        Button(width = 11, height = 4,text = '7',relief = 'flat', bg = '#e8e8e8', command = lambda:self.show(7)).place(x=0,y=275)
        Button(width = 11, height = 4,text = '8',relief = 'flat', bg = '#e8e8e8', command = lambda:self.show(8)).place(x=90,y=275)
        Button(width = 11, height = 4,text = '9',relief = 'flat', bg = '#e8e8e8', command = lambda:self.show(9)).place(x=180,y=275)
        Button(width = 11, height = 4,text = '0',relief = 'flat', bg = '#e8e8e8', command = lambda:self.show(0)).place(x=90,y=350)
        Button(width = 11, height = 4,text = '.',relief = 'flat', bg = '#e8e8e8', command = lambda:self.show('.')).place(x=180,y=350)
        Button(width = 11, height = 4,text = '+',relief = 'flat', bg = '#b2e7f5', command = lambda:self.show('+')).place(x=270,y=275)
        Button(width = 11, height = 4,text = '-',relief = 'flat', bg = '#b2e7f5', command = lambda:self.show('-')).place(x=270,y=200)
        Button(width = 11, height = 4,text = '/',relief = 'flat', bg = '#b2e7f5', command = lambda:self.show('/')).place(x=270,y=50)
        Button(width = 11, height = 4,text = 'x',relief = 'flat', bg = '#b2e7f5', command = lambda:self.show('*')).place(x=270,y=125)
        Button(width = 11, height = 4,text = '=',relief = 'flat', bg = '#a6f2dd', command = self.solve).place(x=270,y=350)
        Button(width = 11, height = 4,text = 'C',relief = 'flat', bg = '#fcc4b5', command = self.clear).place(x=0,y=350)

        #履歴のフレームを作成
        history_frame = Frame(master, bg = "red")
        history_frame.place(x=0, y=420, width=357, height=240)

        #履歴の表示エリア
        self.history_box = Text(history_frame, width = 35, height = 35 , bg="white", font=("Arial Bold", 12), wrap="word")
        self.history_box.pack(side="left", fill="both", expand= True)

        #スクロールバー
        scrollbar = Scrollbar(history_frame, command = self.history_box.yview)
        scrollbar.pack(side = "right", fill = "y")
        self.history_box.config(yscrollcommand=scrollbar.set)

        #履歴のクリアボタン
        self.clear_history_button = Button(
            width=11, height=2, text='Clear History', relief='flat', bg='#fcc4b5', command=self.clear_history
        )
        self.clear_history_button.place(x=270, y=660)

    def update_entry_value(self, *args):
        """Entryの内容が変更されたら内部変数に反映"""
        self.entry_value = self.equation.get()
        
    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear (self):
        self.entry_value=''
        self.equation.set(self.entry_value)
    
    def solve(self):
        self.history_text = self.entry_value
        self.result = eval(self.entry_value)
        self.equation.set(self.result)
        self.entry_value=str(self.result)
        self.add_history_button(self.history_text)
    
    def add_history_button(self, history_text):
        result_at_creation = self.result  # ボタン作成時の結果を保存
        history_button = Button(
            self.history_box, width=40, height=1, anchor="w", font=("Arial Bold", 12), 
            text=(f"{history_text}={result_at_creation}\n"), relief="flat", bg="white", 
            command=lambda: self.show(result_at_creation)  # 保存した結果を使用
        )
        self.history_box.window_create("end", window=history_button)
        self.history_box.insert("end", "\n")
        self.history_box.see("end")
        
    #履歴を削除
    def clear_history(self):
        self.history_box.delete('1.0','end')


root = Tk()

calculator = Calculator(root)
root.mainloop()
