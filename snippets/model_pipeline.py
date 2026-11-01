# Train a few models and keep whichever does best on the test set
models = {
    'Random Forest': RandomForestClassifier(random_state=42),
    'Gradient Boosting': GradientBoostingClassifier(random_state=42),
    'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000)
}

results = {}

for name, model in models.items():
    # Wrap each model in a pipeline so the step is easy to extend later
    pp = Pipeline(steps=[
        ('classifier', model)
    ])

    print(f"Training {name}...")
    pp.fit(X_train, y_train)

    train_score = pp.score(X_train, y_train)
    test_score = pp.score(X_test, y_test)

    y_pred = pp.predict(X_test)
    report = classification_report(y_test, y_pred)

    results[name] = {
        'pipeline': pp,
        'train_score': train_score,
        'test_score': test_score,
        'classification_report': report
    }

    print(f"{name} - Training accuracy: {train_score:.4f}, Testing accuracy: {test_score:.4f}")
    print("Classification Report:")
    print(report)
    print("-" * 50)

# Pick the best performing model by test accuracy
best_model_name = max(results, key=lambda k: results[k]['test_score'])
best_model = results[best_model_name]['pipeline']
best_score = results[best_model_name]['test_score']
