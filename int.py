# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import easygui as eg
import funciones_telnet
###########################################################################
## Class principal
###########################################################################

class principal ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PROYECTO DE CONMUTACION Y ENRUTAMIENTO", pos = wx.DefaultPosition, size = wx.Size( 500,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		gbSizer4 = wx.GridBagSizer( 0, 0 )
		gbSizer4.SetFlexibleDirection( wx.BOTH )
		gbSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"LOGIN" ), wx.VERTICAL )
		
		gbSizer8 = wx.GridBagSizer( 0, 0 )
		gbSizer8.SetFlexibleDirection( wx.BOTH )
		gbSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText35 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"USUARIO", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )
		gbSizer8.Add( self.m_staticText35, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.user = wx.TextCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, u"user", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer8.Add( self.user, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.password1234 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"PASSWORD", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.password1234.Wrap( -1 )
		gbSizer8.Add( self.password1234, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.password = wx.TextCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, u"xxxxxxx", wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		gbSizer8.Add( self.password, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		sbSizer11.Add( gbSizer8, 1, wx.EXPAND, 5 )
		
		
		gbSizer4.Add( sbSizer11, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		sbSizer12 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		self.m_staticText34 = wx.StaticText( sbSizer12.GetStaticBox(), wx.ID_ANY, u"SISTEMA DE AUTENTICACION", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )
		sbSizer12.Add( self.m_staticText34, 0, wx.ALL, 5 )
		
		self.m_bitmap3 = wx.StaticBitmap( sbSizer12.GetStaticBox(), wx.ID_ANY, wx.Bitmap( "fondo.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer12.Add( self.m_bitmap3, 0, wx.ALL, 5 )
		
		
		gbSizer4.Add( sbSizer12, wx.GBPosition( 1, 3 ), wx.GBSpan( 1, 1 ), 0, 5 )
		
		self.btn_validar = wx.Button( self, wx.ID_ANY, u"VALIDAR", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.btn_validar, wx.GBPosition( 6, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btn_salir1 = wx.Button( self, wx.ID_ANY, u"SALIR", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.btn_salir1, wx.GBPosition( 6, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( gbSizer4 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btn_validar.Bind( wx.EVT_BUTTON, self.validar_ingreso )
		self.btn_salir1.Bind( wx.EVT_BUTTON, self.salir1 )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def validar_ingreso( self, event ):
		x = 0
		f = open("base_de_datos.txt", 'r')
		a = f.readlines()
		for linea in a:
			lista = linea.split(',')
			usr = lista[0]
			contra = lista[1]
			contra2 = (contra[0:(len(contra) - 1)])
			if (self.user.GetLineText(0) == usr and self.password.GetLineText(0) == contra2):
				x = 1
		if (x == 1):
			f.close()
			frame2.Show()
		else:
			msg = "usario o contraseña incorrecto";
			titulo = "error"
			choices = ["yes", "no"]
			reply = eg.buttonbox(msg, title=titulo, choices=choices)

	
	def salir1( self, event ):
		frame.Destroy()


###########################################################################
## Class opciones
###########################################################################

class opciones ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"BIENVENIDOS", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"ELIJA UNA OPCION A REALIZAR", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText5.Wrap( -1 )
		bSizer2.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		
		bSizer2.AddSpacer(  5 )
		
		self.btn_con_basica = wx.Button( self, wx.ID_ANY, u"CONFIGURACION BASICA", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.btn_con_basica, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer2.AddSpacer(  5 )
		
		self.btn_bgp = wx.Button( self, wx.ID_ANY, u"CONFIGURAR BGP", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.btn_bgp, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer2.AddSpacer(  5 )
		
		self.btn_shows = wx.Button( self, wx.ID_ANY, u"REALIZAR SHOWS", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.btn_shows, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer2.AddSpacer( 5 )
		
		self.btn_salir = wx.Button( self, wx.ID_ANY, u"SALIR", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.btn_salir, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btn_con_basica.Bind( wx.EVT_BUTTON, self.configuracion_basica )
		self.btn_bgp.Bind( wx.EVT_BUTTON, self.configurar_bgp )
		self.btn_shows.Bind( wx.EVT_BUTTON, self.take_shows )
		self.btn_salir.Bind( wx.EVT_BUTTON, self.salir2 )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def configuracion_basica( self, event ):
		temp=frame.IsBeingDeleted()
		print(temp)
		if(temp!=True):
			frame3.Show()
		else:
			frame3.Show()


	
	def configurar_bgp( self, event ):
		frame4.Show()
	
	def take_shows( self, event ):
		frame5.Show()
	
	def salir2( self, event ):
		frame5.Destroy()
		frame4.Destroy()
		frame3.Destroy()
		frame2.Destroy()
		frame.Destroy()
	

###########################################################################
## Class op1
###########################################################################

class op1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"CONFIGURACION BASICA", pos = wx.DefaultPosition, size = wx.Size( 562,356 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		gbSizer3 = wx.GridBagSizer( 0, 0 )
		gbSizer3.SetFlexibleDirection( wx.BOTH )
		gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"--*-- UD VA A REALIZAR LA CONFIGURACION BASICA DEL ROUTER --*--", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		gbSizer3.Add( self.m_staticText26, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"CONFIGURAR" ), wx.VERTICAL )
		
		self.m_staticText27 = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"INGRESE EL HOSTNAME", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )
		sbSizer6.Add( self.m_staticText27, 0, wx.ALL, 5 )
		
		self.hostname = wx.TextCtrl( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer6.Add( self.hostname, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btn_configuracion_basica = wx.Button( sbSizer6.GetStaticBox(), wx.ID_ANY, u"CONFIGURACION BASICA", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer6.Add( self.btn_configuracion_basica, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		gbSizer3.Add( sbSizer6, wx.GBPosition( 3, 3 ), wx.GBSpan( 1, 1 ), wx.EXPAND|wx.SHAPED|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		self.btn_salir1 = wx.Button( sbSizer8.GetStaticBox(), wx.ID_ANY, u"SALIR", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer8.Add( self.btn_salir1, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		sbSizer8.AddSpacer( 5 )
		
		self.btn_regresar = wx.Button( sbSizer8.GetStaticBox(), wx.ID_ANY, u"REGRESAR", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer8.Add( self.btn_regresar, 0, wx.ALL|wx.BOTTOM|wx.EXPAND, 5 )
		
		
		sbSizer8.AddSpacer( 5 )
		
		
		gbSizer3.Add( sbSizer8, wx.GBPosition( 5, 3 ), wx.GBSpan( 1, 1 ), wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		self.SetSizer( gbSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btn_configuracion_basica.Bind( wx.EVT_BUTTON, self.realizar_conf_bas )
		self.btn_salir1.Bind( wx.EVT_BUTTON, self.salir3 )
		self.btn_regresar.Bind( wx.EVT_BUTTON, self.returned1 )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def realizar_conf_bas( self, event ):
		host=str(self.hostname.GetLineText(0))
		if(host!=""):
			funciones_telnet.configuracionBasica(tn,host)
		else:
			print("error")
	
	def salir3( self, event ):
		frame2.PageDown()
	
	def returned1( self, event ):
		self.Close(True)

	

###########################################################################
## Class op2
###########################################################################

class op2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"CONFIGURACION BGP", pos = wx.DefaultPosition, size = wx.Size( 779,598 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"--*-- UD VA A CONFIGURAR EL PROTOCOLO DE ENRUTAMIENTO BGP --*-- ", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText12.Wrap( -1 )
		gbSizer2.Add( self.m_staticText12, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 10 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"NUMERO DE AS" ), wx.VERTICAL )
		
		self.m_staticText14 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"INGRESE EL NUMERO DE AS LOCAL", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		sbSizer2.Add( self.m_staticText14, 0, wx.ALL, 5 )
		
		self.numero_as_local = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer2.Add( self.numero_as_local, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText15 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"INGRESE EL NUMERO DE AS REMOTO", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		sbSizer2.Add( self.m_staticText15, 0, wx.ALL, 5 )
		
		self.numero_as_remoto = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer2.Add( self.numero_as_remoto, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btn_guardar_as = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"GUARDAR AS", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer2.Add( self.btn_guardar_as, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.mostrar = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		sbSizer2.Add( self.mostrar, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		gbSizer2.Add( sbSizer2, wx.GBPosition( 4, 2 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.EXPAND|wx.SHAPED, 5 )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"CONFIGURAR VECINDAD" ), wx.VERTICAL )
		
		self.m_staticText17 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"INGRESE LA DIRECCION IP DEL VECINO", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		sbSizer3.Add( self.m_staticText17, 0, wx.ALL, 5 )
		
		self.ip_vecino = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.ip_vecino, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btn_configurar_vecino = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"CONFIGURAR VECINO", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.btn_configurar_vecino, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		gbSizer2.Add( sbSizer3, wx.GBPosition( 4, 4 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.EXPAND|wx.SHAPED, 5 )
		
		self.btn_regresar2 = wx.Button( self, wx.ID_ANY, u"REGRESAR", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.btn_regresar2, wx.GBPosition( 10, 4 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btn_salir3 = wx.Button( self, wx.ID_ANY, u"SALIR", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.btn_salir3, wx.GBPosition( 10, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"CONFIGURAR REDES" ), wx.VERTICAL )
		
		self.m_staticText19 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"INGRESE LAS REDES A PUBLICAR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		sbSizer4.Add( self.m_staticText19, 0, wx.ALL, 5 )
		
		self.network = wx.TextCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		sbSizer4.Add( self.network, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btn_configurar_redes = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, u"CONFIGURAR REDES", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.btn_configurar_redes, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		gbSizer2.Add( sbSizer4, wx.GBPosition( 8, 3 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		
		self.SetSizer( gbSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btn_guardar_as.Bind( wx.EVT_BUTTON, self.guardarAS )
		self.btn_configurar_vecino.Bind( wx.EVT_BUTTON, self.vecinosGP )
		self.btn_regresar2.Bind( wx.EVT_BUTTON, self.returned2 )
		self.btn_salir3.Bind( wx.EVT_BUTTON, self.salir4 )
		self.btn_configurar_redes.Bind( wx.EVT_BUTTON, self.conf_redes )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def guardarAS( self, event ):
		local=str(self.numero_as_local.GetLineText(0))
		localas=local
		remoto=str(self.numero_as_remoto.GetLineText(0))
		remotoas=remoto
		if (local!="") and (remoto!=""):
				self.mostrar.SetValue("Local: "+local+" Remoto: "+remoto)
				funciones_telnet.SesionBGP(tn,localas)
				print ("Se guardo el as")
		else:
			print("error")
	
	def vecinosGP( self, event ):
		vecino=str(self.ip_vecino.GetLineText(0))
		if(vecino!=""):
			funciones_telnet.configurarVecino(vecino,localas,remotoas,tn)
			print("se guardo correntamente")
		else:
			print("error")
	def returned2( self, event ):
		event.Skip()
	
	def salir4( self, event ):
		event.Skip()
	
	def conf_redes( self, event ):
		red=str(self.network.GetLineText(0))
		if(red!=""):
			funciones_telnet.configurarNetwork(tn,red,localas)
			print ("se guardo la conexion de red ")
#			tn.read_all()
			print ("funciona")
		else:
			print("error")

		#s=tn.read_all()
		#print(s)

###########################################################################
## Class op3
###########################################################################

class op3 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"SHOWS", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		gbSizer9 = wx.GridBagSizer( 0, 0 )
		gbSizer9.SetFlexibleDirection( wx.BOTH )
		gbSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText38 = wx.StaticText( self, wx.ID_ANY, u"DE CLICK EN UN BOTON Y ESPERO LOS RESULTADOS", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )
		gbSizer9.Add( self.m_staticText38, wx.GBPosition( 1, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.sh_ip_route = wx.Button( self, wx.ID_ANY, u"IP ROUTE", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer9.Add( self.sh_ip_route, wx.GBPosition( 3, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.sh_ip_neig = wx.Button( self, wx.ID_ANY, u"IP BGP NEIGHBORS", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer9.Add( self.sh_ip_neig, wx.GBPosition( 5, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.sh_ip_bgp = wx.Button( self, wx.ID_ANY, u"IP BGP", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer9.Add( self.sh_ip_bgp, wx.GBPosition( 3, 5 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.sh_run_config = wx.Button( self, wx.ID_ANY, u"RUNNING CONFIG", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer9.Add( self.sh_run_config, wx.GBPosition( 5, 5 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( gbSizer9 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.sh_ip_route.Bind( wx.EVT_BUTTON, self.sh_i_r )
		self.sh_ip_neig.Bind( wx.EVT_BUTTON, self.neighbors )
		self.sh_ip_bgp.Bind( wx.EVT_BUTTON, self.bgp )
		self.sh_run_config.Bind( wx.EVT_BUTTON, self.run_config )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def sh_i_r( self, event ):
		event.Skip()
	
	def neighbors( self, event ):
		event.Skip()
	
	def bgp( self, event ):
		event.Skip()
	
	def run_config( self, event ):
		event.Skip()
	
tn=funciones_telnet.conexion_telnet("192.168.137.2","admin","admin")
#tn.write("enable\n")
#tn.write("admin\n")
#a=tn.read_all()
#print(a)
localas=""
remotoas=""
app = wx.App(False)
frame = principal(None)
frame2 = opciones(None)
frame3 = op1(None)
frame4=op2(None)
frame5=op3(None)
frame.Show(True)
app.MainLoop()

