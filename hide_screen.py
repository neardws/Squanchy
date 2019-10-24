from base64 import b64decode

import wx
from memory_pic import *

def get_pic(pic_code, pic_name):
    image = open(pic_name, 'wb')
    image.write(b64decode(pic_code))
    image.close()

get_pic(fake_screen_png, 'fake_screen.png')

class MyPanel(wx.Panel):
    """"""

    def __init__(self, parent):
        """Constructor"""
        p = wx.Panel.__init__(self, parent)
        bitmap = wx.Bitmap("fake_screen.png", wx.BITMAP_TYPE_ANY)
        size = bitmap.GetWidth(), bitmap.GetHeight()
        wx.StaticBitmap(self, -1, bitmap, pos=(0, 0), size=size)
        self.Bind(wx.EVT_KEY_DOWN, self.onKey)
        self.Centre()
        self.Show()

    def onKey(self, event):
        """
        Check for ESC key press and exit is ESC is pressed
        """
        key_code = event.GetKeyCode()
        if key_code == wx.WXK_ESCAPE:
            self.GetParent().Close()
        else:
            event.Skip()


class MyFrame(wx.Frame):
    """"""

    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Squanchy")
        panel = MyPanel(self)
        self.ShowFullScreen(True)


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()