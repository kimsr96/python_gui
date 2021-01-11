import tkinter.ttk as ttk 
from tkinter import *
root = Tk()
root.title("Nado Gui")
root.geometry("640x480")


values = [str(i) + "일" for i in range(1,32)]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일") #최초 목록 제목 설정

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly") #읽기전용
readonly_combobox.current(0)
readonly_combobox.pack()


def btncmd():
    print(combobox.get()) #선택한 값 표시
    print(readonly_comboboxs.get()) #선택한 값 표시

btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop()