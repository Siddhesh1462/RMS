from tkinter import *
from tkinter import ttk
import random
from tkinter import filedialog
import datetime as dt
import os
from tkinter import messagebox

path = 'C:\\Users\\sanke\\OneDrive\Desktop\\rms-tkinter\\bills'


def main():
    win = Tk()
    app = homePage(win)
    win.mainloop()


exp = " "


class homePage:

    def __init__(self, win):
        self.win = win
        self.win.geometry("1530x790+0+0")
        win["background"] = "#ADD8E6"
        date_pr = dt.datetime.now()
        self.win.title("Restauarant Management System")

        self.title_label = Label(self.win,
                                 text="Sai Restaurant",
                                 font=("Arial", 35, "bold"),
                                 bg="lightblue",
                                 bd=8,
                                 relief=GROOVE)
        self.title_label.pack(side=TOP, fill=X)

        self.date = Label(self.title_label,
                          text=f"{date_pr:%B %d, %Y}",
                          font=("Arial, 18"),
                          bg="lightblue").place(x=50, y=12)
        self.time = Label(self.title_label,
                          text=f"{date_pr:%T}",
                          font=("Arial, 18"),
                          bg="lightblue").place(x=1350, y=12)

        #-------------------------variables------------------------------------#
        bill_no = random.randint(100, 9999)

        #----------------------------------------DRINKS--------------------------------------------------

        self.drink_frame = LabelFrame(self.win,
                                      bg="lightblue",
                                      bd=6,
                                      relief=GROOVE,
                                      text="Drinks",
                                      font=("Arial", 16, "bold"))
        self.drink_frame.place(x=0, y=70, height=416, width=768 / 2)

        sprite = StringVar()
        fanta = StringVar()
        thumsup = StringVar()
        cococola = StringVar()
        pepsi = StringVar()
        c_of_drinks_list = StringVar()
        c_of_drinks = StringVar()
        equation = StringVar()
        Pav_bhaji = StringVar()
        aloo_paratha = StringVar()
        masala_dosa = StringVar()
        medu_wada = StringVar()
        idli_sambar = StringVar()
        c_of_foods_list = StringVar()
        c_of_foods = StringVar()
        c_of_dandf = StringVar()
        tax = StringVar()
        s_total = StringVar()
        total_cost = StringVar()

        def output():
            return self.sec_frame_txt.get(1.0, "end-1c")

        def total():

            sq = sprite.get()
            fq = fanta.get()
            cq = cococola.get()
            tq = thumsup.get()
            pq = pepsi.get()
            drink_dict = dict()
            drinks = ["Sprite", "Fanta", "Cococola", "Thumsup", "Pepsi"]
            drink_q_str = [sq, fq, cq, tq, pq]
            drink_q = []
            c_of_drinks_list = []
            for i in drink_q_str:
                if i == "":
                    i = 0
                else:
                    i = int(i)
                drink_q.append(i)

            for i in drink_q:
                if i != 0:
                    index = drink_q.index(i)
                    drink_name = drinks[index]
                    drink_dict[drink_name] = i

            drink_new_list = list(drink_dict.keys())
            drink_cost = [35, 35, 35, 28, 25]

            for i in range(len(drink_q)):
                c_of_drinks_list.append(drink_q[i] * drink_cost[i])

            c_of_drinks.set(sum(c_of_drinks_list))

            pbq = Pav_bhaji.get()
            apq = aloo_paratha.get()
            mdq = masala_dosa.get()
            mwq = medu_wada.get()
            isq = idli_sambar.get()

            food_q_str = [pbq, apq, mdq, mwq, isq]
            food_dict = dict()
            food = [
                "Pav Bhaji", "Aloo Paratha", "Masala Dosa", "Medu Wada",
                "Idli Sambar"
            ]
            food_q = []
            c_of_foods_list = []
            for i in food_q_str:
                if i == "":
                    i = 0
                else:
                    i = int(i)
                food_q.append(i)

            for i in food_q:
                if i != 0:
                    index = food_q.index(i)
                    food_name = food[index]
                    food_dict[food_name] = i

            food_new_list = list(food_dict.keys())

            food_cost = [40, 30, 55, 30, 40]

            for i in range(len(food_q)):
                c_of_foods_list.append(food_q[i] * food_cost[i])

            c_of_foods.set(sum(c_of_foods_list))

            c_of_dandf = sum(c_of_foods_list) + sum(c_of_drinks_list)
            s_total.set(c_of_dandf)
            tax.set(c_of_dandf * 0.12)

            total_cost.set("%.2f" % (c_of_dandf + (c_of_dandf * 0.12)))

            self.sec_frame_txt.insert(
                END,
                "------------------------------------------------------\n")
            self.sec_frame_txt.insert(END, "\t\t     Sai Restaurant")
            self.sec_frame_txt.insert(
                END, "\n\t At Lonere, Near Grampanchayat, 402103\n")
            self.sec_frame_txt.insert(END, "\t\tContact No. +919422474347\n")
            self.sec_frame_txt.insert(END, f"\t\t      Bill No. {bill_no}\n")
            self.sec_frame_txt.insert(
                END,
                "------------------------------------------------------\n\n")
            self.sec_frame_txt.insert(END, " Mains\t\t\tQuantity\t\t Cost\n")
            for i in range(len(food_new_list)):
                if food_new_list[i] == "Pav Bhaji":
                    self.sec_frame_txt.insert(
                        END,
                        f" {food_new_list[i]}\t\t\t  {food_dict[food_new_list[i]]}\t\t {40 * food_dict[food_new_list[i]]}\n"
                    )
                if food_new_list[i] == "Aloo Paratha":
                    self.sec_frame_txt.insert(
                        END,
                        f" {food_new_list[i]}\t\t\t  {food_dict[food_new_list[i]]}\t\t {30 * food_dict[food_new_list[i]]}\n"
                    )
                if food_new_list[i] == "Masala Dosa":
                    self.sec_frame_txt.insert(
                        END,
                        f" {food_new_list[i]}\t\t\t  {food_dict[food_new_list[i]]}\t\t {55 * food_dict[food_new_list[i]]}\n"
                    )
                if food_new_list[i] == "Medu Wada":
                    self.sec_frame_txt.insert(
                        END,
                        f" {food_new_list[i]}\t\t\t  {food_dict[food_new_list[i]]}\t\t {30 * food_dict[food_new_list[i]]}\n"
                    )
                if food_new_list[i] == "Idli Sambar":
                    self.sec_frame_txt.insert(
                        END,
                        f" {food_new_list[i]}\t\t\t  {food_dict[food_new_list[i]]}\t\t {40 * food_dict[food_new_list[i]]}\n"
                    )
            self.sec_frame_txt.insert(END,
                                      "\n Drinks\t\t\tQuantity\t\t Cost\n")
            for i in range(len(drink_new_list)):
                if drink_new_list[i] == "Sprite":
                    self.sec_frame_txt.insert(
                        END,
                        f" {drink_new_list[i]}\t\t\t  {drink_dict[drink_new_list[i]]}\t\t {35 * drink_dict[drink_new_list[i]]}\n"
                    )
                if drink_new_list[i] == "Fanta":
                    self.sec_frame_txt.insert(
                        END,
                        f" {drink_new_list[i]}\t\t\t  {drink_dict[drink_new_list[i]]}\t\t {35 * drink_dict[drink_new_list[i]]}\n"
                    )
                if drink_new_list[i] == "Cococola":
                    self.sec_frame_txt.insert(
                        END,
                        f" {drink_new_list[i]}\t\t\t  {drink_dict[drink_new_list[i]]}\t\t {35 * drink_dict[drink_new_list[i]]}\n"
                    )
                if drink_new_list[i] == "Thumsup":
                    self.sec_frame_txt.insert(
                        END,
                        f" {drink_new_list[i]}\t\t\t  {drink_dict[drink_new_list[i]]}\t\t {28 * drink_dict[drink_new_list[i]]}\n"
                    )
                if drink_new_list[i] == "Pepsi":
                    self.sec_frame_txt.insert(
                        END,
                        f" {drink_new_list[i]}\t\t\t  {drink_dict[drink_new_list[i]]}\t\t {25 * drink_dict[drink_new_list[i]]}\n"
                    )
            self.sec_frame_txt.insert(END,
                                      f"\n\t\t\tSubTotal\t\t {c_of_dandf}")
            self.sec_frame_txt.insert(
                END, f"\n\t\t\tTax\t\t {'%.2f' % (c_of_dandf*0.12)}")
            self.sec_frame_txt.insert(
                END,
                f"\n\t\t\tTotal\t\t {'%.2f' % (c_of_dandf + (c_of_dandf*0.12))}"
            )
            self.sec_frame_txt.insert(END, f"\n\n\n {date_pr:%B %d, %Y}\n")
            self.sec_frame_txt.insert(END, f" {date_pr:%T}\n")
            self.sec_frame_txt.insert(END, "\n\n\t\tTHANK YOU FOR VISTING")

            refno = str(bill_no)
            pakodi = refno + ".txt"
            global path
            with open(os.path.join(path, pakodi), "w") as file1:
                toFile = output()
                file1.write(toFile)
            qmsg = messagebox.showinfo("Information", "Bill Generated")
            return self.sec_frame_txt

        def reset():

            sprite.set("")
            fanta.set("")
            cococola.set("")
            thumsup.set("")
            pepsi.set("")
            Pav_bhaji.set("")
            aloo_paratha.set("")
            masala_dosa.set("")
            medu_wada.set("")
            idli_sambar.set("")
            c_of_drinks.set("")
            c_of_foods.set("")
            tax.set("")
            s_total.set("")
            total_cost.set("")
            self.sec_frame_txt.destroy()
            self.sec_frame_txt = Text(self.sec_frame,
                                      bg="white",
                                      yscrollcommand=self.y_scroll.set)
            self.sec_frame_txt.pack(fill=BOTH, expand=TRUE, padx=150)

        drink_button1 = IntVar()
        drink_button2 = IntVar()
        drink_button3 = IntVar()
        drink_button4 = IntVar()
        drink_button5 = IntVar()

        def Clicked1():
            if drink_button1.get() == 1:
                self.drink_entry1 = Entry(self.drink_frame,
                                          bd=5,
                                          textvariable=sprite,
                                          font=("Arial", 16),
                                          width=8,
                                          state=NORMAL).grid(row=0,
                                                             column=3,
                                                             padx=2,
                                                             pady=3)

            else:
                self.drink_entry1 = Entry(self.drink_frame,
                                          bd=5,
                                          textvariable=sprite,
                                          font=("Arial", 16),
                                          width=8,
                                          state=DISABLED).grid(row=0,
                                                               column=3,
                                                               padx=2,
                                                               pady=3)

        def Clicked2():
            if drink_button2.get() == 1:
                self.drink_entry2 = Entry(self.drink_frame,
                                          bd=5,
                                          textvariable=fanta,
                                          font=("Arial", 16),
                                          width=8,
                                          state=NORMAL).grid(row=1,
                                                             column=3,
                                                             padx=2,
                                                             pady=3)
            else:
                self.drink_entry2 = Entry(self.drink_frame,
                                          bd=5,
                                          textvariable=fanta,
                                          font=("Arial", 16),
                                          width=8,
                                          state=DISABLED).grid(row=1,
                                                               column=3,
                                                               padx=2,
                                                               pady=3)

        def Clicked3():
            if drink_button3.get() == 1:
                self.drink_entry3 = Entry(self.drink_frame,
                                          bd=5,
                                          textvariable=cococola,
                                          font=("Arial", 16),
                                          width=8,
                                          state=NORMAL).grid(row=2,
                                                             column=3,
                                                             padx=2,
                                                             pady=3)
            else:
                self.drink_entry3 = Entry(self.drink_frame,
                                          bd=5,
                                          textvariable=cococola,
                                          font=("Arial", 16),
                                          width=8,
                                          state=DISABLED).grid(row=2,
                                                               column=3,
                                                               padx=2,
                                                               pady=3)

        def Clicked4():
            if drink_button4.get() == 1:
                self.drink_entry4 = Entry(self.drink_frame,
                                          bd=5,
                                          textvariable=thumsup,
                                          font=("Arial", 16),
                                          width=8,
                                          state=NORMAL).grid(row=3,
                                                             column=3,
                                                             padx=2,
                                                             pady=3)
            else:
                self.drink_entry4 = Entry(self.drink_frame,
                                          bd=5,
                                          textvariable=thumsup,
                                          font=("Arial", 16),
                                          width=8,
                                          state=DISABLED).grid(row=3,
                                                               column=3,
                                                               padx=2,
                                                               pady=3)

        def Clicked5():
            if drink_button5.get() == 1:
                self.drink_entry5 = Entry(self.drink_frame,
                                          bd=5,
                                          textvariable=pepsi,
                                          font=("Arial", 16),
                                          width=8,
                                          state=NORMAL).grid(row=4,
                                                             column=3,
                                                             padx=2,
                                                             pady=3)
            else:
                self.drink_entry5 = Entry(self.drink_frame,
                                          bd=5,
                                          textvariable=pepsi,
                                          font=("Arial", 16),
                                          width=8,
                                          state=DISABLED).grid(row=4,
                                                               column=3,
                                                               padx=2,
                                                               pady=3)

        Button1 = Checkbutton(self.drink_frame,
                              variable=drink_button1,
                              onvalue=1,
                              offvalue=0,
                              text="Sprite",
                              height=1,
                              bg="lightblue",
                              font=("Arial", 16),
                              command=Clicked1).grid(padx=5, pady=5)
        Button2 = Checkbutton(self.drink_frame,
                              variable=drink_button2,
                              onvalue=1,
                              offvalue=0,
                              text="Fanta",
                              height=1,
                              bg="lightblue",
                              font=("Arial", 16),
                              command=Clicked2).grid(padx=5, pady=5)
        Button3 = Checkbutton(self.drink_frame,
                              variable=drink_button3,
                              onvalue=1,
                              offvalue=0,
                              text="CocoCola",
                              height=1,
                              bg="lightblue",
                              font=("Arial", 16),
                              command=Clicked3).grid(padx=5, pady=5)
        Button4 = Checkbutton(self.drink_frame,
                              variable=drink_button4,
                              onvalue=1,
                              offvalue=0,
                              text="ThumbsUp",
                              height=1,
                              bg="lightblue",
                              font=("Arial", 16),
                              command=Clicked4).grid(padx=5, pady=5)
        Button5 = Checkbutton(self.drink_frame,
                              variable=drink_button5,
                              onvalue=1,
                              offvalue=0,
                              text="Pepsi",
                              height=1,
                              bg="lightblue",
                              font=("Arial", 16),
                              command=Clicked5).grid(padx=5, pady=5)

        #-----------------------------------FOOD------------------------------------------------------

        self.food_frame = LabelFrame(self.win,
                                     bg="lightblue",
                                     bd=6,
                                     relief=GROOVE,
                                     text="Dishes",
                                     font=("Arial", 16, "bold"))
        self.food_frame.place(x=768 / 2, y=70, height=416, width=768 / 2)

        food_button1 = IntVar()
        food_button2 = IntVar()
        food_button3 = IntVar()
        food_button4 = IntVar()
        food_button5 = IntVar()

        def Clicked_1():
            if food_button1.get() == 1:
                self.food_entry1 = Entry(self.food_frame,
                                         bd=5,
                                         textvariable=Pav_bhaji,
                                         font=("Arial", 16),
                                         width=8,
                                         state=NORMAL).grid(row=0,
                                                            column=3,
                                                            padx=2,
                                                            pady=3)

            else:
                self.food_entry1 = Entry(self.food_frame,
                                         bd=5,
                                         textvariable=Pav_bhaji,
                                         font=("Arial", 16),
                                         width=8,
                                         state=DISABLED).grid(row=0,
                                                              column=3,
                                                              padx=2,
                                                              pady=3)

        def Clicked_2():
            if food_button2.get() == 1:
                self.food_entry2 = Entry(self.food_frame,
                                         bd=5,
                                         textvariable=aloo_paratha,
                                         font=("Arial", 16),
                                         width=8,
                                         state=NORMAL).grid(row=1,
                                                            column=3,
                                                            padx=2,
                                                            pady=3)
            if food_button2.get() == 0:
                self.food_entry2 = Entry(self.food_frame,
                                         bd=5,
                                         textvariable=aloo_paratha,
                                         font=("Arial", 16),
                                         width=8,
                                         state=DISABLED).grid(row=1,
                                                              column=3,
                                                              padx=2,
                                                              pady=3)

        def Clicked_3():
            if food_button3.get() == 1:
                self.food_entry3 = Entry(self.food_frame,
                                         bd=5,
                                         textvariable=masala_dosa,
                                         font=("Arial", 16),
                                         width=8,
                                         state=NORMAL).grid(row=2,
                                                            column=3,
                                                            padx=2,
                                                            pady=3)
            else:
                self.food_entry3 = Entry(self.food_frame,
                                         bd=5,
                                         textvariable=masala_dosa,
                                         font=("Arial", 16),
                                         width=8,
                                         state=DISABLED).grid(row=2,
                                                              column=3,
                                                              padx=2,
                                                              pady=3)

        def Clicked_4():
            if food_button4.get() == 1:
                self.food_entry4 = Entry(self.food_frame,
                                         bd=5,
                                         textvariable=medu_wada,
                                         font=("Arial", 16),
                                         width=8,
                                         state=NORMAL).grid(row=3,
                                                            column=3,
                                                            padx=2,
                                                            pady=3)
            else:
                self.food_entry4 = Entry(self.food_frame,
                                         bd=5,
                                         textvariable=medu_wada,
                                         font=("Arial", 16),
                                         width=8,
                                         state=DISABLED).grid(row=3,
                                                              column=3,
                                                              padx=2,
                                                              pady=3)

        def Clicked_5():
            if food_button5.get() == 1:
                self.food_entry5 = Entry(self.food_frame,
                                         bd=5,
                                         textvariable=idli_sambar,
                                         font=("Arial", 16),
                                         width=8,
                                         state=NORMAL).grid(row=4,
                                                            column=3,
                                                            padx=2,
                                                            pady=3)
            else:
                self.food_entry5 = Entry(self.food_frame,
                                         bd=5,
                                         textvariable=idli_sambar,
                                         font=("Arial", 16),
                                         width=8,
                                         state=DISABLED).grid(row=4,
                                                              column=3,
                                                              padx=2,
                                                              pady=3)

        Button1 = Checkbutton(self.food_frame,
                              variable=food_button1,
                              onvalue=1,
                              offvalue=0,
                              text="Pav Bhaji",
                              height=1,
                              bg="lightblue",
                              font=("Arial", 16),
                              command=Clicked_1).grid(padx=5, pady=5)
        Button2 = Checkbutton(self.food_frame,
                              variable=food_button2,
                              onvalue=1,
                              offvalue=0,
                              text="Aloo Paratha",
                              height=1,
                              bg="lightblue",
                              font=("Arial", 16),
                              command=Clicked_2).grid(padx=5, pady=5)
        Button3 = Checkbutton(self.food_frame,
                              variable=food_button3,
                              onvalue=1,
                              offvalue=0,
                              text="Masala Dosa",
                              height=1,
                              bg="lightblue",
                              font=("Arial", 16),
                              command=Clicked_3).grid(padx=5, pady=5)
        Button4 = Checkbutton(self.food_frame,
                              variable=food_button4,
                              onvalue=1,
                              offvalue=0,
                              text="Medu Wada",
                              height=1,
                              bg="lightblue",
                              font=("Arial", 16),
                              command=Clicked_4).grid(padx=5, pady=5)
        Button5 = Checkbutton(self.food_frame,
                              variable=food_button5,
                              onvalue=1,
                              offvalue=0,
                              text="Idli Sambar",
                              height=1,
                              bg="lightblue",
                              font=("Arial", 16),
                              command=Clicked_5).grid(padx=5, pady=5)

        #------------------------------------------------------------------------------------------

        self.sec_frame = LabelFrame(self.win,
                                    text="Bill Area",
                                    font=("Arial", 16, "bold"),
                                    bg="lightblue",
                                    bd=6,
                                    relief=GROOVE)
        self.sec_frame.place(x=768, y=70, height=416, width=768)
        self.y_scroll = Scrollbar(self.sec_frame, orient="vertical")
        self.sec_frame_txt = Text(self.sec_frame,
                                  bg="white",
                                  yscrollcommand=self.y_scroll.set)
        self.y_scroll.config(command=self.sec_frame_txt.yview)
        self.y_scroll.pack(side=RIGHT, fill=Y)
        self.sec_frame_txt.pack(fill=BOTH, expand=TRUE, padx=150)

        #---------------------------------------Third---------------------------------------------#

        self.third_frame = Frame(self.win, bg="lightblue", bd=6, relief=GROOVE)
        self.third_frame.place(x=0, y=495, height=305, width=768)

        self.c_of_drinks = Label(self.third_frame,
                                 text="Cost of Drinks",
                                 font=("Arial, 15"),
                                 bg="lightblue").grid(row=0,
                                                      column=0,
                                                      padx=15,
                                                      pady=30)
        self.c_of_drinks_ent = Entry(self.third_frame,
                                     bd=5,
                                     textvariable=c_of_drinks,
                                     font=("Arial", 15),
                                     width=12).grid(row=0, column=1)
        self.c_of_food = Label(self.third_frame,
                               text="Cost of Food Items",
                               font=("Arial, 15"),
                               bg="lightblue").grid(row=1,
                                                    column=0,
                                                    padx=15,
                                                    pady=30)
        self.c_of_food_ent = Entry(self.third_frame,
                                   bd=5,
                                   textvariable=c_of_foods,
                                   font=("Arial", 15),
                                   width=12).grid(row=1, column=1)
        self.sub_total = Label(self.third_frame,
                               text="Sub Total",
                               font=("Arial, 15"),
                               bg="lightblue").grid(row=2,
                                                    column=0,
                                                    padx=15,
                                                    pady=30)
        self.sub_total_ent = Entry(self.third_frame,
                                   bd=5,
                                   textvariable=s_total,
                                   font=("Arial", 15),
                                   width=12).grid(row=2, column=1)
        self.tax = Label(self.third_frame,
                         text="Tax",
                         font=("Arial, 15"),
                         bg="lightblue").grid(row=0,
                                              column=2,
                                              padx=30.50,
                                              pady=30)
        self.tax_ent = Entry(self.third_frame,
                             bd=5,
                             textvariable=tax,
                             font=("Arial", 15),
                             width=12).grid(row=0, column=3)

        self.total_cost = Label(self.third_frame,
                                text="Total Cost",
                                font=("Arial, 15"),
                                bg="lightblue").grid(row=1,
                                                     column=2,
                                                     padx=30.50,
                                                     pady=30)
        self.total_cost_ent = Entry(self.third_frame,
                                    bd=5,
                                    textvariable=total_cost,
                                    font=("Arial", 15),
                                    width=12).grid(row=1, column=3)

        #----------------------------------Calculator----------------------------------------------#

        self.fourth_frame = Frame(self.win,
                                  bg="lightblue",
                                  bd=6,
                                  relief=GROOVE)
        self.fourth_frame.place(x=768, y=495, height=305, width=768)

        self.num_ent = Entry(self.fourth_frame,
                             bd=15,
                             background="lightblue",
                             textvariable=equation,
                             font=("Arial", 14),
                             width=49,
                             justify=RIGHT).grid(row=0, column=0)

        def press(num):
            global exp
            exp = exp + str(num)
            equation.set(exp)

        def equal():
            try:
                global exp
                y = str(eval(exp))
                equation.set(y)
                exp = ""
            except:
                messagebox.showinfo("Error", "Syntax Error")

        def clear():
            global exp
            exp = ""
            equation.set("")

        self.btn_1 = Button(self.fourth_frame,
                            bg="lightblue",
                            text="7",
                            bd=8,
                            width=11,
                            height=1,
                            font=("Arial", 14),
                            command=lambda: press(7)).place(x=0, y=54)
        self.btn_2 = Button(self.fourth_frame,
                            bg="lightblue",
                            text="8",
                            bd=8,
                            width=11,
                            height=1,
                            font=("Arial", 14),
                            command=lambda: press(8)).place(x=145, y=54)
        self.btn_3 = Button(self.fourth_frame,
                            bg="lightblue",
                            text="9",
                            bd=8,
                            width=11,
                            height=1,
                            font=("Arial", 14),
                            command=lambda: press(9)).place(x=290, y=54)
        self.btn_4 = Button(self.fourth_frame,
                            bg="lightblue",
                            text="/",
                            bd=8,
                            width=11,
                            height=1,
                            font=("Arial", 14),
                            command=lambda: press('/')).place(x=435, y=54)
        self.btn_5 = Button(self.fourth_frame,
                            bg="lightblue",
                            text="4",
                            bd=8,
                            width=11,
                            height=1,
                            font=("Arial", 14),
                            command=lambda: press(4)).place(x=0, y=108)
        self.btn_6 = Button(self.fourth_frame,
                            bg="lightblue",
                            text="5",
                            bd=8,
                            width=11,
                            height=1,
                            font=("Arial", 14),
                            command=lambda: press(5)).place(x=145, y=108)
        self.btn_7 = Button(self.fourth_frame,
                            bg="lightblue",
                            text="6",
                            bd=8,
                            width=11,
                            height=1,
                            font=("Arial", 14),
                            command=lambda: press(6)).place(x=290, y=108)
        self.btn_8 = Button(self.fourth_frame,
                            bg="lightblue",
                            text="*",
                            bd=8,
                            width=11,
                            height=1,
                            font=("Arial", 14),
                            command=lambda: press('*')).place(x=435, y=108)
        self.btn_9 = Button(self.fourth_frame,
                            bg="lightblue",
                            text="1",
                            bd=8,
                            width=11,
                            height=1,
                            font=("Arial", 14),
                            command=lambda: press(1)).place(x=0, y=162)
        self.btn_10 = Button(self.fourth_frame,
                             bg="lightblue",
                             text="2",
                             bd=8,
                             width=11,
                             height=1,
                             font=("Arial", 14),
                             command=lambda: press(2)).place(x=145, y=162)
        self.btn_11 = Button(self.fourth_frame,
                             bg="lightblue",
                             text="3",
                             bd=8,
                             width=11,
                             height=1,
                             font=("Arial", 14),
                             command=lambda: press(3)).place(x=290, y=162)
        self.btn_12 = Button(self.fourth_frame,
                             bg="lightblue",
                             text="-",
                             bd=8,
                             width=11,
                             height=1,
                             font=("Arial", 14),
                             command=lambda: press('-')).place(x=435, y=162)

        self.btn_13 = Button(self.fourth_frame,
                             bg="lightblue",
                             text="0",
                             bd=8,
                             width=11,
                             height=2,
                             font=("Arial", 14),
                             command=lambda: press(0)).place(x=0, y=216)
        self.btn_14 = Button(self.fourth_frame,
                             bg="lightblue",
                             text="clear",
                             bd=8,
                             width=11,
                             height=2,
                             font=("Arial", 14),
                             command=clear).place(x=145, y=216)
        self.btn_15 = Button(self.fourth_frame,
                             bg="lightblue",
                             text="=",
                             bd=8,
                             width=11,
                             height=2,
                             font=("Arial", 14),
                             command=equal).place(x=290, y=216)
        self.btn_16 = Button(self.fourth_frame,
                             bg="lightblue",
                             text="+",
                             bd=8,
                             width=11,
                             height=2,
                             font=("Arial", 14),
                             command=lambda: press('+')).place(x=435, y=216)

        #---------------------------------------------------------------------------------#
        def menu():
            self.menuWindow = Toplevel(win)
            self.menuWindow.geometry("765x490+0+0")
            self.menuWindow.configure(bg="#ADD8E6")
            self.menuWindow.title("Sai Menu Card")
            self.menu_title_label = Label(self.menuWindow,
                                          text="Sai Menu Card",
                                          font=("Arial", 35, "bold"),
                                          bg="lightblue",
                                          bd=8,
                                          relief=GROOVE)
            self.menu_title_label.pack(side=TOP, fill=X)
            self.drink_menu_frame = LabelFrame(self.menuWindow,
                                               bg="lightblue",
                                               bd=6,
                                               relief=GROOVE,
                                               text="Drinks",
                                               font=("Arial", 16, "bold"))
            self.drink_menu_frame.place(x=0, y=70, height=416, width=768 / 2)
            self.d1 = Label(self.drink_menu_frame,
                            text="Sprite: 65",
                            font=("Arial", 18),
                            bg="lightblue").grid(row=0,
                                                 column=0,
                                                 padx=15,
                                                 pady=20)
            self.d2 = Label(self.drink_menu_frame,
                            text="Fanta: 65",
                            font=("Arial", 18),
                            bg="lightblue").grid(row=1,
                                                 column=0,
                                                 padx=15,
                                                 pady=20)
            self.d3 = Label(self.drink_menu_frame,
                            text="CocoCola: 65",
                            font=("Arial", 18),
                            bg="lightblue").grid(row=2,
                                                 column=0,
                                                 padx=15,
                                                 pady=20)
            self.d4 = Label(self.drink_menu_frame,
                            text="Thums Up: 58",
                            font=("Arial", 18),
                            bg="lightblue").grid(row=3,
                                                 column=0,
                                                 padx=15,
                                                 pady=20)
            self.d5 = Label(self.drink_menu_frame,
                            text="Pepsi: 50",
                            font=("Arial", 18),
                            bg="lightblue").grid(row=4,
                                                 column=0,
                                                 padx=15,
                                                 pady=20)

            self.food_menu_frame = LabelFrame(self.menuWindow,
                                              bg="lightblue",
                                              bd=6,
                                              relief=GROOVE,
                                              text="Dishes",
                                              font=("Arial", 16, "bold"))
            self.food_menu_frame.place(x=384, y=70, height=416, width=768 / 2)
            self.f1 = Label(self.food_menu_frame,
                            text="Pav Bhaji: 40",
                            font=("Arial", 18),
                            bg="lightblue").grid(row=0,
                                                 column=0,
                                                 padx=15,
                                                 pady=20)
            self.f2 = Label(self.food_menu_frame,
                            text="Aloo Paratha: 30",
                            font=("Arial", 18),
                            bg="lightblue").grid(row=1,
                                                 column=0,
                                                 padx=15,
                                                 pady=20)
            self.f3 = Label(self.food_menu_frame,
                            text="Masala Dosa: 55",
                            font=("Arial", 18),
                            bg="lightblue").grid(row=2,
                                                 column=0,
                                                 padx=15,
                                                 pady=20)
            self.f4 = Label(self.food_menu_frame,
                            text="Medu Wada: 30",
                            font=("Arial", 18),
                            bg="lightblue").grid(row=3,
                                                 column=0,
                                                 padx=15,
                                                 pady=20)
            self.f5 = Label(self.food_menu_frame,
                            text="Idli Sambar: 40",
                            font=("Arial", 18),
                            bg="lightblue").grid(row=4,
                                                 column=0,
                                                 padx=15,
                                                 pady=20)

        def print_file():
            os.startfile(f"{path}\\{bill_no}.txt", "print")

        #-----------------BUTTONS----------------------------------------------------
        menu_btn = Button(self.fourth_frame,
                          text="Menu",
                          bd='3',
                          font=("Arial", 20, "bold"),
                          command=menu,
                          bg="lightblue",
                          width=10).grid(row=0, column=1, padx=2)

        total_btn = Button(self.fourth_frame,
                           text='Total',
                           bd='3',
                           font=("Arial", 20, "bold"),
                           command=total,
                           bg="lightGray",
                           width=10).grid(row=1, column=1, padx=2)

        reset_btn = Button(self.fourth_frame,
                           text='Reset',
                           bd='3',
                           font=("Arial", 20, "bold"),
                           command=reset,
                           bg="lightGray",
                           width=10).grid(row=2, column=1, padx=2)

        exit_btn = Button(self.fourth_frame,
                          text='Exit',
                          bd='3',
                          font=("Arial", 20, "bold"),
                          command=win.destroy,
                          bg="lightGray",
                          width=10).grid(row=3, column=1, padx=2)

        print_btn = Button(self.fourth_frame,
                           text='Print',
                           bd='3',
                           font=("Arial", 20, "bold"),
                           command=print_file,
                           bg="lightGray",
                           width=10).grid(row=4, column=1, padx=2)

        #-----------------------------////-----------------------------------------------


if __name__ == "__main__":
    main()
