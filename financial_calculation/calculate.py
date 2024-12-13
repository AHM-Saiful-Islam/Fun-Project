import pandas as pd

# Initialize variables
initial_balance = 2_500_000  # Initial deposit
interest_rate = 0.0225  # Quarterly interest (9% annual divided by 4)
payment_per_quarter = 210_000  # Builder payment every 3 months
total_months = 36  # Total duration
quarters = total_months // 3  # Total quarters

# Initialize data storage
data = []

# Simulation loop
current_balance = initial_balance
for q in range(1, quarters + 1):
    # Calculate interest earned for the quarter
    interest = current_balance * interest_rate
    # Calculate balance after interest and withdrawal
    end_balance = current_balance + interest - payment_per_quarter
    # Store results for the quarter
    data.append({
        "Quarter": q,
        "Start Balance": round(current_balance, 2),
        "Interest Earned": round(interest, 2),
        "Withdrawal": payment_per_quarter,
        "End Balance": round(end_balance, 2)
    })
    # Update current balance for next quarter
    current_balance = end_balance

# Convert to DataFrame for analysis
df = pd.DataFrame(data)
df
print(df)
df.to_csv("financial_calculation_results.csv", index=False)
