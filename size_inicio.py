#!/usr/bin/python

'''
Por defecto, Windows crea las ventanas en la parte superior izquierda.
No tienen porque ser así en otros SO
'''

import wx

class FramePrinc(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(300,200))
        self.Move((800,250)) #mover a una posicion dada
        self.Centre()   #centrado
        self.Show()

app = wx.App()
frame = FramePrinc(None, "DiCOM iMAGEN")
app.MainLoop()


