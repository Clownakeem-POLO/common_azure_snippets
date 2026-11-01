# Azure ML deployment snippets

This is my working reference for taking a model from a raw dataset all the way to a live
prediction endpoint on Azure Machine Learning. I put it together while deploying a heart-disease
classifier (the Massachusetts General Hospital / Framingham dataset, predicting `TenYearCHD`), but
the steps are the same for most tabular models, so I keep it around as a cheat sheet.

Each file in `snippets/` is one step. They are meant to be read and run in order, not imported as a
package. The `score.py` file is the exception: it is the actual scoring script Azure runs inside the
deployed service.

## The workflow, in order

1. **Import the libraries** - `snippets/libraries.py`
2. **Import the Azure SDK pieces** - `snippets/azure_sdk.py`
3. **Connect to the workspace** - `snippets/workspace_connection.py`
4. **Load and clean the data** - done inline per dataset; the cleaned frame here is `new_mgh`
5. **Correlation matrix** to pick the features worth keeping - `snippets/correlation_matrix.py`
6. **Split into train and test sets** - `snippets/split_and_test_data.py`
7. **Train and compare models**, keep the best one - `snippets/model_pipeline.py`
8. **Save the model** to the outputs folder - `snippets/save_model.py`
9. **Register the model** in the workspace - `snippets/register_model.py`
10. **Write the scoring script** the service will run - `snippets/score.py`
11. **Deploy** to Azure Container Instances - `snippets/deploy_model.py`
12. **Test** the live endpoint with a sample request - `snippets/verify_prediction.py`

## Notes

- Step 4 (load and clean) is left out on purpose, it changes with every dataset. Everything
  downstream assumes a cleaned dataframe called `new_mgh`.
- The deployment uses ACI, which is fine for testing and demos. For anything production-facing you
  would move to AKS.
- No credentials live in these files. The service key is fetched at runtime with
  `service.get_keys()`, and the sample request uses dummy values.
