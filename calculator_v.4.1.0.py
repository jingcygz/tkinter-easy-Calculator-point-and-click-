from tkinter import *
from tkinter.messagebox import *

number2 = ''
number1 = ''
newnumber1 = ''
newnumber2 = ''
xuanze = 0


def more():
    win = Tk()

    def ci():
        try:
            num = float(ent3.get()) ** float(ent4.get())
        except:
            a = "请输入数字/输入的字符违法"
            showerror("error", '%s' % a)
        else:
            showinfo("得数是", '%f' % num)
            ent3.delete(0, END)
            ent4.delete(0, END)

    def yu():
        try:
            num = float(ent3.get()) % float(ent4.get())
        except:
            a = "请输入数字/输入的字符违法"
            showerror("error", '%s' % a)
        else:
            showinfo("得数是", '%f' % num)
            ent3.delete(0, END)
            ent4.delete(0, END)

    def zheng():
        try:
            num = float(ent3.get()) // float(ent4.get())
        except:
            a = "请输入数字/输入的字符违法"
            showerror("error", '%s' % a)
        else:
            showinfo("得数是", '%f' % num)
            ent3.delete(0, END)
            ent4.delete(0, END)

    def tuichu():
        b = '是否退出？'
        a = askquestion("询问？", '%s' % b)
        if a == 'yes':
            win.destroy()
        else:
            pass

    win.geometry('500x500')
    win.title("计算器")
    win.configure(bg='orange')

    lb4 = Label(win, text='计算器附属窗口', bg='orange', fg='red')
    lb4.pack()

    lb5 = Label(win, text="数字一", bg='orange', fg='red')
    lb5.place(relheight=0.1, relwidth=0.3, rely=0.3, relx=0.1)

    lb6 = Label(win, text="数字二", bg='orange', fg='red')
    lb6.place(relheight=0.1, relwidth=0.5, rely=0.6, relx=0.1)

    bt6 = Button(win, text="次方", command=ci, bg='orange', fg='red')
    bt6.place(relheight=0.1, relwidth=0.1, rely=0.8, relx=0.1)

    bt7 = Button(win, text="取余", command=yu, bg='orange', fg='red')
    bt7.place(relheight=0.1, relwidth=0.1, rely=0.8, relx=0.3)

    bt8 = Button(win, text="取整", command=zheng, bg='orange', fg='red')
    bt8.place(relheight=0.1, relwidth=0.1, rely=0.8, relx=0.5)

    bt9 = Button(win, text="退出", command=tuichu, bg='orange', fg='red')
    bt9.place(relheight=0.1, relwidth=0.1, rely=0.6, relx=0.9)

    ent3 = Entry(win, bg='orange', fg='red')
    ent3.place(relheight=0.1, relwidth=0.3, rely=0.3, relx=0.5)

    ent4 = Entry(win, bg='orange', fg='red')
    ent4.place(relheight=0.1, relwidth=0.3, rely=0.6, relx=0.5)

    bt10 = Button(win, text="更多", command=more, bg='orange', fg='red')
    bt10.place(relheight=0.1, relwidth=0.1, rely=0.3, relx=0.9)

    a = '计算器附属窗口'
    showinfo("请切换至", '%s' % a)


def more1():
    t = Tk()

    def jia():
        try:
            num = float(ent1.get()) + float(ent2.get())
        except:
            a = "请输入数字/输入的字符违法"
            showerror("error", '%s' % a)
        else:
            showinfo("得数是", '%f' % num)
            ent1.delete(0, END)
            ent2.delete(0, END)

    def jian():
        try:
            num = float(ent1.get()) - float(ent2.get())
        except:
            a = "请输入数字/输入的字符违法"
            showerror("error", '%s' % a)
        else:
            showinfo("得数是", '%f' % num)
            ent1.delete(0, END)
            ent2.delete(0, END)

    def cheng():
        try:
            num = float(ent1.get()) * float(ent2.get())
        except:
            a = "请输入数字/输入的字符违法"
            showerror("确定？", '%s' % a)
        else:
            showinfo("得数是", '%f' % num)
            ent1.delete(0, END)
            ent2.delete(0, END)

    def chu():
        while 1:
            try:
                num = float(ent1.get()) / float(ent2.get())
                if float(ent2.get()) == 0:
                    a = "输入的数字不能为零"
                    showerror("error", '%s' % a)
                    ent2.delete(0, END)
                    break
            except:
                a = "输入的数字格式不正确,请重新输入"
                showerror("error", '%s' % a)
                ent1.delete(0, END)
                ent2.delete(0, END)
                break
            else:
                showinfo("得数是", '%f' % num)
                ent1.delete(0, END)
                ent2.delete(0, END)
                break

    def tuichu():
        b = '是否退出？'
        a = askquestion("error", '%s' % b)
        if a == 'yes':
            t.destroy()
        else:
            pass

    t.geometry('500x500')
    t.title("计算器")
    t.configure(bg='orange')

    lb2 = Label(t, text="数字一", bg='orange', fg='red')
    lb2.place(relheight=0.1, relwidth=0.3, rely=0.3, relx=0.1)

    lb3 = Label(t, text="数字二", bg='orange', fg='red')
    lb3.place(relheight=0.1, relwidth=0.3, rely=0.6, relx=0.1)

    bt1 = Button(t, text="加", command=jia, bg='orange', fg='red')
    bt1.place(relheight=0.1, relwidth=0.1, rely=0.8, relx=0.1)

    bt2 = Button(t, text="减", command=jian, bg='orange', fg='red')
    bt2.place(relheight=0.1, relwidth=0.1, rely=0.8, relx=0.3)

    bt3 = Button(t, text="乘", command=cheng, bg='orange', fg='red')
    bt3.place(relheight=0.1, relwidth=0.1, rely=0.8, relx=0.5)

    bt5 = Button(t, text='除', command=chu, bg='orange', fg='red')
    bt5.place(relheight=0.1, relwidth=0.1, rely=0.8, relx=0.7)

    bt4 = Button(t, text="更多", command=more, bg='orange', fg='red')
    bt4.place(relheight=0.1, relwidth=0.1, rely=0.3, relx=0.9)

    bt9 = Button(t, text="退出", command=tuichu, bg='orange', fg='red')
    bt9.place(relheight=0.1, relwidth=0.1, rely=0.6, relx=0.9)

    ent1 = Entry(t, bg='orange', fg='red')
    ent1.place(relheight=0.1, relwidth=0.3, rely=0.3, relx=0.5)

    ent2 = Entry(t, bg='orange', fg='red')
    ent2.place(relheight=0.1, relwidth=0.3, rely=0.6, relx=0.5)

    lb1 = Label(t, text="计算器", bg='orange', fg='red')
    lb1.pack()

    t.mainloop()


def more2():
    window = Tk()

    # ----------------------------------------------------------------------------------------------------------------------------

    class Add(object):

        def add0(self):
            global number1
            a1 = '0'
            txt.insert(END, a1)
            number1 += a1

        def add1(self):
            global number1
            a1 = '1'
            txt.insert(END, a1)
            number1 += a1

        def add2(self):
            global number1
            a1 = '2'
            txt.insert(END, a1)
            number1 += a1

        def add3(self):
            global number1
            a1 = '3'
            txt.insert(END, a1)
            number1 += a1

        def add4(self):
            global number1
            a1 = '4'
            txt.insert(END, a1)
            number1 += a1

        def add5(self):
            global number1
            a1 = '5'
            txt.insert(END, a1)
            number1 += a1

        def add6(self):
            global number1
            a1 = '6'
            txt.insert(END, a1)
            number1 += a1

        def add7(self):
            global number1
            a1 = '7'
            txt.insert(END, a1)
            number1 += a1

        def add8(self):
            global number1
            a1 = '8'
            txt.insert(END, a1)
            number1 += a1

        def add9(self):
            global number1
            a1 = '9'
            txt.insert(END, a1)
            number1 += a1

        def adddian(self):
            global number1
            a1 = '.'
            txt.insert(END, a1)
            number1 += a1

    # ----------------------------------------------------------------------------------------------------------------------------

    class Yunsuanfuhao(object):

        def add(self):
            global number1
            global newnumber1
            newnumber1 = number1
            string = '+'
            txt.insert(END, string)
            number1 += string

        def jian(self):
            global number1
            global newnumber1
            newnumber1 = number1
            string = '-'
            txt.insert(END, string)
            number1 += string

        def cheng(self):
            global number1
            global newnumber1
            newnumber1 = number1
            string = '*'
            string1 = '×'
            txt.insert(END, string1)
            number1 += string

        def chu(self):
            global number1
            global newnumber1
            newnumber1 = number1
            string = '/'
            string1 = '÷'
            txt.insert(END, string1)
            number1 += string

    # ----------------------------------------------------------------------------------------------------------------------------

    def dengyu():
        global number2
        global number1
        global xuanze
        try:
            global number2
            global number1
            global newnumber1
            global newnumber2
            number2 = eval(number1)
            string = '='
            txt.insert(END, string)
            txt.insert(END, number2)
        except (ValueError, ZeroDivisionError, SyntaxError) as e:
            a1 = '请输入（点击）正确的数'
            showerror(e, '%s' % a1)
            number2 = ''
            number1 = ''
            xuanze = 0
            txt.delete(1.0, END)

    def ac():
        global number2
        global number1
        global xuanze
        number2 = ''
        number1 = ''
        xuanze = 0
        txt.delete(1.0, END)

    def zhengfushu():
        global number1
        global number2
        txt.insert(END, '-')
        number1 += '-'

    def back():
        try:
            global number1
            global number2
            global xuanze
            number1 = int(number1) // 10
            txt.delete(1.0, END)
            txt.insert(END, str(number1))
        except (ValueError) as e:
            a1 = '请输入（点击）正确的数'
            showerror(e, '%s' % a1)
            number2 = ''
            number1 = ''
            xuanze = 0
            txt.delete(1.0, END)

    def tuichu():
        b2 = '是否退出？'
        a1 = askquestion('questions', '%s' % b2)
        if a1 == 'yes':
            window.destroy()
        else:
            pass

    # ----------------------------------------------------------------------------------------------------------------------------
    window.geometry('500x500')
    window.title('计算器')
    window.iconbitmap(default="./calculator-icon_34473.ico")
    window.configure(bg='orange')

    addnumber = Add()
    addyunsuanfuhao = Yunsuanfuhao()

    lb1 = Label(window, text='计算器', bg='orange', fg='red')
    lb1.pack()

    bt0 = Button(window, text='0', command=addnumber.add0, bg='orange', fg='red')
    bt0.place(relheight=0.1, relwidth=0.2, rely=0.9, relx=0.3)

    bt1 = Button(window, text='1', command=addnumber.add1, bg='orange', fg='red')
    bt1.place(relheight=0.1, relwidth=0.2, rely=0.8, relx=0.1)

    bt2 = Button(window, text='2', command=addnumber.add2, bg='orange', fg='red')
    bt2.place(relheight=0.1, relwidth=0.2, rely=0.8, relx=0.3)

    bt3 = Button(window, text='3', command=addnumber.add3, bg='orange', fg='red')
    bt3.place(relheight=0.1, relwidth=0.2, rely=0.8, relx=0.5)

    bt4 = Button(window, text='4', command=addnumber.add4, bg='orange', fg='red')
    bt4.place(relheight=0.1, relwidth=0.2, rely=0.7, relx=0.1)

    bt5 = Button(window, text='5', command=addnumber.add5, bg='orange', fg='red')
    bt5.place(relheight=0.1, relwidth=0.2, rely=0.7, relx=0.3)

    bt6 = Button(window, text='6', command=addnumber.add6, bg='orange', fg='red')
    bt6.place(relheight=0.1, relwidth=0.2, rely=0.7, relx=0.5)

    bt7 = Button(window, text='7', command=addnumber.add7, bg='orange', fg='red')
    bt7.place(relheight=0.1, relwidth=0.2, rely=0.6, relx=0.1)

    bt8 = Button(window, text='8', command=addnumber.add8, bg='orange', fg='red')
    bt8.place(relheight=0.1, relwidth=0.2, rely=0.6, relx=0.3)

    bt9 = Button(window, text='9', command=addnumber.add9, bg='orange', fg='red')
    bt9.place(relheight=0.1, relwidth=0.2, rely=0.6, relx=0.5)

    bt0 = Button(window, text='.', command=addnumber.adddian, bg='orange', fg='red')
    bt0.place(relheight=0.1, relwidth=0.2, rely=0.9, relx=0.1)

    btadd = Button(window, text='+', command=addyunsuanfuhao.add, bg='orange', fg='red')
    btadd.place(relheight=0.1, relwidth=0.2, rely=0.4, relx=0.8)

    btadd = Button(window, text='-', command=addyunsuanfuhao.jian, bg='orange', fg='red')
    btadd.place(relheight=0.1, relwidth=0.2, rely=0.5, relx=0.8)

    btadd = Button(window, text='×', command=addyunsuanfuhao.cheng, bg='orange', fg='red')
    btadd.place(relheight=0.1, relwidth=0.2, rely=0.6, relx=0.8)

    btadd = Button(window, text='÷', command=addyunsuanfuhao.chu, bg='orange', fg='red')
    btadd.place(relheight=0.1, relwidth=0.2, rely=0.7, relx=0.8)

    btok = Button(window, text='=', command=dengyu, bg='orange', fg='red')
    btok.place(relheight=0.1, relwidth=0.2, rely=0.8, relx=0.8)

    btac = Button(window, text='AC', command=ac, bg='orange', fg='red')
    btac.place(relheight=0.1, relwidth=0.2, rely=0.9, relx=0.8)

    btfushu = Button(window, text='-/+（负）', command=zhengfushu, bg='orange', fg='red')
    btfushu.place(relheight=0.1, relwidth=0.2, rely=0.4, relx=0.6)

    bttuichu = Button(window, text='退出', command=tuichu, bg='orange', fg='red')
    bttuichu.place(relheight=0.1, relwidth=0.2, rely=0.4, relx=0.2)

    btback = Button(window, text='<--', command=back, bg='orange', fg='red')
    btback.place(relheight=0.1, relwidth=0.2, rely=0.4, relx=0.4)

    txt = Text(window, bg='orange', fg='red')
    txt.place(rely=0.05, relheight=0.3, relwidth=1)

    window.mainloop()


def about():
    a1 = '制作：@QQ小井井\n如需搬运请加QQ：771732203（注明来意）\n或更改此为（第一行）：\n制作：@QQ小井井，已注明，已获得许可\ngithub:\nhttps://github.com' \
         '/jingcygz/jingcygz\n（此网站为readme.md） '
    showinfo("关于", '%s' % a1)


if __name__ == '__main__':
    calculator = Tk()
    calculator.geometry("400x240")
    calculator.title('计算器显示界面')
    calculator.configure(bg='orange')

    lb1 = Label(calculator, text='计算器选择界面', bg='orange', fg='red')
    lb1.pack()

    lb2 = Label(calculator, text='qq@小井井，QQ：77173203，邮箱：771732203@qq.com', bg='orange', fg='red')
    lb2.place(relwidth=0.9, rely=0.8, relheight=0.2)

    bt1 = Button(calculator, text='计算器（输入式）', command=more1, bg='orange', fg='red')
    bt1.place(relwidth=0.5, rely=0.2, relx=0.25, relheight=0.2)

    bt2 = Button(calculator, text='计算器（点击式）', command=more2, bg='orange', fg='red')
    bt2.place(relwidth=0.5, rely=0.4, relx=0.25, relheight=0.2)

    btabout = Button(calculator, text='关于', command=about, bg='orange', fg='red')
    btabout.place(relwidth=0.5, rely=0.6, relx=0.25, relheight=0.2)

    calculator.mainloop()
