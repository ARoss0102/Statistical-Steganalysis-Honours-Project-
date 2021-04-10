from stegano import lsb

# print("1 Create")
# print("2 Read")
# option  = input(":")

img = input("please enter the image you wish to use: ")
# msg = input("please enter the text you wish to conceal: ")
file = open("small_file.txt", "r", encoding="utf8")

# print(msg.read())
msg = str(file.read())

stego = lsb.hide(img, msg)

save = input("please enter the name you wish to save this image as: ")#

stego.save(save)

print(lsb.reveal(stego))
