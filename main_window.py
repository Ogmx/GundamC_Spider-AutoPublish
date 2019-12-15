from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import gl
import main_spider as ms

def Check():
	ms.check_info()
	return 

def combChoose(event):
	map = {0:5,1:10,2:15,3:20,4:30,5:50}
	gl.pageLimit=map[comb.current()]
	return

def rdChoose():
	map = {0:'hot-topics',1:'gunpla'}
	gl.subCategory=map[var1.get()]
	return

def Run():
	messagebox.askokcancel('请选择',str(gl.pageLimit)+str(gl.subCategory))
	return

root=Tk()
root.title("自动发布程序")
root.geometry('500x500')

lab1 = Label(root,text="选择发布栏目:")
lab1.place(relx=0.01, rely=0.5)

var1 = IntVar()
rd1 = Radiobutton(root,text="资讯",variable=var1,value=0,command=rdChoose)
rd1.place(relx=0.2,rely=0.5)
rd1 = Radiobutton(root,text="模玩",variable=var1,value=1,command=rdChoose)
rd1.place(relx=0.2,rely=0.6)

lab2 = Label(root,text="选择发布文章数量:")
lab2.place(relx=0.4, rely=0.5)

var2 = StringVar()
comb = ttk.Combobox(root,textvariable=var2,values=['5','10','15','20','30','50'],state="readonly")
comb.current(0)
comb.place(relx=0.65,rely=0.5,relwidth=0.2)
comb.bind('<<ComboboxSelected>>',combChoose)

txt=Text(root)
txt.place(relheight=0.5)

btn1 = Button(root,text="查询",command=Check)
btn1.place(relx=0.1,rely=0.8,relwidth=0.2)
btn2 = Button(root,text="启动",command=Run)
btn2.place(relx=0.4,rely=0.8,relwidth=0.2)
btn3 = Button(root,text="退出",command=root.quit)
btn3.place(relx=0.7,rely=0.8,relwidth=0.2)

root.mainloop()

def main():
	return
if __name__=='__main__':
    main()