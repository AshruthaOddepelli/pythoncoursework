#inherithances 
#5types
#1single inheritance
'''
class whatsappv1:
    def message(self):
        print("You Can Send message to people")
class whatsappv2(whatsappv1):
    def calls(self):
        print("You Can do Video/audio calls")

dinesh = whatsappv1()
print("v1-Dinesh")
dinesh.message()

naresh = whatsappv2()
print("v2-Naresh")
naresh.message()
naresh.calls()
'''
#2.Multiple inheritances->one parents class and mutiple child classes
'''
class whatsappv1:
    def message(self):
        print("You Can Send message to people")
class whatsappv2:
    def calls(self):
        print("You Can do Video/audio calls")
class whatsappv3:
    def media(self):
        print("You Can do photos/videos ")
class whatsappv4(whatsappv1,whatsappv2,whatsappv3):
    def status(self):
        print("You Can share status -[24 hours]")
        

dinesh = whatsappv4()
print("v4-Dinesh")
dinesh.message()
dinesh.calls()
dinesh.media()
dinesh.status()
'''
#3.mutilevel->level by level
'''
class whatsappv1:
    def message(self):
        print("You Can Send message to people")
class whatsappv2(whatsappv1):
    def calls(self):
        print("You Can do Video/audio calls")
class whatsappv3(whatsappv2):
    def media(self):
        print("You Can do photos/videos ")
class whatsappv4(whatsappv3):
    def status(self):
        print("You Can share status -[24 hours]")
        

dinesh = whatsappv4()
print("v4-Dinesh")
dinesh.message()
dinesh.calls()
dinesh.media()
dinesh.status()
'''
#4.hieraricha->single parent many parents in  child
'''
class whatsappv1:
    def message(self):
        print("you can send message to people")
class whatsappv2(whatsappv1):
    def stickers(self):
         print("you can send message with stickers to people") 

class whatsappv3(whatsappv1):
    def emojis(self):
         print("you can send message with emojis to people")


dinesh = whatsappv3()
print("v3")
dinesh.message()
dinesh.emojis()


dinesh = whatsappv2()
print("v2")
dinesh.message()
dinesh.stickers()

'''
#hybrid->combination of 
'''
class whatsappv1:
    def message(self):
        print("you can send message to people")
class whatsappv2(whatsappv1):
    def stickers(self):
         print("you can send message with stickers to people") 

class whatsappv3(whatsappv1):
    def emojis(self):
         print("you can send message with emojis to people")

class whatsappv4(whatsappv3,whatsappv2):
    def gif(self):
         print("you can send message with gif to people")


dinesh = whatsappv4()
print("v4")
dinesh.message()
dinesh.emojis()
dinesh.stickers()
dinesh.gif()
'''

