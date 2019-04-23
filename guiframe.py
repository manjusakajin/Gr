import tkinter as tk
import turtle
import compile
from simulation_frame import *
from setup_env import *
from setup_agent import *

class Application(tk.Frame):
    def __init__(self, master=None):
      super().__init__(master)
      self.tk = master
      self.pack()
      self.create_widgets()

    def create_widgets(self):
    #############################simulation frame #################################
      self.sub_frame1 = tk.Frame(self.master, width=1000, height=550, borderwidth=5, relief="groove")

      self.simulation_module = SimulationModule(self.sub_frame1)
      self.sub_frame1.pack()
      self.current_frame = self.sub_frame1
      self.turtle_screen = self.simulation_module.turtle_screen
 ##################################setup code frame################################
      # self.sub_frame2 = tk.Frame(self.master, width=1000, height=550, borderwidth=5, relief="groove")
      # self.create_code_frame()
########################################setup enviroment##################################
      self.sub_frame3 = tk.Frame(self.master, width=1000, height=550, borderwidth=5, relief="groove")
      self.setup_env = SetupENV(self.sub_frame3, self.turtle_screen)
########################################setup agent#########################################
      self.sub_frame4 = tk.Frame(self.master, width=1000, height=550, borderwidth=5, relief="groove")
      self.setup_agent = SetupAgent(self.sub_frame4, self.turtle_screen)
########################################create button#########################################
      self.interface_button = tk.Button(self, text="Simulation", command=self.display_s_frame)
      self.interface_button.pack(side="left")

      self.code_button = tk.Button(self, text="Enviroment", command=self.display_e_frame)
      self.code_button.pack(side="left")

      self.code_button = tk.Button(self, text="Agent", command=self.display_a_frame)
      self.code_button.pack(side="left")


      # self.code_button = tk.Button(self, text="Code", command=self.display_c_frame)
      # self.code_button.pack(side="left")


    def create_code_frame(self):
      self.read_code = tk.Button(self.sub_frame2, text="read", command=self.get_code)
      self.read_code.pack(side="top")
      self.code = tk.Text(self.sub_frame2,width=685, height=500)
      self.code.pack(side="bottom")

    def display_s_frame(self):
      self.current_frame.pack_forget()
      self.sub_frame1.pack(fill="both", expand=True)
      self.current_frame = self.sub_frame1
    def display_a_frame(self):
      self.current_frame.pack_forget()
      self.sub_frame4.pack(fill="both", expand=True)
      self.current_frame = self.sub_frame4
    def display_e_frame(self):
      self.current_frame.pack_forget()
      self.sub_frame3.pack(fill="both", expand=True)
      self.current_frame = self.sub_frame3

    def get_code(self):
      code = self.code.get("1.0","end")
      compl = compile.Compile()
      compl.setSrc(code)

root = tk.Tk()
app = Application(master=root)
app.master.title("AgentSimulationTool")
app.master.geometry('1000x650')
app.mainloop()
