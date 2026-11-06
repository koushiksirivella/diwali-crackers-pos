import json

white_bill = [
    {"bill_item_no": 1, "name": "3 1/2 Lakshmi (15P)", "pack_details": "20", "units": 20, "rate": 150, "sp": 250},
    {"bill_item_no": 2, "name": "4\" Laxmi", "pack_details": "25", "units": 25, "rate": 150, "sp": 250},
    {"bill_item_no": 3, "name": "4\" Dlx Lion", "pack_details": "10", "units": 10, "rate": 260, "sp": 380},
    {"bill_item_no": 4, "name": "Gold Laxmi", "pack_details": "10", "units": 10, "rate": 280, "sp": 400},
    {"bill_item_no": 5, "name": "5\" Hulk", "pack_details": "10", "units": 10, "rate": 280, "sp": 400},
    {"bill_item_no": 6, "name": "6\" Bruslee", "pack_details": "10", "units": 10, "rate": 330, "sp": 480},
    {"bill_item_no": 7, "name": "2 Sound Crackers", "pack_details": "10", "units": 10, "rate": 280, "sp": 400},
    {"bill_item_no": 8, "name": "3 Sound Colanatia", "pack_details": "10", "units": 10, "rate": 350, "sp": 500},
    {"bill_item_no": 9, "name": "Smoke Bomb", "pack_details": "10", "units": 10, "rate": 250, "sp": 380},
    {"bill_item_no": 10, "name": "28 Cholasa", "pack_details": "10", "units": 10, "rate": 550, "sp": 750},
    {"bill_item_no": 11, "name": "28 Gaint", "pack_details": "10", "units": 10, "rate": 550, "sp": 750},
    {"bill_item_no": 12, "name": "24 Dlx", "pack_details": "5", "units": 5, "rate": 450, "sp": 650},
    {"bill_item_no": 13, "name": "50 Dlx", "pack_details": "5", "units": 5, "rate": 450, "sp": 650},
    {"bill_item_no": 14, "name": "100 mega Dlx", "pack_details": "10", "units": 10, "rate": 350, "sp": 500},
    {"bill_item_no": 15, "name": "18 cm pencil", "pack_details": "50", "units": 50, "rate": 70, "sp": 110},
    {"bill_item_no": 16, "name": "12 cm Pencil Gaint", "pack_details": "20", "units": 20, "rate": 50, "sp": 80},
    {"bill_item_no": 17, "name": "7 cm Pencil", "pack_details": "50", "units": 50, "rate": 22, "sp": 40},
    {"bill_item_no": 18, "name": "100 wala", "pack_details": "50", "units": 50, "rate": 27, "sp": 45},
    {"bill_item_no": 19, "name": "200 wala", "pack_details": "25", "units": 25, "rate": 50, "sp": 80},
    {"bill_item_no": 20, "name": "Rocket Bomb", "pack_details": "50", "units": 50, "rate": 60, "sp": 100},
    {"bill_item_no": 21, "name": "Lunik Rocket", "pack_details": "25", "units": 25, "rate": 90, "sp": 140},
    {"bill_item_no": 22, "name": "Music Rocket", "pack_details": "10", "units": 10, "rate": 120, "sp": 180},
    {"bill_item_no": 23, "name": "Flp Small", "pack_details": "100", "units": 100, "rate": 36, "sp": 60},
    {"bill_item_no": 24, "name": "Flp Spl", "pack_details": "125", "units": 125, "rate": 65, "sp": 100},
    {"bill_item_no": 25, "name": "Flp Gaint", "pack_details": "20", "units": 20, "rate": 120, "sp": 180},
    {"bill_item_no": 26, "name": "WiFi", "pack_details": "10", "units": 10, "rate": 120, "sp": 180},
    {"bill_item_no": 27, "name": "5 Colour mini fountain", "pack_details": "30", "units": 30, "rate": 160, "sp": 240},
    {"bill_item_no": 28, "name": "Clk Dlx Royal", "pack_details": "12", "units": 12, "rate": 330, "sp": 480},
    {"bill_item_no": 29, "name": "Clk Dlx (Leo)", "pack_details": "12", "units": 12, "rate": 350, "sp": 500},
    {"bill_item_no": 30, "name": "Clk Mega Dlx mithra", "pack_details": "10", "units": 10, "rate": 330, "sp": 480},
    {"bill_item_no": 31, "name": "Glc Big (25P)", "pack_details": "24", "units": 24, "rate": 65, "sp": 100},
    {"bill_item_no": 32, "name": "Glc Spl Leo", "pack_details": "75", "units": 75, "rate": 65, "sp": 100},
    {"bill_item_no": 33, "name": "Glc Dlx", "pack_details": "75", "units": 75, "rate": 96, "sp": 150},
    {"bill_item_no": 34, "name": "Wheel Spinner", "pack_details": "30", "units": 30, "rate": 100, "sp": 150},
    {"bill_item_no": 35, "name": "Spinner Spl Royal", "pack_details": "20", "units": 20, "rate": 160, "sp": 240},
    {"bill_item_no": 36, "name": "Wire Chakkar", "pack_details": "10", "units": 10, "rate": 140, "sp": 220},
    {"bill_item_no": 37, "name": "1 1/2 Twinkling", "pack_details": "100", "units": 100, "rate": 18, "sp": 30},
    {"bill_item_no": 38, "name": "4\" Twinkling", "pack_details": "150", "units": 150, "rate": 60, "sp": 100},
    {"bill_item_no": 39, "name": "Hele copter", "pack_details": "20", "units": 20, "rate": 80, "sp": 120},
    {"bill_item_no": 40, "name": "Dola Dola Leo", "pack_details": "100", "units": 100, "rate": 38, "sp": 60},
    {"bill_item_no": 41, "name": "Mega kit kat", "pack_details": "50", "units": 50, "rate": 50, "sp": 80},
    {"bill_item_no": 42, "name": "Ganga Jamuna", "pack_details": "30", "units": 30, "rate": 75, "sp": 120},
    {"bill_item_no": 43, "name": "Flower Bomb vcl", "pack_details": "20", "units": 20, "rate": 150, "sp": 230},
    {"bill_item_no": 44, "name": "Butterfly Yuva", "pack_details": "30", "units": 30, "rate": 70, "sp": 110},
    {"bill_item_no": 45, "name": "2 Comment (P) Window", "pack_details": "10", "units": 10, "rate": 70, "sp": 110},
    {"bill_item_no": 46, "name": "7 shot (10P)", "pack_details": "5", "units": 5, "rate": 200, "sp": 300},
    {"bill_item_no": 47, "name": "4\" comment (1P)", "pack_details": "2", "units": 2, "rate": 760, "sp": 1100},
    {"bill_item_no": 48, "name": "4\" Comment (3P)", "pack_details": "2", "units": 2, "rate": 900, "sp": 1300},
    {"bill_item_no": 49, "name": "Small Bullet Bomb", "pack_details": "150", "units": 150, "rate": 13, "sp": 25},
    {"bill_item_no": 50, "name": "Solar Bomb", "pack_details": "50", "units": 50, "rate": 45, "sp": 75},
    {"bill_item_no": 51, "name": "Classic Bomb", "pack_details": "50", "units": 50, "rate": 92, "sp": 150},
    {"bill_item_no": 52, "name": "Military Bomb", "pack_details": "10", "units": 10, "rate": 165, "sp": 250},
    {"bill_item_no": 53, "name": "Marshal Black", "pack_details": "25", "units": 25, "rate": 160, "sp": 240},
    {"bill_item_no": 54, "name": "Digital Bomb", "pack_details": "20", "units": 20, "rate": 190, "sp": 280},
    {"bill_item_no": 55, "name": "Jurassic Marshal", "pack_details": "20", "units": 20, "rate": 180, "sp": 270},
    {"bill_item_no": 56, "name": "240 Shot (Jyothi)", "pack_details": "3", "units": 3, "rate": 3100, "sp": 4500},
    {"bill_item_no": 57, "name": "Lamp", "pack_details": "15", "units": 15, "rate": 250, "sp": 380},
    {"bill_item_no": 58, "name": "50 Ele", "pack_details": "10", "units": 10, "rate": 130, "sp": 200},
    {"bill_item_no": 59, "name": "50 Colour", "pack_details": "10", "units": 10, "rate": 140, "sp": 210},
    {"bill_item_no": 60, "name": "Robin King Siren", "pack_details": "5", "units": 5, "rate": 65, "sp": 100},
    {"bill_item_no": 61, "name": "Dil Se (1P)", "pack_details": "5", "units": 5, "rate": 210, "sp": 320},
    {"bill_item_no": 62, "name": "Cukoo", "pack_details": "5", "units": 5, "rate": 130, "sp": 200},
    {"bill_item_no": 63, "name": "Butterscotch", "pack_details": "5", "units": 5, "rate": 230, "sp": 350},
    {"bill_item_no": 64, "name": "Golden Rabbit", "pack_details": "5", "units": 5, "rate": 260, "sp": 390},
    {"bill_item_no": 65, "name": "Speed Test mithra", "pack_details": "15", "units": 15, "rate": 125, "sp": 190},
    {"bill_item_no": 66, "name": "900 cc", "pack_details": "10", "units": 10, "rate": 130, "sp": 200},
    {"bill_item_no": 67, "name": "Turbo wheel", "pack_details": "10", "units": 10, "rate": 80, "sp": 130},
    {"bill_item_no": 68, "name": "Top Gun", "pack_details": "5", "units": 5, "rate": 180, "sp": 270},
    {"bill_item_no": 69, "name": "Pistol 58", "pack_details": "5", "units": 5, "rate": 230, "sp": 350},
    {"bill_item_no": 70, "name": "Bada Peacock Standard", "pack_details": "5", "units": 5, "rate": 250, "sp": 380},
    {"bill_item_no": 71, "name": "Chota Bhai Siren", "pack_details": "9", "units": 9, "rate": 170, "sp": 260},
    {"bill_item_no": 72, "name": "Big Elephant", "pack_details": "5", "units": 5, "rate": 200, "sp": 300},
    {"bill_item_no": 73, "name": "Bat & Ball", "pack_details": "2", "units": 2, "rate": 350, "sp": 500},
    {"bill_item_no": 74, "name": "Wicked Willow Rocket", "pack_details": "6", "units": 6, "rate": 300, "sp": 450}
]

pink_bill = [
    {"bill_item_no": 1, "name": "100 Bijili", "pack_details": "1 x 300", "units": 300, "rate": 25, "sp": 40},
    {"bill_item_no": 2, "name": "CLK Ishwarya", "pack_details": "1 x 60", "units": 60, "rate": 160, "sp": 240},
    {"bill_item_no": 3, "name": "FLP Ashoka", "pack_details": "1 x 100", "units": 100, "rate": 85, "sp": 130},
    {"bill_item_no": 4, "name": "7 CM Electric", "pack_details": "4", "units": 4, "rate": 1000, "sp": 1500},
    {"bill_item_no": 5, "name": "15 CM Colour", "pack_details": "3 x 100", "units": 300, "rate": 30, "sp": 50},
    {"bill_item_no": 6, "name": "15 CM Electric", "pack_details": "3 x 100", "units": 300, "rate": 28, "sp": 45},
    {"bill_item_no": 7, "name": "30 CM Colour", "pack_details": "3 x 100", "units": 300, "rate": 30, "sp": 50},
    {"bill_item_no": 8, "name": "30 CM Electric", "pack_details": "3 x 100", "units": 300, "rate": 28, "sp": 45},
    {"bill_item_no": 9, "name": "1K Wala", "pack_details": "1 x 36", "units": 36, "rate": 130, "sp": 200},
    {"bill_item_no": 10, "name": "2K Wala", "pack_details": "1 x 20", "units": 20, "rate": 260, "sp": 390},
    {"bill_item_no": 11, "name": "5K Wala", "pack_details": "1 x 8", "units": 8, "rate": 650, "sp": 950},
    {"bill_item_no": 12, "name": "10K Wala", "pack_details": "1 x 5", "units": 5, "rate": 1300, "sp": 1900},
    {"bill_item_no": 13, "name": "30 Shot", "pack_details": "1 x 18", "units": 18, "rate": 380, "sp": 580},
    {"bill_item_no": 14, "name": "60 Shot", "pack_details": "1 x 12", "units": 12, "rate": 760, "sp": 1150},
    {"bill_item_no": 15, "name": "120 Shot", "pack_details": "1 x 6", "units": 6, "rate": 1520, "sp": 2350},
    {"bill_item_no": 16, "name": "12 Shot Himalaya", "pack_details": "1 x 36", "units": 36, "rate": 138, "sp": 210},
    {"bill_item_no": 17, "name": "Robin Big Kids", "pack_details": "1 x 60", "units": 60, "rate": 42, "sp": 70},
    {"bill_item_no": 18, "name": "Robin 5 Star", "pack_details": "1 x 40", "units": 40, "rate": 125, "sp": 190},
    {"bill_item_no": 19, "name": "Mathabu", "pack_details": "2 x 50", "units": 100, "rate": 58, "sp": 90},
    {"bill_item_no": 20, "name": "Look Pots", "pack_details": "2 x 100", "units": 200, "rate": 21, "sp": 35}
]

items = []

for item in white_bill:
    num_str = str(item["bill_item_no"])
    rate = item["rate"]
    rate_10 = round(rate * 1.10, 2)
    units = item["units"]
    items.append({
        "id": f"W_{num_str}",
        "sticker_no": num_str,
        "lot_no": "WHITE",
        "bill_type": "white",
        "bill_name": "White Bill (Nandigama)",
        "bill_item_no": item["bill_item_no"],
        "name": item["name"],
        "pack_details": item["pack_details"],
        "total_units": units,
        "units_sold": 0,
        "rate": rate,
        "rate_plus_10": rate_10,
        "bill_total": units * rate,
        "selling_price": item["sp"],
        "verified": False,
        "verified_at": None,
        "notes": "",
        "search_keys": [num_str, item["name"].lower()]
    })

for item in pink_bill:
    num_str = f"1294-{item['bill_item_no']}"
    rate = item["rate"]
    rate_10 = round(rate * 1.10, 2)
    units = item["units"]
    items.append({
        "id": f"P_{item['bill_item_no']}",
        "sticker_no": num_str,
        "lot_no": "1294",
        "bill_type": "pink",
        "bill_name": "Pink Bill 1294 (Chilakaluripet)",
        "bill_item_no": item["bill_item_no"],
        "name": item["name"],
        "pack_details": item["pack_details"],
        "total_units": units,
        "units_sold": 0,
        "rate": rate,
        "rate_plus_10": rate_10,
        "bill_total": units * rate,
        "selling_price": item["sp"],
        "verified": False,
        "verified_at": None,
        "notes": "",
        "search_keys": [
            "1294",
            num_str,
            f"1294 {item['bill_item_no']}",
            f"p{item['bill_item_no']}",
            f"pink {item['bill_item_no']}",
            str(item["bill_item_no"]),
            item["name"].lower()
        ]
    })

with open("items_data.json", "w", encoding="utf-8") as f:
    json.dump(items, f, indent=2)

print("Updated items_data.json with lot 1294 and searchable numbers!")
