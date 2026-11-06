from PIL import Image

imgs = [
    ("WhatsApp Image 2026-11-06 at 8.20.07 AM.jpeg", "pink"),
    ("WhatsApp Image 2026-11-06 at 8.20.07 AM (1).jpeg", "white1"),
    ("WhatsApp Image 2026-11-06 at 8.20.07 AM (2).jpeg", "white2"),
    ("WhatsApp Image 2026-11-06 at 8.20.08 AM.jpeg", "white3"),
]

for filename, tag in imgs:
    im = Image.open(filename)
    w, h = im.size
    # crop top 25%
    im.crop((0, 0, w, int(h * 0.25))).save(f"crop_{tag}_top.jpg")
    # crop bottom 25%
    im.crop((0, int(h * 0.75), w, h)).save(f"crop_{tag}_bottom.jpg")

print("All crops saved")
