import math
import random

class Main:
  """handles inputes and evaluates the problem."""
  def __init__(self):
    self.num1 = exec(input("enter a number: "))
    self.num2 = exec(input("enter another number: "))
    self.op = exec(input("enter an operator"))
    if self.op == '+':
      self.answer = self.num1 + self.num2
    elif self.op == '-':
      self.answer = self.num1 - self.num2
    elif self.op == '*' || 'x' || 'X':
      self.answer = self.num1 * self.num2
    elif self.op == '/' || '÷':
      self.answer = self.num1 / self.num2
    elif self.op == '%':
      self.answer = self.num1 % self.num2
    else:
      print("big stonks")
      print str(self.answer)
