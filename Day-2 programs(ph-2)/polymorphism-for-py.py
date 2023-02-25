class vizag():
    def placename(self):
        print("vizag placename is AU")
    def student(self):
        print("yes - vizag")
    def which_year(self):
        print("3rd year-AU")

class hyd():
    def placename(self):
        print("hyd placename is HYD-KLU")
    def student(self):
        print("yes - HYD")
    def which_year(self):
        print("3rd year-hyd")

obj_viz =vizag()
obj_hyd = hyd()
for details in (obj_viz,obj_hyd):
    details.placename()
    details.student()
    details.which_year()
