import requests

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error fetching data. Check your internet connection or currency code.")
        return None
    
    data = response.json()
    rates = data.get("rates", {})
    return rates.get(target_currency, None)

def convert_currency(amount, base_currency, target_currency):
    rate = get_exchange_rate(base_currency, target_currency)
    if rate is None:
        print("Conversion error. Please check input data.")
        return None
    return amount * rate

def main():
    print("Simple Currency Converter")
    base_currency = input("Enter base currency (e.g., USD): ").upper()
    target_currency = input("Enter target currency (e.g., EUR): ").upper()
    amount = float(input("Enter amount: "))
    
    result = convert_currency(amount, base_currency, target_currency)
    if result is not None:
        print(f"{amount} {base_currency} = {result:.2f} {target_currency}")

if __name__ == "__main__":
    main()
