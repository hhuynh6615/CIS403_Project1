from tkinter import *

root = Tk()
root.title('Project 1 - GUI Calculator')
root.geometry("500x600")

label_frame = LabelFrame(root, text="Mortgage Calculator")
label_frame.pack(pady=30)

def main():
    if priceEntry.get() and downEntry.get() and interestEntry.get() and termEntry.get():
        years = int(termEntry.get())
        months = years * 12
        rate = float(interestEntry.get())
        downPay = float(downEntry.get())
        price = int(priceEntry.get())
        downPayment = downPay * price
        loan = price - downPayment

        monthlyRate = rate / 100 / 12
        payment = (monthlyRate / (1 - (1 + monthlyRate) ** (-months))) * loan
        payment = f"{payment:,.2f}"
        paymentLabel.config(text=f"{payment}")
    else:
        paymentLabel.config(text="You forgot to enter something.")

myFrame = Frame(label_frame)
myFrame.pack(pady=10, padx=20)

price = Label(myFrame, text="Price Amount: ")
priceEntry = Entry(myFrame, font=("Arial", 18))

down = Label(myFrame, text="Down Payment: ")
downEntry = Entry(myFrame, font=("Arial", 18))

interest = Label(myFrame, text="Interest Rate: ")
interestEntry = Entry(myFrame, font=("Arial", 18))

term = Label(myFrame, text="Terms: ")
termEntry = Entry(myFrame, font=("Arial", 18))

price.grid(row=0, column=0)
priceEntry.grid(row=0, column=1, pady=20)

down.grid(row=1, column=0)
downEntry.grid(row=1, column=1)

interest.grid(row=2, column=0)
interestEntry.grid(row=2, column=1, pady=20)

term.grid(row=3, column=0)
termEntry.grid(row=3, column=1)

button = Button(label_frame, text="Calculate")
button.pack(pady=20)

paymentLabel = Label(root, text="", font=("Arial", 18))
paymentLabel.pack(pady=20)

root.mainloop()