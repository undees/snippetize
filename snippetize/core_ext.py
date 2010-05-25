from zipfile import ZipFile

def enter_zip(self):
    return self

def exit_zip(self, type, value, traceback):
    self.close()
    return False

setattr(ZipFile, '__exit__', exit_zip)
setattr(ZipFile, '__enter__', enter_zip)
