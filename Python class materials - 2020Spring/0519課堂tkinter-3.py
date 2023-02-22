ll#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 15:53:21 2020

@author: liuqingxuan
"""
import tkinter as tk
import tkinter.messagebox

window=tk.Tk()
window.title('Convert kilometers to miles')
window.geometry("300x100+250+150")

def k2mconvert():
        # Get the value entered by the user into the
        # kilo_entry widget.
        kilo = float(entry.get())

        # Convert kilometers to miles.
        miles = kilo * 0.6214

        # Display the results in an info dialog box.
        tkinter.messagebox.showinfo('Results',
                                    str(kilo) +
                                    ' kilometers is equal to ' +
                                    str(miles) + ' miles.')
#標示文字
label = tk.Label(window, text="Enter a distance in kilometers: ")
label.pack()

#輸入欄位
entry = tk.Entry(window, width=20)
entry.pack()

#按鈕
button = tk.Button(window, text = "Convert", command=k2mconvert)
button.pack(side='top')

window.mainloop()