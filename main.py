import sys
import os
#add the project folder to maya
dossier_projet = os.path.dirname(__file__)
if dossier_projet not in sys.path:
    sys.path.append(dossier_projet)


import importlib
import ui
#reload ui so I don't get an old version
importlib.reload(ui)
from ui import RandomAnimatorGenerator


def main():
    global widget
    try:
        widget.close()
    except Exception:
        pass
    widget = RandomAnimatorGenerator()
    widget.show()
 
main()