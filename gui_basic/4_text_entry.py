from tkinter import *
root = Tk()
root.title("Nado Gui")
root.geometry("640x480")

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30) # 한줄 입력 엔터 불가능
e.pack()
e.insert(0, "한 줄만 입력해요") # 0, and 동일 (기본값)

def btncmd():
    #내용 출력
    print(txt.get("1.0",END)) # 처음부터 끝까지 모든 값 1: 첫번째 라인, 0: 0번째 column 위치
    print(e.get())

    #내용 삭제
    txt.delete("1.0",END)
    e.delete(0, END)

    
btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.resizable(False, False) # 크기 조절
root.mainloop()