# Save the best model to the outputs folder so it can be registered
os.makedirs('./outputs', exist_ok=True)
model_filename = './outputs/mgh_best_model.pkl'
joblib.dump(best_model, model_filename)
