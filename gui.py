import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file("gui.glade")

handler = {
	"terminar_aplicacao": Gtk.main_quit
}

builder.connect_signals(handler)
window = builder.get_object("janela_principal")
window.show_all()

Gtk.main()
