import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def univariate(data,col1, col2):
    print('Univariate Analysis')
    filtered_data = data[data[col1] > 1]
    bins_premium = [0, 30, 50, 70, 100, 200, 300, 400, 500]
    bins_claims = [-20000, -10000, 0, 100, 500, 1000, 5000, 10000, 20000, 30000, 40000]


    filtered_data = data[data[col1] > 1]


    fig, axs = plt.subplots(1, 2, figsize=(12, 6))


    negative_claims = data[data[col2] < 0]
    positive_claims = data[data[col2] > 0]


    axs[0].hist(filtered_data[col1], bins=bins_premium, color='blue', alpha=0.7)
    axs[0].set_title(f'Distribution of {col1}')
    axs[0].set_xlabel(col1)
    axs[0].set_ylabel('Frequency')
    axs[0].set_xticks(bins_premium)
    axs[0].grid(axis='y')


    axs[1].hist(negative_claims[col2], bins=bins_claims, color='red', alpha=0.7, label='Negative')
    axs[1].hist(positive_claims[col2], bins=bins_claims, color='green', alpha=0.5, label='Positive')
    axs[1].set_title(f'Distribution of {col2}')
    axs[1].set_xlabel(col2)
    axs[1].set_ylabel('Frequency')
    axs[1].legend()
    axs[1].grid(axis='y')

# Adjust layout
    plt.tight_layout()
    plt.show()


def univariate_others(data, col, ax):
    data[col].value_counts().plot(kind='bar', ax=ax, color=['blue','red','yellow'], alpha=0.7)
    ax.set_title(f'{col} Distribution')
    ax.set_xlabel(col)
    ax.set_ylabel('Count')


def numerical_cols_univariate_analysis(data):
    numerical_cols = data.select_dtypes(include=['float64', 'int64']).columns

    data[numerical_cols].hist(bins=20, figsize=(14, 24), layout=(len(numerical_cols) // 3 + 1, 3))
    plt.suptitle('Distribution of Numerical Variables', fontsize=16)
    plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust layout to make room for the suptitle
    plt.show()

def categorical_cols_univariate_analysis(data):
    categorical_cols = data.select_dtypes(include=['object', 'category']).columns

    fig, axes = plt.subplots(len(categorical_cols), 1, figsize=(12, len(categorical_cols) * 4))

    for i, col in enumerate(categorical_cols):
        data[col].value_counts().plot(kind='bar', ax=axes[i], color='skyblue')
        axes[i].set_title(f'Distribution of {col}', fontsize=14)
        axes[i].set_ylabel('Count')
        axes[i].set_xlabel(col)

    plt.tight_layout()
    plt.show()


def remove_outliers(df):
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 3 * IQR
        upper_bound = Q3 + 3 * IQR
        df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
    
    for col in df.select_dtypes(include=['object', 'category']).columns:
        frequency = df[col].value_counts()
        threshold = 1
        mask = df[col].isin(frequency[frequency > threshold].index)
        df = df[mask]
        
    return df

def plot_trends_by_geography(data, geography_col, trend_cols):
    geography_group = data.groupby(geography_col)

    for col in trend_cols:
        plt.figure(figsize=(10, 6))
        
        if data[col].dtype == 'float64' or data[col].dtype == 'int64':
            #numeric: calculate the mean
            col_mean = geography_group[col].mean()
            col_mean.plot(kind='bar', color='skyblue')
            plt.title(f'Mean {col} by {geography_col}',figsize=(20, 12))
            plt.ylabel(f'Mean {col}')
        
        else:
            #categorical: calculate the distribution
            col_distribution = geography_group[col].value_counts(normalize=True).unstack()
            col_distribution.plot(kind='bar', stacked=True, figsize=(20, 12), colormap='Set3')
            plt.title(f'{col} Distribution by {geography_col}')
            plt.ylabel(f'Proportion of {col}')
        
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.subplots_adjust(right=0.75)
        plt.show()