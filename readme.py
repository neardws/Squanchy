from base64 import b64decode

import wx
from memory_pic import *

def get_pic(pic_code, pic_name):
    image = open(pic_name, 'wb')
    image.write(b64decode(pic_code))
    image.close()

get_pic(readme_png, 'readme.png')

class README_GUI(wx.Frame):

    def __init__(self, parent, title):
        super(README_GUI, self).__init__(parent, title=title, size=(375, 450))
        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        p = wx.Panel(self)
        bitmap = wx.Bitmap("readme.png", wx.BITMAP_TYPE_ANY)
        size = bitmap.GetWidth(), bitmap.GetHeight()
        wx.StaticBitmap(self, -1, bitmap, pos=(0,0), size=size)



if __name__ == '__main__':
    app = wx.App()
    README_GUI(None, title = 'Squanchy')
    app.MainLoop()