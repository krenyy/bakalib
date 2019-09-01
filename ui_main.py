#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.3 on Fri May 31 20:14:20 2019
#

import wx

import icons


# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class frameMain(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: frameMain.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.statusbar = self.CreateStatusBar(1)
        self.buttonChangeuser = wx.Button(self, wx.ID_ANY, u"Změnit uživatele")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: frameMain.__set_properties
        self.SetTitle("Bakalaris")
        self.statusbar.SetStatusWidths([-1])

        # statusbar fields
        statusbar_fields = [u"© Martin Kröner"]
        for i in range(len(statusbar_fields)):
            self.statusbar.SetStatusText(statusbar_fields[i], i)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: frameMain.__do_layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_1 = wx.GridSizer(2, 2, 0, 0)
        self.buttonRozvrh = wx.StaticBitmap(self, wx.ID_ANY, icons.rozvrh.GetBitmap())
        sizer_1.Add(self.buttonRozvrh, 0, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 5)
        self.buttonZnamky = wx.StaticBitmap(self, wx.ID_ANY, icons.znamky.GetBitmap())
        sizer_1.Add(self.buttonZnamky, 0, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 5)
        self.buttonAbsence = wx.StaticBitmap(self, wx.ID_ANY, icons.absence.GetBitmap())
        sizer_1.Add(self.buttonAbsence, 0, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 5)
        sizer_1.Add((0, 0), 0, 0, 0)
        sizer.Add(sizer_1, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        sizer_2.Add(self.buttonChangeuser, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        sizer.Add(sizer_2, 1, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 10)
        self.SetSizer(sizer)
        sizer.Fit(self)
        self.Layout()
        # end wxGlade


# end of class frameMain

class dialogLogin(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: dialogLogin.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.textUser = wx.TextCtrl(self, wx.ID_ANY, "")
        self.textPass = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_PASSWORD)
        self.cityComboBox = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN | wx.CB_READONLY | wx.CB_SORT)
        self.schoolComboBox = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN | wx.CB_READONLY)
        self.textUrl = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY)
        self.buttonLogin = wx.Button(self, wx.ID_ANY, u"Přihlásit se")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: dialogLogin.__set_properties
        self.SetTitle("Login")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: dialogLogin.__do_layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        labelUser = wx.StaticText(self, wx.ID_ANY, u"Uživatelské jméno: ")
        sizer.Add(labelUser, 0, wx.ALIGN_CENTER | wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)
        sizer.Add(self.textUser, 0, wx.ALIGN_CENTER | wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RIGHT, 10)
        labelPass = wx.StaticText(self, wx.ID_ANY, "Heslo: ")
        sizer.Add(labelPass, 0, wx.ALIGN_CENTER | wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)
        sizer.Add(self.textPass, 0, wx.ALIGN_CENTER | wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RIGHT, 10)
        labelCity = wx.StaticText(self, wx.ID_ANY, u"Město: ", style=wx.ALIGN_LEFT)
        sizer.Add(labelCity, 0, wx.ALIGN_CENTER | wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)
        sizer.Add(self.cityComboBox, 0, wx.ALIGN_CENTER | wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RIGHT, 10)
        labelSchool = wx.StaticText(self, wx.ID_ANY, u"Škola: ", style=wx.ALIGN_LEFT)
        sizer.Add(labelSchool, 0, wx.ALIGN_CENTER | wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)
        sizer.Add(self.schoolComboBox, 0, wx.ALIGN_CENTER | wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RIGHT, 10)
        sizer.Add(self.textUrl, 0, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 10)
        sizer.Add(self.buttonLogin, 0, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 10)
        self.SetSizer(sizer)
        sizer.Fit(self)
        self.Layout()
        # end wxGlade

# end of class dialogLogin

class appMain(wx.App):
    def OnInit(self):
        self.frameMain = frameMain(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frameMain)
        self.frameMain.Show()
        return True


# end of class appMain

if __name__ == "__main__":
    app = appMain(0)
    app.MainLoop()