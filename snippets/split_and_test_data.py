# Features I kept after looking at the correlation matrix
X = new_mgh[['age', 'prevalentHyp', 'sysBP', 'diaBP', 'glucose']]
y = new_mgh['TenYearCHD']

# Split into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
