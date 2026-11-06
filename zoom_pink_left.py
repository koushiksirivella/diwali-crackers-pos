from PIL import Image

im = Image.open("WhatsApp Image 2026-11-06 at 8.20.07 AM.jpeg")
w, h = im.size

# Left column (No. and description start)
# y from 15% to 65%, x from 20% to 50%
im.crop((int(w * 0.2), int(h * 0.18), int(w * 0.55), int(h * 0.65))).save("crop_pink_left_col.jpg")
print("Cropped pink left column")
