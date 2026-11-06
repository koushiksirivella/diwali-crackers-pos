import json

with open("check_data.py", "r", encoding="utf-8") as f:
    code = f.read()

# We can directly import the data structures or execute
namespace = {}
exec(code, namespace)

pink_bill = namespace["pink_bill"]
white_bill = namespace["white_bill"]

all_items = []
# Default selling price suggestion: Rate * 1.10 * 1.40 (or reasonable retail price rounded to nearest 5)
def suggest_sp(rate):
    cost_with_overhead = rate * 1.10
    # Add ~40-50% retail margin, rounded up to next 5 or 10
    raw_sp = cost_with_overhead * 1.40
    if raw_sp <= 50:
        return int(round(raw_sp / 5) * 5) or 5
    elif raw_sp <= 200:
        return int(round(raw_sp / 10) * 10)
    else:
        return int(round(raw_sp / 50) * 50) or int(round(raw_sp / 10) * 10)

for item in white_bill:
    rate = item["rate"]
    rate_10 = round(rate * 1.10, 2)
    units = item["units"]
    item_entry = {
        "id": f"W_{item['bill_item_no']}",
        "sticker_no": str(item["bill_item_no"]),
        "search_keys": [str(item["bill_item_no"]), item["name"].lower()],
        "bill_type": "white",
        "bill_name": "White Bill (Nandigama)",
        "bill_item_no": item["bill_item_no"],
        "name": item["name"],
        "pack_details": item["pack_details"],
        "units": units,
        "rate": rate,
        "rate_plus_10": rate_10,
        "bill_total": item["bill_total"],
        "total_plus_10": round(units * rate_10, 2),
        "suggested_selling_price": suggest_sp(rate),
        "selling_price": suggest_sp(rate),
        "verified": False,
        "verified_at": None,
        "notes": ""
    }
    all_items.append(item_entry)

for item in pink_bill:
    rate = item["rate"]
    rate_10 = round(rate * 1.10, 2)
    units = item["units"]
    item_entry = {
        "id": f"P_{item['bill_item_no']}",
        "sticker_no": f"P{item['bill_item_no']}",
        "search_keys": [f"p{item['bill_item_no']}", str(item["bill_item_no"]), str(100 + item["bill_item_no"]), item["name"].lower()],
        "bill_type": "pink",
        "bill_name": "Pink Bill (Chilakaluripet)",
        "bill_item_no": item["bill_item_no"],
        "name": item["name"],
        "pack_details": item["pack_details"],
        "units": units,
        "rate": rate,
        "rate_plus_10": rate_10,
        "bill_total": item["bill_total"],
        "total_plus_10": round(units * rate_10, 2),
        "suggested_selling_price": suggest_sp(rate),
        "selling_price": suggest_sp(rate),
        "verified": False,
        "verified_at": None,
        "notes": ""
    }
    all_items.append(item_entry)

with open("items_data.json", "w", encoding="utf-8") as f:
    json.dump(all_items, f, indent=2)

print(f"Total items generated: {len(all_items)}")
print(f"Total stock value: {sum(x['bill_total'] for x in all_items)}")
