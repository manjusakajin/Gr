from tkinter import *
from tkinter import ttk

class SetupAssociation():
  def __init__(self, frame):
    self.links = []
    self._subframe = frame
    self.initUI(frame)

  def initUI(self, frame):
    frame.columnconfigure(0,weight=14)
    frame.columnconfigure(1,weight=1)
    frame.columnconfigure(2,weight=7)
    frame.columnconfigure(3,weight=14)
    frame.columnconfigure(4,weight=7)
    frame.rowconfigure(0,weight=3)
    frame.rowconfigure(1,weight=1)
    frame.rowconfigure(2,weight=1)
    frame.rowconfigure(3,weight=1)
    frame.rowconfigure(4,weight=1)
    frame.rowconfigure(5,weight=1)
    frame.rowconfigure(6,weight=10)
    scrollbar = Scrollbar(frame)
    scrollbar.grid(row=0,column=1,rowspan=7, sticky="nws")
    Listbox(self._subframe, yscrollcommand=scrollbar.set, selectmode = "single").grid(row=0, column=0, rowspan=7, sticky="nwse")
    Label(self._subframe, text="Create Association", font=("Arial", 20)).grid(row=0,column=3)
    Label(self._subframe, text="Type 1:").grid(row=1,column=2)
    ttk.Combobox(self._subframe).grid(row=1, column=3,sticky="ew")
    Label(self._subframe, text="Type 2:").grid(row=2,column=2)
    ttk.Combobox(self._subframe).grid(row=2, column=3, sticky="ew")
    Label(self._subframe, text="Check :").grid(row=3,column=2)
    ttk.Combobox(self._subframe).grid(row=3, column=3, sticky="ew")
    Button(self._subframe, text="Create New").grid(row=3, column=4)
    Label(self._subframe, text="Type 1 Action :").grid(row=4,column=2)
    ttk.Combobox(self._subframe).grid(row=4, column=3, sticky="ew")
    Button(self._subframe, text="Create New").grid(row=4, column=4)
    Label(self._subframe, text="Type 2 Action :").grid(row=5,column=2)
    ttk.Combobox(self._subframe).grid(row=5, column=3,sticky="ew")
    Button(self._subframe, text="Create New").grid(row=5, column=4)
    Button(self._subframe, text="Create").grid(row=6, column=3)
