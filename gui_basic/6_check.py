from tkinter import *
root = Tk()
root.title("Nado Gui")
root.geometry("640x480")


chkvar = IntVar() #chkvar에 int형으로 값을 저장한다
chkbox = Checkbutton(root, text="오늘 하루 보지 않기" , variable = chkvar)
# chkbox.select() # 자동 선택 처리
# chk.deselect()# 선택해제처리
chkbox.pack()

chkvar2 = IntVar() #chkvar에 int형으로 값을 저장한다
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기" , variable = chkvar2)
chkbox2.pack()



def btncmd():
    print(chkvar.get()) #0:체크해제 1: 체크
    print(chkvar2.get()) #0:체크해제 1: 체크

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.resizable(False, False) # 크기 조절
root.mainloop()