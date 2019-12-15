from tkinter import *
from main_spider import *
from tkinter import ttk
from tkinter import messagebox
import gl
import time
import datetime


def Check():
	txt.delete('1.0','end')
	check_info()
	messagebox.showinfo("提示","查询成功，查询了"+ str(gl.pageLimit) +"篇文章")
	return 
	
def combChoose(event):
	map = {0:1,1:5,2:10,3:15,4:20,5:30}
	gl.pageLimit=map[comb.current()]
	return
	
def rdChoose():
	map = {0:'hot-topics',1:'gunpla'}
	gl.subCategory=map[var1.get()]
	return
	
def Run():
	txt.delete('1.0','end')
	parse_page_index()
	messagebox.showinfo("提示","发布成功，共发布"+ str(gl.pageLimit) +"篇文章")
	return

def Change(str):
	txt.insert(END,str)

gl.pageLimit=1
gl.subCategory="hot-topics"

root=Tk()
root.title("自动发布程序 V1.1")
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
comb = ttk.Combobox(root,textvariable=var2,values=['1','5','10','15','20','30'],state="readonly")
comb.current(0)
comb.place(relx=0.65,rely=0.5,relwidth=0.2)
comb.bind('<<ComboboxSelected>>',combChoose)

s1 = ttk.Scrollbar(root,orient=VERTICAL)  
txt=Text(root,yscrollcommand=s1.set)
s1.place(relx=0.9,relheight=0.5)
s1.config(command=txt.yview)
txt.place(relheight=0.5,relwidth=1)

btn1 = Button(root,text="查询",command=Check)
btn1.place(relx=0.1,rely=0.8,relwidth=0.2)
btn2 = Button(root,text="发布",command=Run)
btn2.place(relx=0.6,rely=0.8,relwidth=0.2)
root.mainloop()

#def main():
#	return

#if __name__=='__main__':
#	main()
