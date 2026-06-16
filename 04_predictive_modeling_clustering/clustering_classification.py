"""
Business Predictive Modeling Engine
Translating Unsupervised Clustering (PCA) and Supervised Classification 
(KNN / Naive Bayes) from Orange Workflows into Production-Ready Python Scripts.
"""

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


def run_customer_segmentation_pipeline(data_path, n_components=2, n_clusters=3):
    """Executes Unsupervised Learning: Principal Component Analysis (PCA)

    followed by K-Means Clustering to group complex customer behaviors automatically.
    """
    print("--- STARTING UNSUPERVISED CUSTOMER SEGMENTATION ENGINE ---")

    # 1. Load Data
    df = pd.read_csv(data_path)

    # Separate features (Assumes all numeric columns represent behavior profiles)
    features = df.select_dtypes(include=[np.number])

    # 2. Scale Features (Crucial for KNN, PCA, and Clustering metrics)
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    # 3. Apply PCA (Dimensionality Reduction)
    pca = PCA(n_components=n_components)
    pca_transformed = pca.fit_transform(scaled_features)

    explained_variance = np.sum(pca.explained_variance_ratio_) * 100
    print(
        f"[PCA COMPLETE] Compressed {features.shape[1]} metrics into {n_components} main variables."
    )
    print(f"Total Explained Variance: {explained_variance:.2f}%")

    # 4. Apply K-Means Clustering (Automated Segment Profiling)
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(scaled_features)

    # Attach results back to the corporate dataset
    df["Principal_Component_1"] = pca_transformed[:, 0]
    df["Principal_Component_2"] = pca_transformed[:, 1]
    df["Customer_Segment_ID"] = cluster_labels

    print(
        f"[CLUSTERING COMPLETE] Organized customer database into {n_clusters} natural behavioral groups.\n"
    )
    return df


def run_supervised_classification_pipeline(df, target_column):
    """Executes Supervised Learning: Compares K-Nearest Neighbors (KNN) vs.

    Naive Bayes to predict specific upcoming customer choices (e.g., product
    purchases).
    """
    print("--- STARTING SUPERVISED PREDICTIVE PIPELINE ---")

    # Prepare inputs and targets
    X = df.select_dtypes(include=[np.number]).drop(
        columns=[target_column], errors="ignore"
    )
    y = df[target_column]

    # Handle Train/Test partition split (80/20 distribution architecture)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )

    # --- MODEL 1: K-Nearest Neighbors Classifier ---
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)
    knn_preds = knn.predict(X_test)

    # --- MODEL 2: Naive Bayes Probabilistic Classifier ---
    nb = GaussianNB()
    nb.fit(X_train, y_train)
    nb_preds = nb.predict(X_test)

    # --- PERFORMANCE MATRIX BENCHMARKING ---
    print("\n================ KNN CLASSIFIER MATRIX ================")
    print(classification_report(y_test, knn_preds))

    print("\n============ NAIVE BAYES CLASSIFIER MATRIX ============")
    print(classification_report(y_test, nb_preds))


# Example pipeline execution configuration:
# if __name__ == "__main__":
#     # 1. Cluster the raw client behavioral dataset
#     processed_df = run_customer_segmentation_pipeline('Ejemplo3_Bank_Clients.csv')
#
#     # 2. Predict target choice actions (e.g., 'Target_Product_Accepted')
#     run_supervised_classification_pipeline(processed_df, target_column='Customer_Segment_ID')
