import requests
import csv

def scrape_daraz_mobiles(query="mobile", pages=2):
    headers = {"User-Agent": "Mozilla/5.0"}
    all_products = []

    for page in range(1, pages + 1):
        url = f"https://www.daraz.com.np/catalog/?q={query}&page={page}&ajax=true"
        print(f"Fetching page {page} → {url}")
        r = requests.get(url, headers=headers)
        if r.status_code != 200:
            print(f"❌ Failed to fetch page {page}")
            continue

        data = r.json()
        items = data.get("mods", {}).get("listItems", [])
        print(f"➡️ Found {len(items)} items on page {page}")

        for item in items:
            name = item.get("name")
            price = item.get("priceShow") or item.get("price")
            if name and price:
                all_products.append((name, f"Rs. {price}"))

    print(f"✅ Total: {len(all_products)} mobiles collected")

    # Save to CSV
    with open("mobiles.csv", "w", encoding="utf-8", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Mobile Name", "Price"])
        writer.writerows(all_products)

    print("✅ Saved to mobiles.csv")

if __name__ == "__main__":
    scrape_daraz_mobiles(pages=3)

