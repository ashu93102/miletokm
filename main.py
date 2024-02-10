import tkinter

window = tkinter.Tk()
window.title("Mile convertor")
window.config(pady=10, padx=20)


def mile_to_km():
    value = int(user_input.get())
    km = value * 1.609
    answer = str(km)
    kilo_res.config(text=answer)


# Entry
user_input = tkinter.Entry(width=10)
user_input.insert(tkinter.END, string="Miles.")
user_input.grid(column=1, row=0)

mile = tkinter.Label(text="Miles")
mile.config(padx=0)
mile.grid(column=2, row=0)

answer_lab = tkinter.Label(text=f"Is equal to", font=("Arial", 12, "bold"))
answer_lab.config(padx=5, pady=5)
answer_lab.grid(column=1, row=1)

kilo_res = tkinter.Label(text="0")
kilo_res.grid(column=2, row=1)


kilo_lab = tkinter.Label(text="Km")
kilo_lab.grid(column=3, row=1)

cal_button = tkinter.Button(text="Calculate", command=mile_to_km)
cal_button.grid(column=2, row=2)

window.mainloop()
