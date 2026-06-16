import pandas as pd
import numpy as np

def clean_and_profile_business_data(file_path):
    """
    Simulates screening raw retail/business data for anomalies, 
    duplicate records, and severe statistical outliers before modeling.
    """
    # Load data
    try:
        df = pd.read_csv(file_path)
        print(f"Successfully loaded dataset with {df.shape[0]} records.")
    except Exception as e:
        return f"Error loading file: {e}"

    # Check 1: Identify Missing Business Information (Data Completeness)
    missing_data = df.isnull().sum()
    print("\n--- Missing Data Analysis ---")
    print(missing_data[missing_data > 0] if missing_data.sum() > 0 else "No missing data detected.")

    # Check 2: Deduplication (Fixing inflated metrics)
    duplicate_count = df.duplicated().sum()
    if duplicate_count > 0:
        print(f"\n[ALERT] Found {duplicate_count} exact duplicate rows. Removing duplicates...")
        df = df.drop_duplicates()
    else:
        print("\nNo duplicate records found.")

    # Check 3: Outlier Detection using Statistical Z-Scores
    # We flag any numeric metric that deviates wildly from the business average
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    print("\n--- Anomaly & Outlier Screening (Z-Score > 3 Standard Deviations) ---")
    
    for col in numeric_cols:
        mean = df[col].mean()
        std = df[col].std()
        if std > 0:
            outliers = df[(df[col] - mean).abs() > 3 * std]
            if not outliers.empty:
                print(f"[ANOMALY FOUND] Column '{col}' contains {len(outliers)} statistical outliers!")
                print(outliers[[col]].head(3))
            else:
                print(f"Column '{col}' looks healthy (values are normally distributed).")
                
    return df

# Example usage on portfolio data:
# clean_df = clean_and_profile_business_data("your_uploaded_store_file.csv")
