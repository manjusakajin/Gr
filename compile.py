import variable as var

class Compile():
  def setSrc(self, srcCode=None):
    self.src = self.cutSrc(srcCode)
    print(self.src)

  def cutSrc(self, srcCode=None):
    if srcCode != None:
      splited = srcCode.split('\n')
      splited.pop()
      for x in range(len(splited)):
        cur = splited[x]
        splited[x] = self.getTokens(cur)
      return splited

  def getTokens(self, command=None):
    tokens = []
    while(command != None and command != ''):
      status = 0
      if command[0] == '#':
        break
      elif command[0] == ' ':
        status = 1
      elif command[0] == '+':
        tokens.append({'type': 'sb_plus'})
        status = 1
      elif command[0] == '-':
        tokens.append({'type': 'sb_minus'})
        status = 1
      elif command[0] == '*':
        tokens.append({'type': 'sb_time'})
        status = 1
      elif command[0] == '/':
        tokens.append({'type': 'sb_slash'})
        status = 1
      elif command[0] == '>':
        if command[1] == '=':
          tokens.append({'type': 'sb_gte'})
          status = 2
        else :
          tokens.append({'type': 'sb_gt'})
          status = 1
      elif command[0] == '<':
        if command[1] == '=':
          tokens.append({'type': 'sb_lte'})
          status = 2
        else:
          tokens.append({'type': 'sb_lt'})
          status = 1
      elif command[0] == '=':
        if command[1] == '=':
          tokens.append({'type': 'sb_eq'})
          status = 2
        else:
          tokens.append({'type': 'sb_assign'})
          status = 1
      elif command[0] == '!':
        if command[1] == '=':
          tokens.append({'type': 'sb_noteq'})
          status = 2
        else:
          self.err.append('syntax error : not use !')
          status = -1
          break
      elif command[0].isdigit():
        i = 0
        while(i<len(command) and command[i].isdigit()):
          i+=1
        status = i
        tokens.append({'type': 'number', 'value': float(command[0:i-1])})
      else:
        i = 0
        while(i<len(command) and command[i] != ' '):
          i+=1
        status = i
        token = command[0:i]
        if token in var.keyword:
          tokens.append({'type': var.keyword[token] })
        else:
          tokens.append({'type': 'indent', 'value': command[0:i]})
      non_cut = command
      command = non_cut[status:len(non_cut)]
      print(command)
    return tokens
