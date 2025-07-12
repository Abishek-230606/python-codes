import pandas as pd 
import matplotlib.pyplot as plt

a = pd.read_csv("data-visualization-practice/orders.csv")
print(a)
print("--------------------------------------")

dfa = pd.DataFrame(a)

dfa["Total_price"] = dfa["Quantity"]*dfa["Price_per_item"]

dfa.to_csv("updated_orders.csv",index = False)
print("--------------updated sucessfully------------------")

b = pd.read_csv("updated_orders.csv")
print(b)
print("-------------------------------------")

dfb = pd.DataFrame(b)

c = dfb.groupby("Category")["Total_price"].sum()
print(c)

plt.figure(figsize=(8,5))  # wider and cleaner

colors = ["#4CAF50", "#2196F3", "#FF9800", "#E91E63"]  # custom colors for bars
plt.bar(c.index, c.values, color=colors, width=0.5, edgecolor='black')

plt.title("Total Sales by Category", fontsize=16, fontweight='bold')
plt.xlabel("Category", fontsize=12)
plt.ylabel("Total Sales (₹)", fontsize=12)

plt.grid(axis='y', linestyle='--', alpha=0.7)  # light horizontal grid
plt.xticks(rotation=10)
plt.tight_layout()
plt.show()

print("Total sales by category have been visualized successfully.")

payment_counts = dfb["Payment_Method"].value_counts()
print(payment_counts)

colors = ["#4CAF50", "#2196F3", "#FFC107"]  # Green, Blue, Orange

plt.pie(payment_counts.values,
        labels=payment_counts.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors)

plt.title("Payment Method Distribution")
plt.axis('equal')  # Keep it a perfect circle
plt.show()

print("Payment method distribution has been visualized successfully.")

plt.figure(figsize=(8, 5))

plt.hist(dfb["Total_price"], bins=5, color="#03A9F4", edgecolor="black")

plt.title("Order Price Distribution", fontsize=15, fontweight="bold")
plt.xlabel("Total Order Price (₹)", fontsize=12)
plt.ylabel("Number of Orders", fontsize=12)

plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

print("Order price distribution has been visualized successfully.")