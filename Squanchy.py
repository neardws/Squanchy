from base64 import b64decode

import wx
import socket
from readme import README_GUI
from hide_screen import MyFrame
import threading
from ico import MyApp
from pubsub import pub

from memory_pic import *

def get_pic(pic_code, pic_name):
    image = open(pic_name, 'wb')
    image.write(b64decode(pic_code))
    image.close()

get_pic(favicon_ico, 'favicon.ico')

class GUI(wx.Frame):
    ICON = "favicon.ico"  # 图标地址
    def __init__(self, parent, title):
        super(GUI, self).__init__(parent, title=title, size=(400, 150))
        self.SetIcon(wx.Icon(self.ICON))  # 设置图标和标题
        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        p = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        l1 = wx.StaticText(p, label="Squanchy is a great tool, wubba lubba dub dub.", style=wx.ALIGN_CENTRE)
        vbox.Add(l1, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 20)

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        b1 = wx.Button(p, label="README")
        b1.Bind(wx.EVT_BUTTON, self.OnClick_readme, b1)
        hbox.AddStretchSpacer(1)
        hbox.Add(b1, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        b2 = wx.Button(p, label="Show Screen Image")
        b2.Bind(wx.EVT_BUTTON, self.OnClick_show, b2)
        hbox.AddStretchSpacer(1)
        hbox.Add(b2, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        # b3 = wx.Button(p, label="Upload Screen Image")
        # b3.Bind(wx.EVT_BUTTON, self.OnClick_upload, b3)
        # hbox.AddStretchSpacer(1)
        # hbox.Add(b3, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        vbox.Add(hbox, 0, wx.ALIGN_CENTER_HORIZONTAL)

        p.SetSizer(vbox)

        thread = threading.Thread(target=self.do_work)
        thread.setDaemon(True)
        thread.start()

        # 注册
        pub.subscribe(self.updateHandle, "show")

        # 绑定事件
        self.Bind(wx.EVT_CLOSE, self.OnHide)
        self.Bind(wx.EVT_ICONIZE, self.OnIconfiy)

    def updateHandle(self, msg):
        if(msg == 'hidden_screen'):
            app = wx.App(False)
            frame = MyFrame()
            app.MainLoop()
        elif(msg == 'client'):
            self.Show()
        elif(msg == 'readme'):
            app = wx.App()
            README_GUI(None, title='Squanchy')
            app.MainLoop()
        else:
            pass

    def OnClick_readme(self, event):
        app = wx.App()
        README_GUI(None, title='Squanchy')
        app.MainLoop()

    def OnClick_show(self, event):
        app = wx.App(False)
        frame = MyFrame()
        app.MainLoop()

    def OnClick_upload(self, event):
        pass

    def OnHide(self, event):
        self.Hide()
        app = MyApp()
        app.MainLoop()

    def OnIconfiy(self, event):
        self.Hide()
        event.Skip()


    def do_work(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
        client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        client.bind(("", 37020))
        while True:
            data, addr = client.recvfrom(1024)
            print("received message: %s" % data)
            str = data.decode('ASCII')
            if(str == 'it`s coming'):
                wx.CallAfter(pub.sendMessage, "show", msg='hidden_screen')



if __name__ == '__main__':
    app = wx.App()
    GUI(None, title = 'Squanchy')
    app.MainLoop()


