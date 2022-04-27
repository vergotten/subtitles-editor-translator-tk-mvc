from model import *
from view import View
from controller import Controller
import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        """ Initialize model, view and controller.
        """
        super().__init__()

        self.title('Subtitle Translator')
        self.geometry("1050x600")

        # initialize model
        model = Model()

        # initialize view
        view = View(self.master)

        # initialize controller
        self.controller = Controller(model, view)
        view.set_controller(self.controller)

        # menu for top level window
        self.menubar = None
        self.file = None
        self.edit = None
        self.create_menu()

        # bind hotkeys
        self.bind_all('<Control-o>', self.controller.open)
        self.bind_all('<Control-s>', self.controller.save_as)
        self.bind_all('<Control-t>', self.controller.translate)
        self.bind_all('<Control-x>', self.controller.close)

    def create_menu(self):
        """ Menu widget on a toplevel window of application.
        """
        self.menubar = tk.Menu(self)

        self.file = tk.Menu(self.menubar, tearoff=0)
        self.file.add_command(label="Open", command=self.controller.open)
        self.file.add_command(label="Save as", command=self.controller.save_as)
        self.file.add_command(label="Close", command=self.controller.close)
        self.file.add_separator()
        self.file.add_command(label="Exit", command=self.quit)
        self.menubar.add_cascade(label="File", menu=self.file)

        self.edit = tk.Menu(self.menubar, tearoff=0)
        self.edit.add_command(label="Translate", command=self.controller.translate)
        self.menubar.add_cascade(label="Edit", menu=self.edit)

        self.config(menu=self.menubar)


if __name__ == '__main__':
    app = App()
    app.mainloop()
