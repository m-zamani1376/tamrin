import json
json_path = r"C:\Users\Etezadi\Desktop\New.txt"

try:
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    all_titles = []

    for post in data.get("posts", []):
        if post.get("title"):
            all_titles.append(post["title"])

        for tag in post.get("tags", []):
            if tag.get("title"):
                all_titles.append(tag["title"])

        for prod in post.get("products", []):
            t = prod.get("title_fa") or prod.get("title")
            if t:
                all_titles.append(t)

    print("لیست همه تایتل‌ها:")
    for title in all_titles:
        print("-", title)
    print("تعداد کل تایتل‌ها:", len(all_titles))

except FileNotFoundError:
    print("فایل مورد نظر پیدا نشد.")
except json.JSONDecodeError:
    print("خطا در خواندن داده‌های JSON.")
except Exception as e:
    print("یک خطای غیرمنتظره رخ داد:", e)
