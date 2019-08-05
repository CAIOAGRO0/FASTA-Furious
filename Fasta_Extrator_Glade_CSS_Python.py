import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file("Fasta_Extrator_Glade_CSS_Python.glade")

handler = {
	"terminar_aplicacao": Gtk.main_quit
}

builder.connect_signals(handler)
window = builder.get_object("Janela_principal")
window.show_all()

Gtk.main()
