#!/usr/bin/env python
# coding: utf-8

# In[35]:


import random
from tkinter import *
from tkinter import ttk

flag = False
capacity = 10
order_quantity = 0
cycle = 1
day = 1
beginning_inventory = 10
demand = 0
ending_inventory = 0
shortage = 0
order = 0
order_arrival_time = 0

def next_day():
    global day, cycle, beginning_inventory, demand, ending_inventory, shortage, order, order_arrival_time, flag, order_quantity
    day += 1
    if order_arrival_time < 0:
        order_arrival_time = 0
        flag = False
        shortage =shortage - order_quantity
        if shortage < 0:
            beginning_inventory = -shortage
            shortage = 0
            
    if day % 5 == 0:
        cycle += 1
        
    demand = random.randint(1,5)
    ending_inventory = beginning_inventory - demand
    
    if ending_inventory < 0:
        shortage += -ending_inventory
        ending_inventory = 0
        
    if ending_inventory > 0:
        shortage = 0
        
    if day % 5 == 0:
        order = shortage + (capacity - ending_inventory)
        flag = True
        order_arrival_time = random.randint(1,2)
        order_quantity = order
        
    # Update the table with the new row
    table.insert('', 'end', values=(cycle, day, beginning_inventory, demand, ending_inventory, shortage, order, order_arrival_time))
    
    order=0
    if flag==True :
        order_arrival_time=order_arrival_time-1
        
    beginning_inventory = ending_inventory

root = Tk()
root.title("Inventory System")

font = ('Arial', 25, 'bold')

columns = ("Cycle", "Day", "Beginning Inventory", "Demand", "End Inventory", "Shortage", "Order", "Order Arrival Time")
table = ttk.Treeview(root, columns=columns, show='headings')
for col in columns:
    table.heading(col, text=col)
    table.column(col, anchor=CENTER)
table.grid(row=0, column=0, sticky='nsew')

button_next = Button(root, text="Click", command=next_day)
button_next.grid(row=1, column=0)

# Insert the initial row
table.insert('', 'end', values=(cycle, day, beginning_inventory, demand, ending_inventory, shortage, order, order_arrival_time))

root.mainloop()



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




