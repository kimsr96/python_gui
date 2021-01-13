from tkinter import *
root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480+300+100") #가로 *세로 + x좌표 + y좌표

filename = ''

def open_file():
    filename = filedialog.askopenfilename(initialdir="/", title="Open File", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))

def save_file(self, whatever = None):
    if (self.filename == ''):
        self.save_file_as()
    else:
        f = open(self.filename, 'w')
        f.write(self.get('1.0', 'end'))
        f.close()

def open_file():
    global filename
    # filename fileed
    return
menu = Menu(root)
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="Open File...", command=open_file)
menu_file.add_command(label="Save", command=self.save_file)
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)

scrollbar = Scrollbar()
scrollbar.pack(side="right", fill="y")

txt = Text(root, width=640, height=480, yscrollcommand = scrollbar.set)
txt.pack()

root.config(menu=menu)
root.mainloop()