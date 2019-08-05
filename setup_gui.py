from cx_Freeze import setup, Executable
import sys

base = None

if sys.platform == 'win64':
    base = None


executables = [Executable("gui.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "Fasta_Extractor",
    options = options,
    version = "0.0.1",
    description = 'Primeiro executável',
    executables = executables
)