from tkinter import ttk
import tkinter as tk
from tkinter.filedialog import askopenfilename
import tkinter.scrolledtext as scrolledtext
from tkinter.filedialog import asksaveasfilename
from supported_languages import supported_languages
import os


class View(ttk.Frame):
    def __init__(self, master):
        """ Initialize all widgets.
        """
        super().__init__(master)
        self.controller = None

        # widgets initialisation
        self.top_frame = None
        self.dest_lbl = None
        self.dest_entry = None
        self.src_lbl = None
        self.src_entry = None
        self.left_frame = None
        self.right_frame = None
        self.text_left = None
        self.text_right = None

        # var initialisation
        self.src_var = tk.StringVar(master, "English")
        self.dest_var = tk.StringVar(master, "Russian")

        self.master.minsize(1050, 600)
        self.create_widgets()

    def create_widgets(self):
        """ Create and place all widgets on the grid.
        """
        # top frame with label widgets
        self.top_frame = tk.Frame(self.master, height=22, bg='white')
        self.top_frame.grid(row=0, column=0, columnspan=2, sticky='nsew')
        self.src_lbl = tk.Label(self.top_frame, bg='white', text='translate from: ')
        self.src_lbl.place(x=0, y=0)
        self.src_entry = tk.Entry(self.top_frame, width=10, relief='flat', textvariable=self.src_var)
        self.src_entry.place(x=85, y=1)
        self.dest_lbl = tk.Label(self.top_frame, bg='white', text='to: ')
        self.dest_lbl.place(x=150, y=0)
        self.dest_entry = tk.Entry(self.top_frame, width=10, relief='flat', textvariable=self.dest_var)
        self.dest_entry.place(x=170, y=1)

        # create two frames
        # left frame and scrolled text widget
        self.left_frame = tk.Frame(self.master, bg='blue')
        self.left_frame.grid(row=1, column=0, sticky='nsew')
        self.text_left = scrolledtext.ScrolledText(self.left_frame, wrap=tk.WORD)
        self.text_left.pack(fill="both", expand=True, side=tk.LEFT)

        # right frame and scrolled text widget
        self.right_frame = tk.Frame(self.master, bg='red')
        self.right_frame.grid(row=1, column=1, sticky='nsew')
        self.text_right = scrolledtext.ScrolledText(self.right_frame, wrap=tk.WORD)
        self.text_right.pack(fill="both", expand=True, side=tk.LEFT)

        # configuration for cols rows expansion
        self.master.grid_rowconfigure(1, minsize=1, weight=1)  # expand row 1 widgets
        self.master.grid_columnconfigure(0, minsize=1, weight=1)  # expand column 0 widget
        self.master.grid_columnconfigure(1, minsize=1, weight=1)  # expand column 1 widget

    def set_controller(self, controller):
        """ Set controller from a controller class.
        """
        self.controller = controller

    @staticmethod
    def file_dialogue_menu():
        """ File dialogue to open a file. Returns a filepath val.
        """
        file = askopenfilename(filetypes=[('Subtitle Files', '*.srt')])
        if file:
            filepath = os.path.abspath(file)
        return filepath

    @staticmethod
    def save_as_dialogue_menu():
        """ File dialog to save file. Returns a filepath.
        """
        filepath = asksaveasfilename(filetypes=[('Subtitle Files', '*.srt')], defaultextension=".srt")
        if filepath:
            return filepath

    def set_widget(self, widget):
        """ Specify which widget to use.
        """
        if widget == 'text_left':
            return self.text_left
        elif widget == 'text_right':
            return self.text_right
        else:
            return "Widget is not specified correctly!"

    def is_widget_empty(self, widget):
        """ If widget empty returns True.
        """
        widget_to_use = self.set_widget(widget)
        if widget_to_use.get('1.0', tk.END) == "\n":
            print("Widget is empty")
            return True

    def show_subtitles_in_widget(self, subtitles_list, widget):
        """ Display subtitles text in a widget.
        """
        widget_to_use = self.set_widget(widget)
        if subtitles_list is not None:
            for count, line in enumerate(subtitles_list, 1):
                widget_to_use.insert(tk.INSERT, str(count) + '\n')
                widget_to_use.insert(tk.INSERT, line + '\n')

    def clear_text_widget(self, widget):
        """ Clear text widget.
        """
        widget_to_use = self.set_widget(widget)
        widget_to_use.delete(1.0, tk.END)

    def widget_text_to_list(self, widget):
        """ Update changes from a text widget to a subtitle text list.
        """
        widget_to_use = self.set_widget(widget)
        all_text_from_widget = widget_to_use.get('1.0', 'end-2c').split('\n')
        # every even line is text in widget
        return [line for count, line in enumerate(all_text_from_widget, 1) if count % 2 == 0]

    def get_entries(self):
        """ Get source and destination languages from widget entries.
        """
        src = self.src_var.get().lower()
        dest = self.dest_var.get().lower()
        if src not in supported_languages.values():
            print(src, " language not supported")
        if dest not in supported_languages.values():
            print(dest, " language not supported")
        if src in supported_languages.values() and dest in supported_languages.values():
            return src, dest
        else:
            return None, None
