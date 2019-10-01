#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
import random as rn


class Bar:
    def __init__(self, height, order, id):
        self.height = height
        self.order = order
        self.id = id

    def change_id(self, id):
        self.id = id


bar_list = []


CANVAS_WIDTH = 900
CANVAS_HEIGHT = 600

for x in range(0, 60):
    bar_list.append(Bar(rn.randint(1, 100), x, x))

width = 10
spacing = 5


def bar(order, height, id):
    x1 = order * (width + spacing)
    x2 = x1 + width
    y2 = height * 5
    canvas.create_rectangle(x1, 0, x2, y2, tag=id+1)


def update_bar(id1, id2):
    w = canvas.coords(id1)
    y = canvas.coords(id2)

    if not w or not y or y[3] <= 0 or w[3] <= 0:
        pass
    else:
        temp_id = id2
        #canvas.itemconfig(id1, fill='blue')
        #canvas.itemconfig(id2, fill='blue')
        canvas.coords(id1, y[0], 0, y[2], w[3])
        canvas.coords(id2, w[0], 0, w[2], y[3])
        #canvas.itemconfig(id1, fill='red')
        #canvas.itemconfig(id2, fill='blue')
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
        canvas.itemconfig(bar_list[i].id, fill='purple')


def test_thing(id):
    canvas.itemconfig(id, fill='purple')


def test_thing2(id):
    canvas.itemconfig(id, fill='green')


def insertion_sort(array):
    for i in range(1, len(array)):
        canvas.after(0, update_key(array[i].id))
        canvas.update()
        key = array[i].height
        j = i - 1
        while j >= 0 and key < array[j].height:
            canvas.after(50, update_bar(array[j].id, array[j+1].id))
            canvas.update()
            array[j+1].height = array[j].height
            temp = array[j+1].id
            array[j+1].id = array[j].id
            array[j].id = temp
            j -= 1

        array[j + 1].height = key
    canvas.after(0, finished())
    canvas.update()


def marker(id):
    canvas.itemconfig(id, fill='tan1')


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i].height < R[j].height:
                #canvas.after(0, test_thing(L[i].id))
                #canvas.update()
                arr[k] = L[i]
                temp_array.append(L[i])
                i += 1

            else:
                #canvas.after(0, test_thing2(R[j].id))
                #canvas.update()
                arr[k] = R[j]
                temp_array.append(R[j])
                j += 1

            k += 1

        while i < len(L):
            #canvas.after(20, test_thing(L[i].id))
            #canvas.update()
            arr[k] = L[i]
            temp_array.append(L[i])
            i += 1
            k += 1

        while j < len(R):
            #canvas.after(20, test_thing2(R[j].id))
            #canvas.update()
            arr[k] = R[j]
            temp_array.append(R[j])
            j += 1
            k += 1

    for q in range(len(arr)):
        canvas.after(20, overtake(q, arr[q].height))
        canvas.update()


root = tk.Tk()
root.title("Animated Circle")
# ulc position of rootwindow
root.geometry("+{}+{}".format(150, 80))
# create a canvas to draw on
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack()

for i in range(1, len(bar_list)):
    bar(i, bar_list[i].height, bar_list[i].id)
    #print(bar_list[i].height, bar_list[i].id)
temp_array = []
merge_sort(bar_list)
#insertion_sort(bar_list)

#for i in range(1, len(bar_list)):
    #print(bar_list[i].height, bar_list[i].id)

root.mainloop()