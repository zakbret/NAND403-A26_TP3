import importlib
import ui
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