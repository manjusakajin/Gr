import tkinter as tk
from turtle import *
import random

class Agent():
  def __init__(self, agenttype, move_behavior, screen, shape, width, height):
    self.turtle = RawPen(screen)
    self.turtle.shape(shape)
    self.type_name = agenttype
    self.move_behavior = move_behavior
    self.screen_width = width
    self.screen_height = height
    self.setupPosition()
  def setupPosition(self):
    if self.screen_width != None and self.screen_height != None:
      self.originXPosition = random.randint(0, self.screen_width)
      self.originYPosition = random.randint(0, self.screen_height)
    else:
      self.originXPosition = random.randint(0, 100)
      self.originYPosition = random.randint(0, 100)
    self.turtle.penup()
    self.turtle.setposition(self.originXPosition,self.originYPosition)
  def move(self):
    print("loan")
    exec('self.' + self.move_behavior + '()')
  def randomRun(self):
    x = self.turtle.xcor()
    y = self.turtle.ycor()
    moveX = -1
    moveY = -1
    while moveX<0 or moveX>self.screen_width or moveY<0 or moveY>self.screen_height:
      moveX = x + random.randint(-5,5)
      moveY = y + random.randint(-5,5)
    self.turtle.goto(moveX, moveY)
    print("ramdomRun")
