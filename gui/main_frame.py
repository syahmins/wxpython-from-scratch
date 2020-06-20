import sys

import gui.glade_generated as gg


class MainFrame(gg.MainFrame):
    def mnu_exit(self, event):
        sys.exit(0)

    def mnu_about(self, event):
        print('ABOUT')