import tkinter as tk

class StopWatch:
  def __init__(self, root):
    self.count= 0
    self.break_loop=0
    self.i=0
    self.label3=tk.Label(root,text="\n\tStop watch",font="Times 20",anchor=tk.CENTER)
    self.label3.grid(column=0,row=0)
    self.label = tk.Label(root, text="\tTimer", font="Times 20",width=15,height=3,justify=tk.CENTER,anchor=tk.CENTER)
    self.label.grid(column=0,row=1)
    self.display=tk.StringVar()
    self.scrollbar=tk.Scrollbar(root)
    self.scrollbar.grid(column=3,row=5)
    self.mylist=tk.Listbox(root,width=10,height=3,yscrollcommand=self.scrollbar.set)
    
  def callback(self):
    self.break_loop=0
    self.count=0
    self.i=0
    self.mylist.delete(0,tk.END)
    self.label.after(1000, self.counter)
     
  
  def  markTime(self):
    getDisplay=self.display.get()
    self.i+=1
    self.mylist.insert(tk.END,"MARK : " +getDisplay+str(self.count))
    self.mylist.grid(column=2,row=5)
    self.scrollbar.config(command= self.mylist.yview )
    
    
  def breakLoop(self):
    self.break_loop=1
  
  def startFunction(self,root):
    
    button=tk.Button(root,text="Start",command=self.callback,width=6,height=3)
    button1=tk.Button(root,text="Mark",command=self.markTime,width=6,height=3)
    button2=tk.Button(root,text="Stop",command=self.breakLoop,width=6,height=3)
    button.grid(column=0,row=4)
    button1.grid(column=0,row=5)
    button2.grid(column=0,row=6)
  
  
  def counter(self):
    if self.break_loop==0:
      self.count += 1
      self.label.configure(text="\t"+str(self.count),justify=tk.RIGHT,anchor=tk.CENTER)
      self.label.after(1000, self.counter)
    else:
      self.label.config(text="\tEnd")
    

if __name__=="__main__":
    root=tk.Tk()
    root.title("StopWatch")
    root.geometry("350x400")
    root.resizable(0,0)
    stopwatch=StopWatch(root)
    stopwatch.startFunction(root)
    root.mainloop()
    