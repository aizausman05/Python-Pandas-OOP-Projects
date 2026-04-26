import pandas as pd
class Product:
    def __init__(self, prod_id, price):
        self.prod_id = prod_id
        self.price = price
    def apply_discount(self, percent_off):
        self.price = self.price - (self.price * percent_off / 100)
        return self.price
df = pd.read_csv("k_products.csv")
electronics_df = df[df["Category"] == "Electronics"].copy()
discounted_prices = []
for _, row in electronics_df.iterrows():
    product = Product(row["Product_ID"], row["Price"])
    new_price = product.apply_discount(20)
    discounted_prices.append(new_price)
electronics_df["Price"] = discounted_prices
electronics_df["Promo_Active"] = "Yes"
electronics_df.to_excel("m_holiday_promos.xlsx", index=False)
print("Discount applied successfully!")
print(electronics_df)