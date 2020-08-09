import tkinter as tk
from tkinter import ttk
class MathIO():
    @staticmethod
    def clear_textbox(textbox):
        textbox['state']= 'normal'
        textbox.delete(1.0, tk.END)
        textbox['state'] = disabled
    @staticmethod
    def write_sum_to_textbox(num1, num2, textbox1):
        textbox1['state'] = 'normal'
        num = MathProcessor.add_with_parameters(num1, num2)
        text = str.format('The sum of {num1} and {num2} is {num}\n',
                          num1=num1, num2=num2, num=num)
        textbox1.insert(tk.END, text)
        textbox1['state'] = 'disabled'
    @staticmethod
    def write_diff_to_textbox(num1, num2, textbox1):
        textbox1['state']= 'normal'
        num = MathProcessor.subtract_with_parameters(num1,num2)
        text = str.format('The difference of {num1} and {num2} is {num}\n',
                          num1=num1, num2=num2, num=num)
        textbox1.insert(tk.END, text)
        textbox1['state'] = 'disabled'
    @staticmethod
    def write_product_to_textbox(num1, num2, textbox1):
        textbox1['state'] = 'normal'
        num = MathProcessor.multiply_with_parameters(num1, num2)
        text = str.format('The product of {num1} and {num2} is {num}\n',
                          num1=num1, num2=num2, num=num)
        textbox1.insert(tk.END, text)
        textbox1['state'] = 'disabled'

    @staticmethod
    def write_quotient_to_textbox(num1, num2, textbox1):
        textbox1['state']= 'normal'
        num = MathProcessor.divide_with_parameters(num1,num2)
        text = str.format('The quotient of {num1} and {num2} is {num}\n',
                          num1=num1, num2=num2, num=num)
        textbox1.insert(tk.END, text)
        textbox1['state'] = 'disabled'
class MathProcessor():
    @staticmethod
    def add_with_parameters(n1, n2):
        return n1+n2
    @staticmethod
    def subtract_with_parameters(n1, n2):
        return n1-n2
    @staticmethod
    def multiply_with_parameters(n1, n2):
        return n1*n2
    @staticmethod
    def divide_with_parameters(n1, n2):
        return n1/n2
class MainWindow(object):

    # -- window_root (tk.TK)
    #   -- lbl_math_info (tk.label)
    #   -- txt_first_number (ttk.entry)
    #   -- txt_second_number (ttk.entry)
    #   -- btn_add (ttk.add)
    #   -- btn_subtract (ttk.subtract)
    #   -- btn_multiply (ttk.multiply)
    #   -- btn_divide (ttk.divide)
    @staticmethod
    def create_main_window():
        application_window = tk.Tk()  # creates a root node
        application_window.geometry("500x200+400+100")  # Define the size of the window
        application_window.title("Math!")  # add title to window
        # Create a label object in the window and get a reference
        lbl_your_label = ttk.Label(application_window, text="Select a math operation!")
        # add label to the root container using the pack layout manager method
        lbl_your_label.grid(row=1, column=1, sticky=tk.NW, padx=5, pady=5)

        # create add button
        btn_add = ttk.Button(application_window, text="Add", width=10)  # button def
        btn_add.grid(row=3, column=1, sticky=tk.NW, padx=10, pady=5)  # button on grid
        btn_add['command'] = lambda: MathIO.write_sum_to_textbox(float(txt_first_number.get()),
        float(txt_second_number.get()),mtx_results)

        # create subtract button
        btn_subtract = ttk.Button(application_window, text="Subtract", width=10)  # button def
        btn_subtract.grid(row=3, column=2, sticky=tk.NW, padx=10, pady=5)  # button on grid
        btn_subtract['command'] = lambda: MathIO.write_diff_to_textbox(float(txt_first_number.get()),
        float(txt_second_number.get()),mtx_results)

        # create multiply button
        btn_multiply = ttk.Button(application_window, text="Multiply", width=10)  # button def
        btn_multiply.grid(row=3, column=3, sticky=tk.NW, padx=10, pady=5)  # button on grid
        btn_multiply['command'] = lambda: MathIO.write_product_to_textbox(float(txt_first_number.get()),
        float(txt_second_number.get()),mtx_results)

        # create divide button
        btn_divide = ttk.Button(application_window, text="Divide", width=10)  # button def
        btn_divide.grid(row=3, column=4, sticky=tk.NW, padx=10, pady=5)  # button on grid
        btn_divide['command'] = lambda: MathIO.write_quotient_to_textbox(float(txt_first_number.get()),
        float(txt_second_number.get()),mtx_results)

        # create first text entry
        lbl_first_number = ttk.Label(
            application_window,
            text='First Number:',
            width=20,
            anchor =tk.W
        )
        lbl_first_number.grid(row=2,column=1,sticky=tk.W)
        txt_first_number = ttk.Entry(application_window, width=10)
        txt_first_number.grid(row=2, column=1,sticky=tk.E)
        txt_first_number.insert(0,"0.00")

        # create second entry
        lbl_second_number = ttk.Label(
            application_window,
            text='Second Number:',
            width=20,
            anchor =tk.E
        )
        lbl_second_number.grid(row=2,column=2,sticky=tk.E)
        txt_second_number = ttk.Entry(application_window, width=10)
        txt_second_number.grid(row=2, column=3, sticky=tk.W,)
        txt_second_number.insert(0,"0.00")
        # create a multi-line textbox
        mtx_results = tk.Text(width=50, height=5)
        mtx_results.grid(row=4,
        column=1,
        sticky=tk.N,
        columnspan=4,
        padx=10,
        pady=10)
        return application_window
if __name__=='__main__':
    mw = MainWindow.create_main_window()
    mw.mainloop()
