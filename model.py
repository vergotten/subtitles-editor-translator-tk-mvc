import pysubs2
from googletrans import Translator


class Model:

    @staticmethod
    def load_subs(file_path):
        """ Load a subtitle file.
        """
        return pysubs2.load(file_path, encoding="utf-8")

    @staticmethod
    def save_subs(subtitles, file_path):
        """ Save subtitles as a file.
        """
        subtitles.save(file_path)

    def translate_subs(self, subtitles_list, src=None, dest=None):
        """ Translate subtitles from a subtitle list.
        """
        translated_subtitles = []
        for line in subtitles_list:
            new_line = line.replace("\\N", " ")
            translator = Translator()
            translated = translator.translate(new_line, src=src, dest=dest)
            translated_subtitles.append(self._add_separator(str(translated.text)))
        return translated_subtitles

    @staticmethod
    def _add_separator(string):
        """ Function that checks length of text and adds new line separator.
        """
        indices = [i for i, x in enumerate(string) if x == " "]
        if len(string) > 50 and len(indices) > 1:
            middle_index = indices[int(len(indices) / 2)]
            string = string[:middle_index] + '\\N' + string[middle_index + 1:]
        return string
