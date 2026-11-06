from PIL import Image

im = Image.open("WhatsApp Image 2026-11-06 at 8.20.08 AM.jpeg")
w, h = im.size

# Let's crop the entire bottom-left and middle of this page
im.crop((int(w * 0.1), int(h * 0.3), int(w * 0.9), int(h * 0.95))).save("crop_white3_full_bottom.jpg")
print("Saved white3 full bottom")
