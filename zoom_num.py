from PIL import Image

im = Image.open("WhatsApp Image 2026-11-06 at 8.20.07 AM.jpeg")
w, h = im.size

# The number is located around x: 40% to 65%, y: 64% to 75%
crop_num = im.crop((int(w * 0.4), int(h * 0.65), int(w * 0.65), int(h * 0.73)))
crop_num.save("crop_blue_num.jpg")
print("Cropped blue num")
