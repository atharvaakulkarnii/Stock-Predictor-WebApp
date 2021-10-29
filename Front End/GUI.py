
import tkinter as tk
root = tk.Tk()
def gethistory():
 from nsepy import get_history
 from datetime import datetime
 import dateutil.relativedelta
 import pandas as pd  
 v = str(w.get())
 to_date=datetime.now()
 to_date=datetime.strftime(to_date,'%Y %m %d')
 to_date=datetime.strptime(to_date,'%Y %m %d')
 from_date=to_date - dateutil.relativedelta.relativedelta(months=12)   #can write months=6 | manths=10 | year=1 | days=10
 data=get_history(symbol=v,start=from_date,end=to_date)
 df = pd.DataFrame(data)
 df.to_csv('file1.csv')
 # print(data)
 #
 #

label = tk.Label(root,text="Hello World!")
label.pack()
w = tk.Entry(root)
w.pack()
button = tk.Button(root,text="test button",command=gethistory)
button.pack()
root.config(bg='azure')
root.minsize(600,400)
root.title("Stock Predictor")
root.mainloop()