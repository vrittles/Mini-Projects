import parser
import tkinter.messagebox as msgbox  # Added for displaying GCD and LCM results
from tkinter import *
root=Tk()
root.title("Calculator")

display=Entry(root)
display.grid(row=1,columnspan=6,sticky=W+E)

#get the user input and place it in the textfield
# Input fields for two numbers
num1_entry = Entry(root)
num1_entry.grid(row=6, column=0)
num2_entry = Entry(root)
num2_entry.grid(row=6, column=2)


i=0
def get_variables(num):
    global i
    display.insert(i,num)
    i+=1

def clear_all():
    display.delete(0,END)

def undo():
    entire_string=display.get()
    if len(entire_string):
        new_string=entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0,"Error")

def get_operation(opr):
    global i
    length=len(opr)
    display.insert(i,opr)
    i+=length

def calculate():
    entire_string=display.get()
    try:
        a=parser.expr(entire_string).compile()
        result=eval(a)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"error")

# Function to find the GCD of two numbers using Euclidean algorithm
def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to find the LCM of two numbers
def find_lcm(a, b):
    return (a * b) // find_gcd(a, b)

# Calculate and display GCD and LCM
def calculate_gcd_lcm():
    try:
        num1 = int(num1_entry.get())
        num2 = int(num2_entry.get())
        gcd = find_gcd(num1, num2)
        lcm = find_lcm(num1, num2)
        msgbox.showinfo("Result", f"The GCD of {num1} and {num2} is: {gcd}\n"
                                   f"The LCM of {num1} and {num2} is: {lcm}")
    except ValueError:
        msgbox.showerror("Error", "Please enter valid numbers for GCD and LCM calculation.")





#adding button to the calculator

Button(root,text="1",command=lambda :get_variables(1)).grid(row=2,column=0)
Button(root,text="2",command=lambda :get_variables(2)).grid(row=2,column=1)
Button(root,text="3",command=lambda :get_variables(3)).grid(row=2,column=2)
Button(root,text="4",command=lambda :get_variables(4)).grid(row=3,column=0)
Button(root,text="5",command=lambda :get_variables(5)).grid(row=3,column=1)
Button(root,text="6",command=lambda :get_variables(6)).grid(row=3,column=2)
Button(root,text="7",command=lambda :get_variables(7)).grid(row=4,column=0)
Button(root,text="8",command=lambda :get_variables(8)).grid(row=4,column=1)
Button(root,text="9",command=lambda :get_variables(9)).grid(row=4,column=2)
Button(root,text="0",command=lambda :get_variables(0)).grid(row=5,column=0)

Button(root,text="AC",command=lambda :clear_all()).grid(row=5,column=1)
Button(root,text="=",command=lambda :calculate()).grid(row=5,column=2)
Button(root,text="->",command=lambda :undo()).grid(row=2,column=3)

Button(root,text="+",command=lambda :get_operation('+')).grid(row=3,column=3)
Button(root,text="-",command=lambda :get_operation('-')).grid(row=4,column=3)
Button(root,text="*",command=lambda :get_operation('*')).grid(row=5,column=3)
Button(root,text="/",command=lambda :get_operation('/')).grid(row=2,column=4)
Button(root,text="pi",command=lambda :get_operation('*3.14')).grid(row=3,column=4)
Button(root,text="%",command=lambda :get_operation('%')).grid(row=4,column=4)
Button(root,text="(",command=lambda :get_operation('(')).grid(row=5,column=4)
Button(root,text=")",command=lambda :get_operation(')')).grid(row=2,column=5)
Button(root,text="exp",command=lambda :get_operation('**')).grid(row=3,column=5)
Button(root,text="x!").grid(row=4,column=5)
Button(root,text="^2",command=lambda :get_operation('**2')).grid(row=5,column=5)

# Button to calculate GCD and LCM
Button(root, text="Calculate GCD/LCM", command=calculate_gcd_lcm).grid(row=6, column=4)





root.mainloop()