def info(data):
    numerical_cols = ['TotalPremium', 'TotalClaims'] 

    summary = data[numerical_cols].describe()
    print("Summary Statistics:\n", summary)

    variability = data[numerical_cols].var()
    std_dev = data[numerical_cols].std()

    print("Variance:\n", variability)
    print("Standard Deviation:\n", std_dev)

def check_missing(data):
    missing_values = data.isnull().sum()

# Output missing values information
    print("\nMissing Values:\n", missing_values[missing_values>0])



