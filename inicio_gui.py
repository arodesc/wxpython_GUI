#!/usr/bin/python
import wx

app = wx.App() #todos los programas tienen que tener un objeto app
frame = wx.Frame(None, -1, "DiCOM iMAGEN")  #crear un objeto frame
                                            #frame es un widget padre
frame.Show()
app.MainLoop()
