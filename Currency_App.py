#Currency App ($ , ¥ , ₹ , €)

amount1 = float(input("Enter amount that need's to be Converted: "))

currency1 = input("Enter your Current Currency ($ , ¥ , ₹ , €) : ").strip()

currency2 = input("Enter Curency you want to Convert into ($ , ¥ , ₹ , €) : ").strip()

rates = {
    ('$','¥'): 158.93,
    ('$','€'): 0.86,
    ('$','₹'): 95.11,
    ('¥','$'): 0.0063,
    ('¥','₹'): 0.60,
    ('¥','€'): 0.0054,
    ('₹','¥'): 1.67,
    ('₹','€'): 0.0091,
    ('₹','$'): 0.011,
    ('€','₹'): 110.03,
    ('€','$'): 1.16,
    ('€','¥'): 183.96,
}

if currency1 == currency2:
    print(amount1)
else:
    rate = rates.get((currency1, currency2))
    if rate is not None:
        print(amount1 * rate)
    else:
        print("Invalid Currency Entered")