# two classes - one child-like mom,dad ----child
#inherits properties of mom and dad
class mom:      #BASE CLASS -1
    def mdisplay(self):
        print("mom clas")
class dad:       # BASE CLASS -2
    def ddisplay(self):
        print("dad class")
class child(mom,dad):  # derived or inheritance
    def cdisplay(self):
        print("child class")
c1 = child()
c1.cdisplay()
c1.mdisplay()
c1.ddisplay()
