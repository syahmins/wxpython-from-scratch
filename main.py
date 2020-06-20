import wx

from gui.app import App
from gui.main_frame import MainFrame

if __name__ == '__main__':
    app = App()
    frame = MainFrame(None, wx.ID_ANY, "Hello World!")
    app.SetTopWindow(frame)
    frame.Show()
    app.MainLoop()
