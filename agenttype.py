class AgentType():
  def __init__(self, typename, amount, behavior):
    self.name = typename
    self.amount = amount
    self.move_behavior = behavior
  def setshape(self, shape):
    if shape[1] != "New Shape":
      self.shape = shape
