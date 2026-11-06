from PIL import Image

# Load the images and let's inspect sizes
img1 = Image.open("WhatsApp Image 2026-11-06 at 8.20.07 AM.jpeg")
print("Pink slip size:", img1.size)

# Bottom section of pink slip
# size is (900, 1600)
w, h = img1.size
bottom_crop = img1.crop((0, int(h * 0.6), w, h))
bottom_crop.save("crop_pink_bottom.jpg")

# Also let's check top of pink slip
top_crop = img1.crop((0, 0, w, int(h * 0.4)))
top_crop.save("crop_pink_top.jpg")

print("Cropped successfully")
