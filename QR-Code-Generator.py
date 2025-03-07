import qrcode as qr


ChannelName = input("Enter the YouTube Channel Name : ")

QrData = "https://www.youtube.com/@" + ChannelName

QrImg = qr.make(QrData)

QrImg.save(ChannelName + ".png")


