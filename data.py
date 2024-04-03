import numpy as np
import pandas as pd

num_sampes = 1000

customer_id = np.arange(1, num_sampes + 1)
age = np.random.randint(18, 70, num_sampes)
monthly_spend = np.random.normal(100, 30, num_sampes)
tenure = np.random.randint(0, 60, num_sampes)
support_calls = np.random.randint(0, 5, num_sampes)
plan_type = np.random.choice(['Month-to-month', 'One year', 'Two year'], num_sampes)
subscription_type = np.random.choice(['premium', 'super', 'mobile', 'free'], num_sampes)
monthly_charges = np.random.gamma(50, 20, num_sampes)
churn = np.random.choice(['Yes', 'No'], num_sampes)



data = pd.DataFrame({
    'CustomerID': customer_id,
    'Age': age,
    'MonthlySpend': monthly_spend,
    'Tenure': tenure,
    'SupportCalls': support_calls,
    'PlanType': plan_type,
    'SubscriptionType': subscription_type,
    'MonthlyCharges': monthly_charges,
    'Churn': churn
})

# Save synthetic data to a CSV file
data.to_csv('churn_data.csv', index=False)