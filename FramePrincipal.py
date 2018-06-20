# -*- coding: utf-8 -*- 



import wx
import wx.xrc

class FramePrincipal ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Géolocalisation", pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizerPrincipal = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel1 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Adresse :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer4.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.m_textCtrl_adresse = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_textCtrl_adresse, 1, wx.ALL, 5 )
		
		self.m_button_rechercher = wx.Button( self.m_panel1, wx.ID_ANY, u"Rechercher", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_button_rechercher, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( bSizer4, 0, wx.EXPAND, 5 )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		m_listBox_localisationChoices = []
		self.m_listBox_localisation = wx.ListBox( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_localisationChoices, 0 )
		bSizer5.Add( self.m_listBox_localisation, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer2.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		
		self.m_panel1.SetSizer( bSizer2 )
		self.m_panel1.Layout()
		bSizer2.Fit( self.m_panel1 )
		self.m_notebook1.AddPage( self.m_panel1, u"Localisation", False )
		self.m_panel2 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText19 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Origine :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		bSizer18.Add( self.m_staticText19, 0, wx.ALL, 5 )
		
		self.m_textCtrl_origine = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.m_textCtrl_origine, 1, wx.ALL, 5 )
		
		self.m_staticText20 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Destionation :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		bSizer18.Add( self.m_staticText20, 0, wx.ALL, 5 )
		
		self.m_textCtrl_destination = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.m_textCtrl_destination, 1, wx.ALL, 5 )
		
		self.m_button_estimation = wx.Button( self.m_panel2, wx.ID_ANY, u"Estimation", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.m_button_estimation, 0, wx.ALL, 5 )
		
		
		bSizer3.Add( bSizer18, 0, wx.EXPAND, 5 )
		
		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer20 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel4 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel4, wx.ID_ANY, u"En voiture" ), wx.VERTICAL )
		
		m_listBox2Choices = []
		self.m_listBox2 = wx.ListBox( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox2Choices, 0 )
		sbSizer8.Add( self.m_listBox2, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel4.SetSizer( sbSizer8 )
		self.m_panel4.Layout()
		sbSizer8.Fit( self.m_panel4 )
		bSizer20.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel5 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer12 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel5, wx.ID_ANY, u"À vélo" ), wx.VERTICAL )
		
		m_listBox4Choices = []
		self.m_listBox4 = wx.ListBox( sbSizer12.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox4Choices, 0 )
		sbSizer12.Add( self.m_listBox4, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel5.SetSizer( sbSizer12 )
		self.m_panel5.Layout()
		sbSizer12.Fit( self.m_panel5 )
		bSizer20.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer19.Add( bSizer20, 1, wx.EXPAND, 5 )
		
		bSizer21 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel6 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer21.Add( self.m_panel6, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel7 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer13 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel7, wx.ID_ANY, u"En marche" ), wx.VERTICAL )
		
		m_listBox3Choices = []
		self.m_listBox3 = wx.ListBox( sbSizer13.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox3Choices, 0 )
		sbSizer13.Add( self.m_listBox3, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel7.SetSizer( sbSizer13 )
		self.m_panel7.Layout()
		sbSizer13.Fit( self.m_panel7 )
		bSizer21.Add( self.m_panel7, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel71 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer21.Add( self.m_panel71, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer19.Add( bSizer21, 1, wx.EXPAND, 5 )
		
		
		bSizer3.Add( bSizer19, 1, wx.EXPAND, 5 )
		
		
		self.m_panel2.SetSizer( bSizer3 )
		self.m_panel2.Layout()
		bSizer3.Fit( self.m_panel2 )
		self.m_notebook1.AddPage( self.m_panel2, u"Distance", True )
		
		bSizerPrincipal.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizerPrincipal )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		self.m_button_rechercher.Bind( wx.EVT_BUTTON, self.Rechercher )
		self.m_button_estimation.Bind( wx.EVT_BUTTON, self.Estimation )
	
	def __del__( self ):
		pass
	
	
	def Rechercher( self, event ):
		event.Skip()
	
	def Estimation( self, event ):
		event.Skip()
	

