# This file makes Python's built-in ZipFile class
# respect the with: statement.

from zipfile import ZipFile

def enter_zip(self):
    return self

def exit_zip(self, type, value, traceback):
    self.close()
    return False # Don't ignore exceptions

setattr(ZipFile, '__exit__', exit_zip)
setattr(ZipFile, '__enter__', enter_zip)
