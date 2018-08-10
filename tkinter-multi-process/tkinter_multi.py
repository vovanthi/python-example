import tkinter as tk
from muti
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "  Init  "
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

    def say_hi(self):
        print("hi there, everyone!")

if __name__=='__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
