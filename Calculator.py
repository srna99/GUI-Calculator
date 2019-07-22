import tkinter
import math


class Calculator:
    expression = ""
    is_solved = True

    def __init__(self, window: tkinter.Tk):

        window.title("Calculator")
        window.geometry("275x440")
        window.configure(bg="#e7e6e1", padx=5, pady=10)

        self.display = tkinter.StringVar(window, "0")

        display_label = tkinter.Label(window, textvariable=self.display, font=("Arial", 14),
                                      anchor="e", height=2, width=20, padx=9, bg="#e7e6e1",
                                      borderwidth=3, relief="ridge", fg="#222222")
        display_label.grid(row=0, column=0, columnspan=4, padx=10)

        button1 = tkinter.Button(window, text="1", height=3, width=6, activebackground="#e8e5d1",
                                 bg="#f9f6e2", fg="#222222", command=lambda: self.number_pressed("1"))
        button1.grid(row=6, column=0, pady=5)

        button2 = tkinter.Button(window, text="2", height=3, width=6, activebackground="#e8e5d1",
                                 bg="#f9f6e2", fg="#222222", command=lambda: self.number_pressed("2"))
        button2.grid(row=6, column=1)

        button3 = tkinter.Button(window, text="3", height=3, width=6, activebackground="#e8e5d1",
                                 bg="#f9f6e2", fg="#222222", command=lambda: self.number_pressed("3"))
        button3.grid(row=6, column=2)

        button4 = tkinter.Button(window, text="4", height=3, width=6, activebackground="#e8e5d1",
                                 bg="#f9f6e2", fg="#222222", command=lambda: self.number_pressed("4"))
        button4.grid(row=5, column=0)

        button5 = tkinter.Button(window, text="5", height=3, width=6, activebackground="#e8e5d1",
                                 bg="#f9f6e2", fg="#222222", command=lambda: self.number_pressed("5"))
        button5.grid(row=5, column=1)

        button6 = tkinter.Button(window, text="6", height=3, width=6, activebackground="#e8e5d1",
                                 bg="#f9f6e2", fg="#222222", command=lambda: self.number_pressed("6"))
        button6.grid(row=5, column=2)

        button7 = tkinter.Button(window, text="7", height=3, width=6, activebackground="#e8e5d1",
                                 bg="#f9f6e2", fg="#222222", command=lambda: self.number_pressed("7"))
        button7.grid(row=4, column=0, pady=5)

        button8 = tkinter.Button(window, text="8", height=3, width=6, activebackground="#e8e5d1",
                                 bg="#f9f6e2", fg="#222222", command=lambda: self.number_pressed("8"))
        button8.grid(row=4, column=1)

        button9 = tkinter.Button(window, text="9", height=3, width=6, activebackground="#e8e5d1",
                                 bg="#f9f6e2", fg="#222222", command=lambda: self.number_pressed("9"))
        button9.grid(row=4, column=2)

        button0 = tkinter.Button(window, text="0", height=3, width=6, activebackground="#e8e5d1",
                                 bg="#f9f6e2", fg="#222222", command=lambda: self.number_pressed("0"))
        button0.grid(row=7, column=0)

        decimal_button = tkinter.Button(window, text=".", height=3, width=6, activebackground="#e8e5d1",
                                        bg="#f9f6e2", fg="#222222",
                                        command=lambda: self.number_pressed("."))
        decimal_button.grid(row=7, column=1)

        sign_button = tkinter.Button(window, text="±", height=3, width=6, activebackground="#e8e5d1",
                                     bg="#f9f6e2", fg="#222222",
                                     command=lambda: self.function_pressed("±"))
        sign_button.grid(row=7, column=2)

        divide_button = tkinter.Button(window, text="÷", height=3, width=6, activebackground="#446a84",
                                       activeforeground="#eeeeee", bg="#557b95", fg="#eeeeee",
                                       command=lambda: self.function_pressed("/"))
        divide_button.grid(row=3, column=3)

        multiply_button = tkinter.Button(window, text="×", height=3, width=6, activebackground="#446a84",
                                         activeforeground="#eeeeee", bg="#557b95", fg="#eeeeee",
                                         command=lambda: self.function_pressed("*"))
        multiply_button.grid(row=4, column=3)

        subtract_button = tkinter.Button(window, text="-", height=3, width=6, activebackground="#446a84",
                                         activeforeground="#eeeeee", bg="#557b95", fg="#eeeeee",
                                         command=lambda: self.function_pressed("-"))
        subtract_button.grid(row=5, column=3)

        add_button = tkinter.Button(window, text="+", height=3, width=6, activebackground="#446a84",
                                    activeforeground="#eeeeee", bg="#557b95", fg="#eeeeee",
                                    command=lambda: self.function_pressed("+"))
        add_button.grid(row=6, column=3)

        equal_button = tkinter.Button(window, text="=", height=3, width=6, activebackground="#446a84",
                                      activeforeground="#eeeeee", bg="#557b95", fg="#eeeeee",
                                      command=self.solve)
        equal_button.grid(row=7, column=3)

        clear_button = tkinter.Button(window, text="AC", height=3, width=6, activebackground="#aaaba8",
                                      bg="#c1c0b9", fg="#222222", command=self.clear)
        clear_button.grid(row=2, column=3)

        percent_button = tkinter.Button(window, text="%", height=3, width=6, activebackground="#aaaba8",
                                        bg="#c1c0b9", fg="#222222",
                                        command=lambda: self.function_pressed("%"))
        percent_button.grid(row=3, column=0)

        square_button = tkinter.Button(window, text="x²", height=3, width=6, activebackground="#aaaba8",
                                       bg="#c1c0b9", fg="#222222",
                                       command=lambda: self.function_pressed("x²"))
        square_button.grid(row=3, column=1)

        sqrt_button = tkinter.Button(window, text="√", height=3, width=6, activebackground="#aaaba8",
                                     bg="#c1c0b9", fg="#222222",
                                     command=lambda: self.function_pressed("√"))
        sqrt_button.grid(row=3, column=2)

        log_button = tkinter.Button(window, text="log", height=3, width=6, activebackground="#aaaba8",
                                    bg="#c1c0b9", fg="#222222",
                                    command=lambda: self.function_pressed("log"))
        log_button.grid(row=2, column=0, pady=5)

        factorial_button = tkinter.Button(window, text="x!", height=3, width=6,
                                          activebackground="#aaaba8", bg="#c1c0b9", fg="#222222",
                                          command=lambda: self.function_pressed("x!"))
        factorial_button.grid(row=2, column=1)

        fraction_button = tkinter.Button(window, text="⅟ x", height=3, width=6,
                                         activebackground="#aaaba8", bg="#c1c0b9", fg="#222222",
                                         command=lambda: self.function_pressed("1/x"))
        fraction_button.grid(row=2, column=2)

    def number_pressed(self, number):

        if self.is_solved:
            if number == ".":
                number = "0."

            self.expression = number
            self.display.set(self.expression)
            self.is_solved = False
        else:
            if number == ".":
                if not self.expression[-1].isdigit():
                    number = "0."
                else:
                    number_list = self.expression.replace("+", " ").replace("-", " ").replace("/", " ") \
                        .replace("*", " ").split()

                    current_number = number_list[-1]

                    is_int = math.floor(float(current_number)) == int(current_number)

                    if not is_int:
                        return

            self.expression += number
            self.display.set(self.expression)

    def function_pressed(self, symbol):

        if self.expression != "":
            self.is_solved = False
            if symbol == "+" or symbol == "-" or symbol == "*" or symbol == "/":
                self.expression += symbol
                self.display.set(self.expression)
            else:
                if symbol == "±":
                    self.expression += "*-1"
                elif symbol == "x²":
                    try:
                        self.expression = str(round(pow(float(self.expression), 2), 7))
                    except OverflowError:
                        self.display.set("error")
                        self.expression = ""
                elif symbol == "√":
                    self.expression = str(round(math.sqrt(abs(float(self.expression))), 7))
                elif symbol == "%":
                    self.expression += "/100"
                elif symbol == "log":
                    pass
                elif symbol == "1/x":
                    pass
                elif symbol == "x!":
                    pass

                self.solve()

    def solve(self):

        try:
            self.display.set(str(round(eval(self.expression), 7)))
            self.expression = self.display.get()
            self.is_solved = True
        except (SyntaxError, ZeroDivisionError, ValueError, OverflowError):
            self.display.set("error")
            self.expression = ""

    def clear(self):

        self.expression = ""
        self.display.set("0")


# -- Main Driver Code --

gui = tkinter.Tk()

calculator = Calculator(gui)

gui.mainloop()
