import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load dataset
df = pd.read_csv("C:/Users/hp/OneDrive/Desktop/datasets/supply_chain_data.csv")
print(df.head())
print(df.columns.tolist())
print(df.shape)

# 2. Basic info
print("\n--- Basic Info ---")
print(df.describe())
print(df.isnull().sum())

# 3. Lead Time Analysis
print("\n--- Lead Time Analysis ---")
avg_lead = df.groupby('Product type')['Lead times'].mean().round(2)
print(avg_lead)

plt.figure(figsize=(8, 5))
avg_lead.plot(kind='bar', color=['#1B2A6B', '#0D9488', '#4F46E5'])
plt.title('Average Lead Time by Product Type')
plt.xlabel('Product Type')
plt.ylabel('Lead Time (days)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('lead_time_analysis.png')
plt.show()

# 4. Stock-to-Sales Ratio
print("\n--- Stock to Sales Ratio ---")
df['Stock_to_Sales_Ratio'] = df['Stock levels'] / (df['Number of products sold'] + 1)
stock_ratio = df.groupby('Product type')['Stock_to_Sales_Ratio'].mean().round(2)
print(stock_ratio)

plt.figure(figsize=(8, 5))
stock_ratio.plot(kind='bar', color=['#1B2A6B', '#0D9488', '#4F46E5'])
plt.title('Stock-to-Sales Ratio by Product Type')
plt.xlabel('Product Type')
plt.ylabel('Stock to Sales Ratio')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('stock_to_sales_ratio.png')
plt.show()

# 5. Supplier Performance
print("\n--- Supplier Performance ---")
supplier_perf = df.groupby('Supplier name').agg({
    'Lead times': 'mean',
    'Defect rates': 'mean',
    'Number of products sold': 'sum'
}).round(2)
print(supplier_perf)

# 6. Shipping Bottlenecks
print("\n--- Shipping Bottlenecks ---")
shipping = df.groupby('Shipping carriers')['Shipping times'].mean().round(2)
print(shipping)

plt.figure(figsize=(8, 5))
shipping.plot(kind='bar', color=['#1B2A6B', '#0D9488', '#4F46E5', '#F59E0B'])
plt.title('Average Shipping Time by Carrier')
plt.xlabel('Shipping Carrier')
plt.ylabel('Shipping Time (days)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('shipping_bottlenecks.png')
plt.show()

# 7. Revenue by Product Type
print("\n--- Revenue by Product Type ---")
revenue = df.groupby('Product type')['Revenue generated'].sum().round(2)
print(revenue)

plt.figure(figsize=(6, 6))
revenue.plot(kind='pie', autopct='%1.1f%%',
             colors=['#1B2A6B', '#0D9488', '#4F46E5'])
plt.title('Revenue by Product Type')
plt.ylabel('')
plt.savefig('revenue_by_product.png')
plt.show()

# 8. Save report
report = df.groupby('Product type').agg({
    'Lead times': 'mean',
    'Stock levels': 'mean',
    'Number of products sold': 'sum',
    'Revenue generated': 'sum',
    'Defect rates': 'mean'
}).round(2)
report.to_excel('supply_chain_report.xlsx')
print("\nReport saved!")
print("Done!")