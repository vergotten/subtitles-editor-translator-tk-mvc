class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.subtitles = None
        self.debug = True

    def open(self, event=None):
        """ Open subtitles file from menu bar.
        """
        try:
            filepath = self.view.file_dialogue_menu()
            if filepath:
                self.close()
                self.subtitles = self.model.load_subs(file_path=filepath)
                self.view.show_subtitles_in_widget([line.text for line in self.subtitles], widget='text_left')

                if self.debug is True:
                    print("Controller -> open", 200)
        except Exception as e:
            print("Error ", e)

    def translate(self, event=None):
        """ Translate subtitles and show in text widget.
        """
        self.view.clear_text_widget(widget='text_right')
        if not self.view.is_widget_empty(widget='text_left'):
            subtitles_list = self.view.widget_text_to_list(widget='text_left')
            try:
                if subtitles_list:
                    src, dest = self.view.get_entries()
                    if (src is not None) and (dest is not None):
                        print(src, dest)
                        translated_subtitles = self.model.translate_subs(subtitles_list, src=src, dest=dest)
                        self.view.show_subtitles_in_widget(translated_subtitles, widget='text_right')
                    else:
                        print("Not supported languages")

                    if self.debug is True:
                        print("Controller -> translate subtitles", 200)
            except Exception as e:
                print("Error ", e)

    def save_as(self, event=None):
        """ Save subtitles as file from right text widget.
        """
        try:
            if not self.view.is_widget_empty(widget='text_right'):
                line_list = self.view.widget_text_to_list(widget='text_right')
                for count, line in enumerate(self.subtitles):
                    line.text = line_list[count]
                filepath = self.view.save_as_dialogue_menu()
                if filepath is not None:
                    self.model.save_subs(self.subtitles, filepath)

                if self.debug is True:
                    print("Controller -> save as", 200)
        except Exception as e:
            print("Error ", e)

    def close(self, event=None):
        """ Close all subtitles. Clear both text widgets.
        """
        try:
            self.view.clear_text_widget(widget='text_left')
            self.view.clear_text_widget(widget='text_right')

            if self.debug is True:
                print("Controller -> close", 200)
        except Exception as e:
            print("Error ", e)
