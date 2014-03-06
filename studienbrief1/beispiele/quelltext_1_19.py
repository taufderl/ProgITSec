class Contact(object):

    def __init__(self, first_name=None, last_name=None, 
                 display_name=None, email=None):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_display_name(display_name)
        self.set_email(email)

    def set_first_name(self, value):
        self._first_name = value

    def get_first_name(self):
        return self._first_name

    def set_last_name(self, value):
        self._last_name = value

    def get_last_name(self):
        return self._last_name

    def set_display_name(self, value):
        self._display_name = value

    def get_display_name(self):
        return self._display_name

    def set_email(self, value):
        self._email = value

    def get_email(self):
        return self._email

    def print_info(self):
        print(self.display_name, "<" + self.email + ">")