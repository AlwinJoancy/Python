# multilevel inheritance

# phone in 2000


class Phone20:

    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
        self.torchMode = False

    def call(self, phoneNumber):
        print(f"calling to number: {phoneNumber}")

    def torch(self, mode=False):
        self.torchMode = mode

    def displayPhoneDetails(self):
        print(self.name, self.color, self.price, self.torchMode)


# single inheritance

class Phone2002(Phone20):
    def onRadio(self):
        print("radio is on")


class Phone2005(Phone2002):
    def playSong(self):
        print("song is playing now")

    def onRadio(self):
        pass


class ChinaBasePhone:
    def __init__(self, model):
        self.model = model

    def playVideo(self):
        print("video is playing......")


class ChinaPhone(Phone2002, ChinaBasePhone):

    def __init__(self, name, color, price, model):
        Phone2002.__init__(self, name, color, price)
        ChinaBasePhone.__init__(self, model)

    def playAudioWithPlayback(self):
        print("mp3 player is working........")


maryJoancyPhone = Phone2005("Nokia", "grey", 10000)
maryJoancyPhone.displayPhoneDetails()
maryJoancyPhone.torch(True)
maryJoancyPhone.displayPhoneDetails()
maryJoancyPhone.onRadio()
maryJoancyPhone.playSong()


phone1 = ChinaPhone("vivo", "black", 65421, "dsjklf")
phone1.playAudioWithPlayback()
print(phone1.model)
