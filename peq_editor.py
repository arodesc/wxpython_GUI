#!/usr/bin/env python

import wx
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title = title, size=(200,100))
        self.control = wx.TextCtrl(self, style = wx.TE_MULTILINE)
        self.show=True


app = wx.App(False)
frame = MyFrame(None, "Pequeño Editor")
app.MainLoop()
