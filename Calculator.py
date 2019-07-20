import tkinter


class Calculator:
    expression = ""

    def __init__(self, window):
        window.title("Calculator")
        window.geometry("260x305")
        window.configure(bg="#e7e6e1")

        self.display = tkinter.StringVar(window, "0")

        self.display_label = tkinter.Label(window, textvariable=self.display, font=("Arial", 13),
                                           anchor="e", height=2, width=25, padx=5, bg="#e7e6e1",
                                           borderwidth=3, relief="ridge", fg="#222222")
        self.display_label.grid(row=0, column=0, columnspan=4, padx=10, pady=5)

        button1 = tkinter.Button(window, text="1", height=3, width=5, bg="#f9f6e2", fg="#222222")
        button1.grid(row=4, column=0)

        button2 = tkinter.Button(window, text="2", height=3, width=5, bg="#f9f6e2", fg="#222222")
        button2.grid(row=4, column=1)

        button3 = tkinter.Button(window, text="3", height=3, width=5, bg="#f9f6e2", fg="#222222")
        button3.grid(row=4, column=2)

        button4 = tkinter.Button(window, text="4", height=3, width=5, bg="#f9f6e2", fg="#222222")
        button4.grid(row=3, column=0, pady=5)

        button5 = tkinter.Button(window, text="5", height=3, width=5, bg="#f9f6e2", fg="#222222")
        button5.grid(row=3, column=1)

        button6 = tkinter.Button(window, text="6", height=3, width=5, bg="#f9f6e2", fg="#222222")
        button6.grid(row=3, column=2)

        button7 = tkinter.Button(window, text="7", height=3, width=5, bg="#f9f6e2", fg="#222222")
        button7.grid(row=2, column=0)

        button8 = tkinter.Button(window, text="8", height=3, width=5, bg="#f9f6e2", fg="#222222")
        button8.grid(row=2, column=1)

        button9 = tkinter.Button(window, text="9", height=3, width=5, bg="#f9f6e2", fg="#222222")
        button9.grid(row=2, column=2)

        button0 = tkinter.Button(window, text="0", height=3, width=5, bg="#f9f6e2", fg="#222222")
        button0.grid(row=5, column=1, pady=5)

        divide_button = tkinter.Button(window, text="/", height=3, width=5, bg="#557b95", fg="#eeeeee")
        divide_button.grid(row=2, column=3)

        multiply_button = tkinter.Button(window, text="*", height=3, width=5, bg="#557b95", fg="#eeeeee")
        multiply_button.grid(row=3, column=3)

        subtract_button = tkinter.Button(window, text="-", height=3, width=5, bg="#557b95", fg="#eeeeee")
        subtract_button.grid(row=4, column=3)

        add_button = tkinter.Button(window, text="+", height=3, width=5, bg="#557b95", fg="#eeeeee")
        add_button.grid(row=5, column=3)

        equal_button = tkinter.Button(window, text="=", height=3, width=5, bg="#c1c0b9", fg="#222222")
        equal_button.grid(row=5, column=2)

        clear_button = tkinter.Button(window, text="AC", height=3, width=5, bg="#c1c0b9", fg="#222222")
        clear_button.grid(row=5, column=0)


# -- Main Driver Code --

gui = tkinter.Tk()

Calculator(gui)

gui.mainloop()
