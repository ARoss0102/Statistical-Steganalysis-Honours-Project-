# This code uses the work of C. Bonhomme, “Stegano,” Dec. 20, 2019.
# https://pypi.org/project/stegano/

from stegano import lsb


img = input("please enter the image you wish to use: ")
# Change the filename and encoding as required
file = open("small_file.txt", "r", encoding="utf8")

msg = str(file.read())

stego = lsb.hide(img, msg)

save = input("please enter the name you wish to save this image as: ")#

stego.save(save)

print(lsb.reveal(stego))
