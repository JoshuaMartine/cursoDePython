"""
Herencia multiple
"""
class A:
    def print_A():
        print ("Print clase A")

class B:
   def print_B():
         print ("Print clase B")


class C:
    def C (A,B):
      print("clase C")   


obj = C

obj.print_A()
obj.print_B()
obj.print_C()

