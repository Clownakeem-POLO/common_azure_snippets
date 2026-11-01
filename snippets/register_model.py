model = Model.register(
    workspace=ws,
    model_path=model_filename,
    model_name="mgh_health_model",
    description="Predicting a patient's chance of TenYearCHD (Massachusetts General Hospital dataset)",
    tags={"data_source": "mghdataset.csv", "model_type": best_model_name}
)
print(f"Model registered: {model.name}, version: {model.version}")
