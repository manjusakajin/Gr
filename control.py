from env import *
from turtle import *
import random
from agent import *

class Controlmodule():
  def __init__(self, env_module, agent_module, screen):
    self._screen = screen
    self._env = env_module
    self._agentmodule = agent_module
    self.agents = []

  def setup(self):
    self._screen.clear()
    object = Enviroment(self._screen)
    if self._env.bgcolor:
      object.setupbgcolor(self._env.bgcolor)
    if self._env.bgpic:
      object.setupbgpic(self._env.bgpic)
    if self._env.width and self._env.height:
      object.setupgrid(self._env.width, self._env.height)
    else:
      object.setupgrid(100, 100)
    if self._agentmodule:
      for x in self._agentmodule.agents:
        if x != "New Agent":
          for y in range(x.amount):
            agent = Agent(x.name, x.move_behavior, self._screen,
            x.shape[1], self._env.width, self._env.height)
            self.agents.append(agent)
            # turtle = RawPen(self._screen)
            # turtle.shape(x.shape[1])
            # if self._env.width != None and self._env.height != None:
            #   self.originXPosion = random.randint(0, self._env.width)
            #   self.originYPosion = random.randint(0, self._env.height)
            # else:
            #   self.originXPosion = random.randint(0, 100)
            #   self.originYPosion = random.randint(0, 100)
            # turtle.penup()
            # turtle.setposition(self.originXPosion,self.originYPosion)
  def run(self):
    if self.agents:
      for x in self.agents:
        x.move()
    self._screen.ontimer(self.run())
