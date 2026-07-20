
class wpv1:
    def status(self):
        print("You can upload images/videos")

class wpv2(wpv1):
     def status(self):
         super().status()
         print("You can react and reply")

class wpv3(wpv2):
     def status(self):
         super().status()
         print("You can reshare and like")

ashrutha = wpv3()
ashrutha.status()
'''
#multiplelevel inheristances won't work super().method()&use class().method()

class wpv1:
    def status(self):
        print("You can upload images/videos")

class wpv2:
     def status(self):
         print("You can react and reply")

class wpv3(wpv2,wpv1):
     def status(self):
         wpv1.status(self)
         wpv2.status(self)
         print("You can reshare and like")

ashrutha = wpv3()
ashrutha.status()
'''