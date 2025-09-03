import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv(r"C:\Users\paruo\OneDrive\Desktop\smart_logistics_dataset.csv")  

# Overview
print("===== Dataset Overview =====")
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Missing values:\n", df.isnull().sum(), "\n")

print("===== Queries & Answers =====\n")

# Q1: How many unique assets are tracked?
q1 = df['Asset_ID'].nunique()
print(f"Q1: Number of unique assets tracked?\nA1: {q1}\n")

# Q2: What percentage of shipments faced logistics delay?
q2 = df['Logistics_Delay'].mean() * 100
print(f"Q2: Percentage of delayed shipments?\nA2: {q2:.2f}%\n")

# Q3: What is the average, min, and max waiting time?
q3_avg = df['Waiting_Time'].mean()
q3_min = df['Waiting_Time'].min()
q3_max = df['Waiting_Time'].max()
print(f"Q3: Waiting time stats?\nA3: Avg = {q3_avg:.2f}, Min = {q3_min}, Max = {q3_max}\n")

# Q4: Which logistics delay reason occurs most often?
if 'Logistics_Delay_Reason' in df.columns:
    q4 = df['Logistics_Delay_Reason'].value_counts().head(3)
    print("Q4: Top 3 logistics delay reasons?\nA4:\n", q4, "\n")

# Q5: What is the average asset utilization rate?
q5 = df['Asset_Utilization'].mean()
print(f"Q5: Average asset utilization?\nA5: {q5:.2f}%\n")

# Q6: How does traffic status affect delays?
q6 = df.groupby('Traffic_Status')['Logistics_Delay'].mean() * 100
print("Q6: Delay percentage by traffic condition:\nA6:\n", q6, "\n")

# Q7: What is the average monthly waiting time trend?
df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
df['Month'] = df['Timestamp'].dt.to_period('M')
q7 = df.groupby('Month')['Waiting_Time'].mean().head(12)
print("Q7: Avg monthly waiting time (first 12 months):\nA7:\n", q7, "\n")

# Q8: Which shipment status is most common?
q8 = df['Shipment_Status'].value_counts()
print("Q8: Shipment status distribution?\nA8:\n", q8, "\n")

# Q9: Compare demand forecast vs inventory levels
q9_demand = df['Demand_Forecast'].mean()
q9_inventory = df['Inventory_Level'].mean()
print(f"Q9: Avg Demand Forecast = {q9_demand:.2f}, Avg Inventory Level = {q9_inventory:.2f}\n")

# Q10: Which assets experience the most delays?
q10 = df.groupby('Asset_ID')['Logistics_Delay'].sum().sort_values(ascending=False).head(5)
print("Q10: Top 5 assets with most delays:\nA10:\n", q10, "\n")
