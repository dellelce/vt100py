#!/usr/bin/env python
#
# File:         vt100.py
# Created:      1346 100713
# Description:  class to handle vt100 terminal configuration & output in a pythonic way
#
#

class vt100:

  esc = chr(27);

  @classmethod
  def bold(self):
    return self.esc + '[1m'

  @classmethod
  def reset(self):
    return self.esc + '[0m'

  @classmethod
  def title(self, name = None):

    return self.esc + '];' + name + chr(7)


  @classmethod
  def cursor_pos(self, x = 0, y = 0):

     try:
       x_s = str(x)
     except: 
       x_s = '0'

     try:
       y_s = str(y)
     except: 
       y_s = '0'

     return self.esc + '[' + x_s + ';' + y_s + 'H'

## EOF ##

