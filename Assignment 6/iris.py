import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# 2. Load the dataset
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names

# Convert to pandas DataFrame for easier handling
data = pd.DataFrame(data=X, columns=feature_names)
data['species'] = [target_names[i] for i in y]

# 3. Summarize the dataset
print("Dimensions of the dataset:")
print(data.shape)

print("\nPeek at the data:")
print(data.head())

print("\nStatistical summary of all attributes:")
print(data.describe())

print("\nBreakdown of the data by the class variable:")
print(data['species'].value_counts())

# 4. Visualize the dataset

# Univariate plots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))
for i, feature in enumerate(feature_names):
    sns.histplot(data[feature], kde=True, ax=axes[i // 2, i % 2])
    axes[i // 2, i % 2].set_title(f'Distribution of {feature}')

plt.tight_layout()
plt.show()

# Multivariate plots
sns.pairplot(data, hue='species')
plt.show()

# 5. Evaluate some algorithms

# Separate out a validation dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Set up models
models = {
    'Logistic Regression': LogisticRegression(max_iter=200),
    'Linear Discriminant Analysis': LinearDiscriminantAnalysis(),
    'K-Nearest Neighbors': KNeighborsClassifier(),
    'Decision Tree': DecisionTreeClassifier(),
    'Gaussian Naive Bayes': GaussianNB(),
    'Support Vector Machine': SVC()
}

# Cross-validation and evaluation
results = {}
for name, model in models.items():
    # 10-fold cross-validation
    cv_scores = cross_val_score(model, X_train, y_train, cv=10)
    results[name] = {
        'Mean Accuracy': np.mean(cv_scores),
        'Standard Deviation': np.std(cv_scores)
    }

# Print results
print("\nAlgorithm Performance:")
for name, metrics in results.items():
    print(f"{name}: Mean Accuracy = {metrics['Mean Accuracy']:.3f}, Std Dev = {metrics['Standard Deviation']:.3f}")

# 6. Making some predictions

# Fit all models and make predictions on the test set
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\n{name} Test Accuracy: {accuracy:.3f}")
