	
import wx
from EvtFramePrincipal import EvtFramePrincipal


class MyApp(wx.App):
    def OnInit(self):
        self.m_frame = EvtFramePrincipal(None)
        self.m_frame.Show(True)
        self.SetTopWindow(self.m_frame)

        return True

app = MyApp(0)
app.MainLoop()
