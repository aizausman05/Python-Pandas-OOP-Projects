import pandas as pd
class Ingredient:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
    def use_item(self, amount):
        self.quantity -= amount
df = pd.read_csv("d_morning_stock.csv")
df.rename(columns={"Qty_kg": "Current_Quantity"}, inplace=True)
df["Current_Quantity"] = df["Current_Quantity"].astype(float)
coffee_row = df[df["Ingredient"] == "Coffee Beans"]
coffee_name = coffee_row["Ingredient"].values[0]
coffee_qty = coffee_row["Current_Quantity"].values[0]
coffee_obj = Ingredient(coffee_name, coffee_qty)
coffee_obj.use_item(2.5)
df.loc[df["Ingredient"] == "Coffee Beans", "Current_Quantity"] = coffee_obj.quantity
df.to_csv("f_Evening_stock.csv", index=False)
print("Evening Stock Updated Successfully")