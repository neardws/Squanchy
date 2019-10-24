from base64 import b64decode
import wx
import wx.adv
from pubsub import pub

from memory_pic import *

def get_pic(pic_code, pic_name):
    image = open(pic_name, 'wb')
    image.write(b64decode(pic_code))
    image.close()

get_pic(favicon_ico, 'favicon.ico')

class MyTaskBarIcon(wx.adv.TaskBarIcon):
    ICON = "favicon.ico"  # 图标地址
    ID_ABOUT = wx.NewId()  # 菜单选项“关于”的ID
    ID_EXIT = wx.NewId()  # 菜单选项“退出”的ID
    ID_SHOW_WEB = wx.NewId()  # 菜单选项“显示页面”的ID
    TITLE = "Squanchy" #鼠标移动到图标上显示的文字

    def __init__(self):
        wx.adv.TaskBarIcon.__init__(self)
        self.SetIcon(wx.Icon(self.ICON), self.TITLE)  # 设置图标和标题
        self.Bind(wx.EVT_MENU, self.onAbout, id=self.ID_ABOUT)  # 绑定“关于”选项的点击事件
        self.Bind(wx.EVT_MENU, self.onExit, id=self.ID_EXIT)  # 绑定“退出”选项的点击事件
        self.Bind(wx.EVT_MENU, self.onShowWeb, id=self.ID_SHOW_WEB)  # 绑定“显示页面”选项的点击事件

    # “关于”选项的事件处理器
    def onAbout(self, event):
        wx.CallAfter(pub.sendMessage, "show", msg='readme')

    # “退出”选项的事件处理器
    def onExit(self, event):
        wx.Exit()

    # “显示页面”选项的事件处理器
    def onShowWeb(self, event):
        wx.CallAfter(pub.sendMessage, "show", msg='client')

    # 创建菜单选项
    def CreatePopupMenu(self):
        menu = wx.Menu()
        for mentAttr in self.getMenuAttrs():
            menu.Append(mentAttr[1], mentAttr[0])
        return menu

    # 获取菜单的属性元组
    def getMenuAttrs(self):
        return [('Active', self.ID_SHOW_WEB),
                ('About', self.ID_ABOUT),
                ('Exit', self.ID_EXIT)]


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self)
        MyTaskBarIcon()#显示系统托盘图标


class MyApp(wx.App):
    def OnInit(self):
        MyFrame()
        return True


if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()