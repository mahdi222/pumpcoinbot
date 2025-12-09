import requests
import json

# آدرس API سایت CoinGecko برای گرفتن اطلاعات بازار
# vs_currency=usd: قیمت‌ها را بر اساس دلار آمریکا بگیر
# market_cap_less_than=200000000: فیلتر برای مارکت کپ زیر 200 میلیون دلار
# per_page=250: حداکثر تعداد ارز در هر صفحه (برای اینکه چیزی از قلم نیفتد)
# page=1: صفحه اول نتایج
url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&market_cap_less_than=200000000&order=market_cap_desc&per_page=250&page=1"

print("در حال دریافت اطلاعات از CoinGecko...")

try:
    # ارسال درخواست به سرور CoinGecko
    response = requests.get(url)
    
    # بررسی اینکه آیا درخواست موفقیت‌آمیز بوده است (Status Code 200)
    response.raise_for_status()
    
    # تبدیل پاسخ متنی (JSON) به یک لیست از دیکشنری‌های پایتون
    coins = response.json()
    
    print(f"تعداد {len(coins)} ارز با مارکت کپ زیر 200 میلیون دلار پیدا شد.")
    print("-" * 40) # یک خط جداکننده برای خوانایی بهتر

    # چاپ اطلاعات 10 ارز برتر در این لیست
    for coin in coins[:10]: # فقط 10 تای اول را نمایش می‌دهیم تا خروجی شلوغ نشود
        name = coin.get('name')
        symbol = coin.get('symbol').upper()
        market_cap = coin.get('market_cap')
        
        # استفاده از f-string برای فرمت‌دهی زیبا و خوانا
        print(f"نام: {name} ({symbol})")
        print(f"مارکت کپ: ${market_cap:,}") # علامت ویرگول برای جدا کردن هزارگان
        print("-" * 20)

except requests.exceptions.RequestException as e:
    print(f"خطا در برقراری ارتباط با سرور: {e}")
except json.JSONDecodeError:
    print("خطا: پاسخ دریافت شده از سرور در فرمت JSON معتبر نیست.")

