# pip install qrcode[pil]

import qrcode

image = qrcode.make("https://www.linkedin.com/in/aryanbarde80/") #in double quotes paste link of the thing you want qr of.

image.save("Linkedin_Aryan.png") #in double quotes give name by which you want to save image of the qr code
