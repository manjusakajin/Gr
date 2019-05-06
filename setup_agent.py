from tkinter import *
from agenttype import *
from tkinter import ttk
from tkinter.filedialog import Open
from PIL import Image, ImageTk
from turtle import *
import variable as var

class SetupAgent():
  def __init__(self, master=None, screen=None):
    self._currenttype = None
    self._screen = screen
    self._master = master
    self.behavior = "randomRun"
    self.agents = ["New Agent"]
    self.initUI(master)
  def initUI(self, frame):
    frame.columnconfigure(0,weight=4)
    frame.columnconfigure(1,weight=1)
    frame.columnconfigure(2,weight=45)
    frame.rowconfigure(0,weight=1)
    scrollbar = Scrollbar(frame)
    scrollbar.grid(row=0,column=1, sticky="nws")
    self._list = Listbox(frame, width = 30, yscrollcommand=scrollbar.set, selectmode = "single")
    self._list.bind('<<ListboxSelect>>', self.AgentForm)
    self._list.grid(row=0,column=0, sticky="nwse")
    for x in self.agents:
      if x == "New Agent":
        self._list.insert("end", x)
      else :
        self._list.insert("end", x.name)
    self.createform()

  def AgentForm(self, event):
    select_index = self._list.curselection()
    if select_index:
      self._select_index = select_index[0]
      if self._select_index == 0:
        self.showcreateform()
      else :
        type = self.agents[self._select_index]
        self.showeditform(type)


  def createform(self):
    self._subframe = Frame(self._master, width=900, height=500)
    ###########################Title#######################################
    self._subframe.title = StringVar()
    Label(self._subframe, textvariable=self._subframe.title, font=("Arial", 20)).place(x=200,y=10)
    self._subframe.title.set("Create Agent")
    ##########################Name Input##################################
    Label(self._subframe, text="Name:").place(x=50, y=80)
    self._subframe.name_input = Entry(self._subframe, width=50)
    self._subframe.name_input.place(x=150, y=80)
    ##########################Amount Input##################################
    Label(self._subframe, text="Amount:").place(x=50, y=120)
    self._subframe.amount_input = Entry(self._subframe, width=50)
    self._subframe.amount_input.place(x=150, y=130)
    ##########################Shape Input##################################
    Label(self._subframe, text="Shape:").place(x=50, y=160)
    shapes = self._screen.getshapes()
    shapes.insert(0, "New Shape")
    self._subframe.shape_box = ttk.Combobox(self._subframe, values=shapes)
    self._subframe.shape_box.place(x=150, y=160)
    self._subframe.shape_box.bind("<<ComboboxSelected>>", self.selectShape)
    #############################Behavior Input############################
    self.behavior_label = Label(self._subframe, text="Behavior:")
    self.behavior_label.place(x=50, y=200)
    self.behavior_box = ttk.Combobox(self._subframe, values=var.methods)
    self.behavior_box.place(x=150, y=200)
    self.behavior_box.bind("<<ComboboxSelected>>", self.selectbehavior)
    self.behavior_button = Button(self._subframe, text="Create New Method")
    self.behavior_button.place(x=350,y=200)
    ##########################Apply button##################################
    self._subframe.button_title = StringVar()
    Button(self._subframe, textvariable=self._subframe.button_title,
      command=lambda: self.createNewType(self._subframe.name_input,
                                         self._subframe.amount_input,
                                         self._subframe.shape_box
                                         )).place(x=250,y=400)
    self._subframe.button_title.set("Create")


  def showcreateform(self):
    self._subframe.grid(row=0, column = 2)
    self._subframe.name_input.delete(0, "end")
    self._subframe.amount_input.delete(0, "end")
    self._subframe.shape_box.set('')
    self._subframe.title.set("Create Agent")
    self._subframe.button_title.set("Create")
    print("showcreate")

  def showeditform(self, typeobject):
    self._subframe.title.set(typeobject.name)
    self._subframe.name_input.delete(0, "end")
    self._subframe.name_input.insert(0, typeobject.name)
    self._subframe.amount_input.delete(0, "end")
    self._subframe.amount_input.insert(0, typeobject.amount)
    self._subframe.shape_box.set('')
    self._subframe.shape_box.current(typeobject.shape[0])
    self._subframe.button_title.set("Update")
    self._subframe.grid(row=0, column = 2)
    print("showedit")

  def createNewType(self, name, amount, shape=None):
    if self._is_int(amount.get()) == True:
      amount = int(amount.get())
    else :
      amount = 1
    if self._select_index == 0 :
      new = AgentType(name.get(), amount, self.behavior)
      if shape != None:
        new.setshape([shape.current(),shape.get()])
      self.agents.append(new)
      self._list.insert("end", new.name)
      print(self.agents)
    else:
      agenttype = self.agents[self._select_index]
      agenttype.name = name.get()
      agenttype.amount = amount
      agenttype.setshape([shape.current(),shape.get()])
      self._currenttype = agenttype
      print(agenttype)

  def _is_int(self, x):
    try:
        x = int(x)
        return True
    except:
        return False

  def selectShape(self, event):
    shape_name = self._subframe.shape_box.get()
    shape_index = self._subframe.shape_box.current()
    if shape_name != "New Shape":
      if self._currenttype:
        self._currenttype.setshape(shape_index, shape_name)
    else:
      self.behavior_label.place(x=50, y=330)
      self.behavior_box.place(x=150, y=330)
      self.behavior_button.place(x=350, y=330)
      Label(self._subframe, text="Shape Name:").place(x=80, y=200)
      shape_name_entry = Entry(self._subframe)
      shape_name_entry.place(x=180, y=200)
      Button(self._subframe, text="Shape Image", command=self.inputImage).place(x=150, y=250)
      self._subframe.shape_image = Label(self._subframe)
      Button(self._subframe, text="Add", command= lambda: self.createShape(shape_name_entry.get(), self._shape_image)).place(x=150, y=280)
  def inputImage(self):
    ftypes = [('Image files', '*.gif *.png *.jpeg'), ('All files', '*')]
    dlg = Open(self._master, filetypes = ftypes)
    fl = dlg.show()
    if fl != '':
      photo = ImageTk.PhotoImage(Image.open(fl))
      self._shape_image = photo
      print(photo)
      self._subframe.shape_image.configure(image=photo)
      self._subframe.shape_image.photo = photo
      self._subframe.shape_image.place(x=400, y=200)

  def createShape(self, name, img):
    if name != '':
      new = Shape("image", img)
      self._screen.register_shape(name, new)
      shapes = self._screen.getshapes()
      shapes.insert(0, "New Shape")
      self._subframe.shape_box.configure(values = shapes)
      print(self._screen.getshapes())
  def selectbehavior(self, event):
    self.behavior = self.behavior_box.get()
