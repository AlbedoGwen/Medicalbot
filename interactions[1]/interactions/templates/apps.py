import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Generate random data
def generate_data(size=1000):
    np.random.seed(42)
    data = {
        "Age": np.random.randint(18, 65, size),
        "Salary": np.random.randint(20000, 120000, size),
        "Experience": np.random.randint(1, 40, size),
        "Department": np.random.choice(["HR", "Tech", "Sales", "Marketing", "Finance"], size),
        "Satisfaction": np.random.uniform(1, 10, size)
    }
    return pd.DataFrame(data)

# Process data
def process_data(df):
    df["Salary"] = df["Salary"].apply(lambda x: x if x > 30000 else 30000)
    df["Experience"] = df["Experience"].apply(lambda x: x if x > 1 else 1)
    return df

# Visualize data
def visualize_data(df):
    plt.figure(figsize=(12, 6))
    sns.histplot(df["Salary"], bins=30, kde=True, color="blue")
    plt.title("Salary Distribution")
    plt.xlabel("Salary")
    plt.ylabel("Frequency")
    plt.show()
    
    plt.figure(figsize=(12, 6))
    sns.boxplot(x="Department", y="Salary", data=df)
    plt.title("Salary by Department")
    plt.xlabel("Department")
    plt.ylabel("Salary")
    plt.show()
    
    plt.figure(figsize=(12, 6))
    sns.scatterplot(x="Experience", y="Salary", hue="Department", data=df)
    plt.title("Experience vs Salary")
    plt.xlabel("Years of Experience")
    plt.ylabel("Salary")
    plt.show()
    
    plt.figure(figsize=(10, 5))
    sns.violinplot(x="Department", y="Satisfaction", data=df)
    plt.title("Employee Satisfaction by Department")
    plt.xlabel("Department")
    plt.ylabel("Satisfaction Level")
    plt.show()

if __name__ == "__main__":

    df = generate_data(1000)
    df = process_data(df)
    visualize_data(df)