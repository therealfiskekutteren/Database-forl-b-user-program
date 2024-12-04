import tkinter as tk

# def on_button_click():
    # print(entry.get())

root = tk.Tk()
label1 = tk.Label(root, text="Label 1")
label2 = tk.Label(root, text="Label 2")
label3 = tk.Label(root, text="Label 3")
label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=0, column=2, columnspan=2)
# entry = tk.Entry(root)
# entry.pack()
# button = tk.Button(root,text="click deez", command=on_button_click)
# button.pack()
root.mainloop()