class Contact(object):

    def __init__(self, first_name=None, last_name=None, 
                 display_name=None, email=None):
        self.first_name = first_name
        self.last_name = last_name
        self.display_name = display_name
        self.email = email

    def print_info(self):
        print(self.display_name, "<" + self.email + ">")