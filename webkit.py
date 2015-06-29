from gi.repository import Gtk, WebKit

class App:
	def __init__(self):
		self.window = Gtk.Window()
		
		self.window.set_default_size(640,480)
		
		self.webview = WebKit.WebView()
		
		self.webview.load_uri("http://www.google.com.pe")
		
		self.atras = Gtk.Button()
		self.atras.set_label("<--")
		self.adelante = Gtk.Button()
		self.adelante.set_label("-->")
		self.ir = Gtk.Button()
		self.ir.set_label("Ir")
		self.url = Gtk.Entry()
		self.url.set_text ("www.google.com.pe")
		
		self.barra = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL)
		self.visor = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL)
		
		self.wrapper = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)
		
		self.contenedor_atras = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)
		self.contenedor_adelante = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)
		self.contenedor_ir = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)
		self.contenedor_url = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)
		
		self.contenedor_atras.pack_start(self.atras, True, True, 0)
		self.contenedor_adelante.pack_start(self.adelante, True, True, 0)
		self.contenedor_ir.pack_start(self.ir, True, True, 0)
		self.contenedor_url.pack_start(self.url, True, True, 0)
		self.visor.pack_start(self.webview, True, True, 0)
		
		self.barra.pack_start(self.contenedor_atras, False, True, 0)
		self.barra.pack_start(self.contenedor_adelante, False, True, 0)
		self.barra.pack_start(self.contenedor_url, True, True, 0)
		self.barra.pack_start(self.contenedor_ir, False, True, 0)
		
		self.wrapper.pack_start(self.barra, False, False, 0)
		self.wrapper.pack_start(self.visor, True, True, 0)
		
		self.window.add(self.wrapper)		
		
		self.window.connect ('destroy', lambda x: Gtk.main_quit())
		self.ir.connect ('clicked', self.ir_clicked_cb)
		self.url.connect ('activate', self.url_key_cb)
		self.atras.connect ('clicked', self.atras_cb)
		self.adelante.connect ('clicked', self.adelante_cb)
		self.webview.connect ('onload-event', self.onload_cb)
		
		self.window.show_all()
		
	def ir_clicked_cb (self, ir):
		direccion = self.url.get_text()
		self.webview.load_uri ("http://" + direccion)
		
	def url_key_cb (self, url):
		if url.get_text() != "": 
			direccion = self.url.get_text()
			self.webview.load_uri("http://" + direccion)


	def atras_cb (self, atras):
		self.webview.go_back ()
		
	def adelante_cb (self, adelante):
		self.webview.go_forward ()
	
	def onload_cb (self, frame, data):
		uri = self.webview.get_uri ()
		self.url.set_text (uri.replace ("http://", ""))
		
		

if __name__ == '__main__':
	App()
	Gtk.main()

