from tkinter.scrolledtext import ScrolledText
import json
import json_tools
from tkinter import *

def diff_detail(diffent):
    if diffent !="[]":
        diffent=diffent.replace('replace',"新值替换老值字段")
        diffent = diffent.replace('value', "新值")
        diffent = diffent.replace('prev', "老值")
        diffent = diffent.replace('add', "新值增加字段")
        diffent = diffent.replace('remove', "新值移除字段")
        diffent = diffent.replace('None', "null")
        diffent = diffent.replace("'", '"')
        diffent = json.loads(diffent)
    else:
        diffent="无区别，比对成功！"
    return diffent

'''主界面'''
def dsqUI():
    def compare():
        try:
            e3.delete(1.0,END)
            jsona = json.loads(e1.get(1.0,END).replace("'",'"'))
            jsonb = json.loads(e2.get(1.0,END).replace("'",'"'))
            diffent = json_tools.diff(jsona,jsonb)
            diffent=diff_detail(str(diffent))
            result.config(fg="red")
            if diffent=="无区别，比对成功！":
                result.config(fg="green")
                e3.insert(1.0,diffent)
            else:
                for index in range(0,len(diffent)):
                    e3.insert(END,diffent[index])
                    e3.insert(INSERT,"\n")
                    e3.insert(INSERT,"\n")
        except EXCEPTION:
            e3.insert(1.0,"请检查输入JSON的格式")
    def reset():
        e1.delete(1.0,END)
        e2.delete(1.0,END)
    root=Tk()
    e1=ScrolledText(root,bd=3,relief="solid")
    e2=ScrolledText(root,bd=3,relief="solid")
    e3=ScrolledText(root,bd=3,relief="solid",fg='red')

    # e_sku=Entry(root,width=15,bd=3)
    # e_sku.grid(row=0,column=2,padx=50,pady=60,sticky=N+W)
    #
    # e_sku1 = Entry(root, width=15, bd=3)
    # e_sku1.grid(row=0, column=2, padx=50, pady=60, sticky=N)
    #
    # e_sku2 = Entry(root, width=15, bd=3)
    # e_sku2.grid(row=0, column=2, padx=50, pady=60, sticky=E+N)
    """设置标题"""
    root.title("JSON对比工具")
    Label(root,text="老值",font=("微软雅黑",30),padx=5).grid(row=0,column=0)
    Label(root,text="新值",font=("微软雅黑",30),padx=5).grid(row=1,column=0)


    result=Label(root,text="比对结果",font=("微软雅黑",40),fg='black')
    result.grid(row=0,column=2,sticky=S)

    e1.grid(row=0,column=1,padx=5,pady=5)
    e2.grid(row=1,column=1,padx=5,pady=5)
    e3.grid(row=1,column=2,padx=5,pady=5)

    bt_compare = Button(root,text='对比',bd=3,width=8,height=2,activeforeground="green",activebackground="pink",command=compare,font=("微软雅黑",20),relief=SUNKEN)
    bt_reset=Button(root,text='重置',bd=3,width=8,height=2,activeforeground="green",activebackground="pink",command=reset,font=("微软雅黑",20),relief=SUNKEN)

    bt_compare.grid(row=2,column=2,padx=10)
    bt_reset.grid(row=2,column=1)

    mainloop()

if __name__ == '__main__':
    dsqUI()


