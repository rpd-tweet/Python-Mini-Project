import tkinter as tk   # tinker module containing tk toolkit 
                       # renamed as tk

root=tk.Tk()  # root widget

w=tk.Label(root,text="First Project!!") # label widget

w.pack()  # packs the windows size to fit to the text

root.mainloop() # event loop
               # to make windows appear
