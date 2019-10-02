#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.font as font
import random as rn


class Bar:
    def __init__(self, height, order, id):
        self.height = height
        self.order = order
        self.id = id

    def change_id(self, id):
        self.id = id

    def change_height(self, height):
        self.height = height


bar_list = []
bars = []
CANVAS_WIDTH = 1001
CANVAS_HEIGHT = 500
spacing = 0
population = 101


def bar(order, height, id, shoop):
    x = str(id)
    x1 = (order-1) * (10)
    x2 = x1 + 10
    y2 = height * 5
    shoop.create_rectangle(x1, 0, x2, y2, tag=x, fill='orange', outline="")


def update_bar(id1, id2):
    w = canvas.coords(id1)
    y = canvas.coords(id2)
    if not w or not y or y[3] <= 0 or w[3] <= 0:
        canvas.itemconfig(id1, fill='red')
        canvas.itemconfig(id2, fill='blue')

    else:
        temp_id = id2
        canvas.coords(id1, y[0], 0, y[2], w[3])
        canvas.coords(id2, w[0], 0, w[2], y[3])
        canvas.itemconfig(id1, fill='red')
        canvas.itemconfig(id2, fill='blue')
        canvas.itemconfig(id2, tag=id1)
        canvas.itemconfig(id1, tag=temp_id)


def overtake(id, height):
    w = canvas.coords(id)
    if not w or w[3] <= 0:
        pass
    else:
        canvas.coords(id, w[0], 0, w[2], height*5)


def update_key(id):
    canvas.itemconfig(id, fill='green')


def finished():
    for i in range(len(bar_list)):
        canvas.itemconfig(bar_list[i].id, fill='dark turquoise')


def test_thing(id):
    canvas.itemconfig(id, fill='red')


def test_thing2(id):
    canvas.itemconfig(id, fill='blue')


def insertion_sort(array):
    for i in range(1, len(array)):
        canvas.after(0, update_key(array[i].id))
        canvas.update()
        key = array[i].height
        j = i - 1
        while j >= 0 and key < array[j].height:
            canvas.after(5, update_bar(array[j].id, array[j+1].id))
            canvas.update()
            array[j+1].height = array[j].height
            temp = array[j+1].id
            array[j+1].id = array[j].id
            array[j].id = temp
            j -= 1

        array[j + 1].height = key


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i].height < right[j].height:
                canvas.after(0, test_thing(left[i].id))
                canvas.update()
                arr[k] = left[i]
                i += 1
            else:
                canvas.after(0, test_thing2(right[j].id))
                canvas.update()
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            canvas.after(0, test_thing(left[i].id))
            canvas.update()
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            canvas.after(0, test_thing2(right[j].id))
            canvas.update()
            arr[k] = right[j]
            j += 1
            k += 1
    for q in range(len(arr)):
        canvas.after(10, overtake(q, arr[q].height))
        canvas.update()


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def partition(arr, low, high):
    pivot = arr[high].height
    canvas.after(20, update_key(arr[high].id))
    g = (low - 1)
    for j in range(low, high):
        if arr[j].height < pivot:
            g += 1
            arr[g], arr[j] = arr[j], arr[g]
            canvas.after(20, update_bar(arr[g].id, arr[j].id))
            canvas.update()
    canvas.after(10, update_bar(arr[g+1].id, arr[high].id))
    canvas.update()
    arr[g+1], arr[high] = arr[high], arr[g+1]
    return g + 1


def gui_start_quick():
    start_button = tk.Button(root, text="QUICK", command=start_call_quick, bd=0, font=my_font, bg='deep sky blue')
    start_button.pack()
    start_button.place(x=10, y=660, height=50, width=333)


def gui_start_merge():
    start_button = tk.Button(root, text="MERGE", command=start_call_merge, bd=0, font=my_font, bg='light slate blue')
    start_button.pack()
    start_button.place(x=343, y=660, height=50, width=333)


def gui_start_insertion():
    start_button = tk.Button(root, text="INSERTION", command=start_call_insertion, bd=0, font=my_font, bg='aquamarine')
    start_button.pack()
    start_button.place(x=676, y=660, height=50, width=333)


def gui_generator():
    generate_button = tk.Button(root, text="GENERATE", command=create_array, bd=0, font=my_font, bg='royal blue')
    generate_button.pack()
    generate_button.place(x=10, y=580, height=50, width=1000)


def gui_slider():
    scale = tk.Scale(root, variable=var, tickinterval=10, from_=10, to=100, orient=tk.HORIZONTAL, length=1000,
                     resolution=10, showvalue=0, width=30)
    scale.pack()
    scale.place(x=10, y=505)


def start_call_quick():
    quick_sort(bar_list, 1, len(bar_list)-1)
    canvas.after(0, finished())
    canvas.update()


def start_call_merge():
    merge_sort(bar_list)
    canvas.after(0, finished())
    canvas.update()


def start_call_insertion():
    insertion_sort(bar_list)
    canvas.after(0, finished())
    canvas.update()


def create_array():
    bar_list.clear()
    total = var.get() + 1
    for x in range(0, total):
        bar_list.append(Bar(rn.randint(1, 100), x, x))
    change_bars()


def change_bars():
    size = 1000.3*(var.get()**(-1))
    print(size)
    for i in range(1, population):
        canvas.coords(i, 0, 0, 0, 0)

    for i in range(1, len(bar_list)):
        canvas.coords(i, (i-1) * size, 0, ((i-1) * size) + size, bar_list[i].height*5)
        canvas.itemconfig(i, fill="orange")


root = tk.Tk()
my_font = font.Font(root, family="Helvetica", size=15, weight='bold')
root.title("Sorting Visualizer")
var = tk.IntVar(root)
root.geometry("1020x800+250+250")
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, background='gray15')
canvas.pack()

for x in range(0, population):
    bar_list.append(Bar(rn.randint(1, 100), x, x))

for i in range(1, len(bar_list)):
    bar(i, bar_list[i].height, bar_list[i].id, canvas)

gui_start_quick()
gui_start_merge()
gui_start_insertion()
gui_slider()
gui_generator()

root.mainloop()