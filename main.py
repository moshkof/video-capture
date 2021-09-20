import tkinter as tk
import video_capture


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        # self.video_capture.run_analysis()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Показать видео\n"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.video = tk.Frame(self, bg=video_capture)
        self.video = video_capture.run_analysis()

        # self.quit = tk.Button(self, text="выход", fg="red",
        #                       command=self.master.destroy)
        # self.quit.pack(side="bottom")


    # def video_capture(self):
    #     self.video_cap = tk.Frame(self.video_capture)
        # self.video_capture.pack()

    def say_hi(self):
        video_capture.run_analysis()
        self.quit = tk.Button(self, text="выход", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
        # print("hi there, everyone!")
        


root = tk.Tk()
app = Application(master=root)
app.master.geometry('400x250')
app.mainloop()
