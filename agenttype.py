class AgentType():
  def __init__(self, name, amount=1):
    self.name = name
    self.amount = amount
  def setshape(self, shape):
    if shape[1] != "New Shape":
      self.shape = shape
