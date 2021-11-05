from tkinter import *
import json
import socket


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.size = StringVar()
        self.toppings = []
        self.prices = {"medium": 0, "large": 0, "xlarge": 0,
                       "sausage": 0, "pepperoni": 0, "chicken": 0, "mushroom": 0, "black olive": 0,
                       "green pepper": 0, "red pepper": 0, "onion": 0}
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = 5421
        self.host = socket.gethostbyname("localhost")
        self.socket.connect((self.host, self.port))
        data = bytes.decode(self.socket.recv(1024))
        print(data)

        self.socket.send(str.encode('p'))
        self.prices = json.loads(bytes.decode(self.socket.recv(1024)))
        self.socket.send(str.encode('t'))
        self.toppings = json.loads(bytes.decode(self.socket.recv(1024)))
        self.socket.send(str.encode('q'))

        self.chk = list(self.toppings)
        self.chkVar = list(self.toppings)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.lbl_title = Label(self, text="Python Pizza Calculator", font="Arial 13 bold")
        self.lbl_title.grid(row=0, column=0, columnspan=3, sticky="W")

        self.lbl_ss = Label(self, text="Select Size", font="Arial 11 normal")
        self.lbl_ss.grid(row=1, column=0, sticky="W")

        self.rad_med = Radiobutton(self, text="Medium", font="Arial 11 normal", variable=self.size, value="Medium")
        self.rad_med.grid(row=2, column=0, sticky="W")

        self.rad_large = Radiobutton(self, text="Large", font="Arial 11 normal", variable=self.size, value="Large")
        self.rad_large.grid(row=2, column=1, sticky="W")

        self.rad_xlarge = Radiobutton(self, text="Extra Large", font="Arial 11 normal", variable=self.size,
                                      value="xLarge")
        self.rad_xlarge.grid(row=2, column=2, sticky="W")

        self.rad_med.select()

        self.lbl_empty = Label(self, text=" ")
        self.lbl_empty.grid(row=3, column=0)

        self.lbl_st = Label(self, text="Select toppings:", font="Arial 11 normal")
        self.lbl_st.grid(row=4, column=0, sticky="W")
        cur_row = 4

        for i in range(len(self.toppings)):
            cur_row += 1
            self.chkVar[i] = BooleanVar()
            self.chk[i] = Checkbutton(self, text=self.toppings[i], variable=self.chkVar[i], font="Arial 11 normal")
            self.chk[i].grid(row=cur_row, column=0, sticky="W")

        cur_row += 1
        self.lbl_empty = Label(self, text=" ", font='Arial 11 bold')
        self.lbl_empty.grid(row=cur_row, column=0, sticky='W')

        cur_row += 1
        self.btn_reset = Button(self, text="Reset ", font='Arial 11 bold', width=12, command=self.reset)
        self.btn_reset.grid(row=cur_row, column=0, sticky=E)

        self.btn_calc = Button(self, text="Calculate price ", font='Arial 11 bold', width=12, command=self.calc)
        self.btn_calc.grid(row=cur_row, column=1, sticky=W)

        cur_row += 1
        self.lbl_total = Label(self, text="Total: ", font='Arial 11 bold')
        self.lbl_total.grid(row=cur_row, column=0, sticky='E')

        self.ent_total = Entry(self, text=" ")
        self.ent_total.grid(row=cur_row, column=1, sticky='W')

    def reset(self):
        self.ent_total.delete(0, END)
        self.rad_med.select()
        for i in range(len(self.toppings)):
            self.chk[i].deselect()

    def calc(self):
        self.ent_total.delete(0, END)
        selected_toppings = []
        size = self.size.get()
        print(self.size.get())
        total = 0
        total_toppings = 0
        total += self.prices[size]

        for i in range(len(self.toppings)):
            if self.chkVar[i].get():
                selected_toppings.append(self.toppings[i])
        #                 print(self.toppings[i])
        print(selected_toppings)

        for i in selected_toppings:
            total_toppings += self.prices[i]

        if size == 'medium':
            total += (total_toppings)
        elif size == 'large':
            total += (total_toppings * 1.2)
        elif size == 'xlarge':
            total += (total_toppings * 1.5)

        self.ent_total.insert(0, "{:,.2f}".format(total))


Window = Tk()
Window.title("Test Application Window")
Window.geometry("370x470")
app = Application(Window)
app.mainloop()
