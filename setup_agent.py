from tkinter import *
from agenttype import *
from tkinter import ttk
from tkinter.filedialog import Open
from PIL import Image, ImageTk
from turtle import *


class SetupAgent():
  def __init__(self, master=None, screen=None):
    self.currenttype = None
    self.screen = screen
    self.master = master
    self.agents = ["New Agent"]
    self.initUI(master)
  def initUI(self, frame):
    frame.columnconfigure(0,weight=4)
    frame.columnconfigure(1,weight=1)
    frame.columnconfigure(2,weight=45)
    frame.rowconfigure(0,weight=1)
    scrollbar = Scrollbar(frame)
    scrollbar.grid(row=0,column=1, sticky="nws")
    self.list = Listbox(frame, width = 30, yscrollcommand=scrollbar.set, selectmode = "single")
    self.list.bind('<<ListboxSelect>>', self.AgentForm)
    self.list.grid(row=0,column=0, sticky="nwse")
    for x in self.agents:
      if x == "New Agent":
        self.list.insert("end", x)
      else :
        self.list.insert("end", x.name)
    self.createform()

  def AgentForm(self, event):
    select_index = self.list.curselection()
    if select_index:
      self.select_index = select_index[0]
      if self.select_index == 0:
        self.showcreateform()
      else :
        type = self.agents[self.select_index]
        self.showeditform(type)


  def createform(self):
    self.subframe = Frame(self.master, width=900, height=500)
    ###########################Title#######################################
    self.subframe.title = StringVar()
    Label(self.subframe, textvariable=self.subframe.title, font=("Arial", 20)).place(x=200,y=10)
    self.subframe.title.set("Create Agent")
    ##########################Name Input##################################
    Label(self.subframe, text="Name:").place(x=50, y=80)
    self.subframe.name_input = Entry(self.subframe, width=50)
    self.subframe.name_input.place(x=150, y=80)
    ##########################Amount Input##################################
    Label(self.subframe, text="Amount:").place(x=50, y=120)
    self.subframe.amount_input = Entry(self.subframe, width=50)
    self.subframe.amount_input.place(x=150, y=130)
    ##########################Shape Input##################################
    Label(self.subframe, text="Shape:").place(x=50, y=160)
    shapes = self.screen.getshapes()
    shapes.insert(0, "New Shape")
    self.subframe.shape_box = ttk.Combobox(self.subframe, values=shapes)
    self.subframe.shape_box.place(x=150, y=160)
    self.subframe.shape_box.bind("<<ComboboxSelected>>", self.selectShape)
    ##########################Apply button##################################
    self.subframe.button_title = StringVar()
    Button(self.subframe, textvariable=self.subframe.button_title,
      command=lambda: self.createNewType(self.subframe.name_input,
                                         self.subframe.amount_input,
                                         self.subframe.shape_box
                                         )).place(x=250,y=400)
    self.subframe.button_title.set("Create")


  def showcreateform(self):
    self.subframe.grid(row=0, column = 2)
    self.subframe.name_input.delete(0, "end")
    self.subframe.amount_input.delete(0, "end")
    self.subframe.shape_box.set('')
    self.subframe.title.set("Create Agent")
    self.subframe.button_title.set("Create")
    print("showcreate")

  def showeditform(self, typeobject):
    self.subframe.title.set(typeobject.name)
    self.subframe.name_input.delete(0, "end")
    self.subframe.name_input.insert(0, typeobject.name)
    self.subframe.amount_input.delete(0, "end")
    self.subframe.amount_input.insert(0, typeobject.amount)
    self.subframe.shape_box.set('')
    self.subframe.shape_box.current(typeobject.shape[0])
    self.subframe.button_title.set("Update")
    self.subframe.grid(row=0, column = 2)
    print("showedit")

  def createNewType(self, name, amount, shape=None):
    if self._is_int(amount.get()) == True:
      amount = int(amount.get())
    else :
      amount = 1
    if self.select_index == 0 :
      new = AgentType(name.get(), amount)
      if shape != None:
        new.setshape([shape.current(),shape.get()])
      self.agents.append(new)
      self.list.insert("end", new.name)
      print(self.agents)
    else:
      agenttype = self.agents[self.select_index]
      agenttype.name = name.get()
      agenttype.amount = amount
      agenttype.setshape([shape.current(),shape.get()])
      self.currenttype = agenttype
      print(agenttype)

  def _is_int(self, x):
    try:
        x = int(x)
        return True
    except:
        return False

  def selectShape(self, event):
    shape_name = self.subframe.shape_box.get()
    shape_index = self.subframe.shape_box.current()
    if shape_name != "New Shape":
      if self.currenttype:
        self.currenttype.setshape(shape_index, shape_name)
    else:
      Label(self.subframe, text="Shape Name:").place(x=80, y=200)
      shape_name_entry = Entry(self.subframe)
      shape_name_entry.place(x=180, y=200)
      Button(self.subframe, text="Shape Image", command=self.inputImage).place(x=150, y=250)
      self.subframe.shape_image = Label(self.subframe)
      Button(self.subframe, text="Add", command= lambda: self.createShape(shape_name_entry.get(), self.shape_image)).place(x=150, y=280)
  def inputImage(self):
    ftypes = [('Image files', '*.gif *.png *.jpeg'), ('All files', '*')]
    dlg = Open(self.master, filetypes = ftypes)
    fl = dlg.show()
    if fl != '':
      photo = ImageTk.PhotoImage(Image.open(fl))
      self.shape_image = photo
      print(photo)
      self.subframe.shape_image.configure(image=photo)
      self.subframe.shape_image.photo = photo
      self.subframe.shape_image.place(x=400, y=200)

  def createShape(self, name, img):
    if name != '':
      new = Shape("image", img)
      self.screen.register_shape(name, new)
      shapes = self.screen.getshapes()
      shapes.insert(0, "New Shape")
      self.subframe.shape_box.configure(values = shapes)
      print(self.screen.getshapes())
