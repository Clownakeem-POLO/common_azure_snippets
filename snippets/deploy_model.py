import datetime

# Build the environment the service will run in
env = Environment(name="mgh-model-env")
conda_dep = CondaDependencies()
conda_dep.add_conda_package("pandas")
conda_dep.add_conda_package("numpy")
conda_dep.add_conda_package("scikit-learn")
conda_dep.add_conda_package("joblib")
conda_dep.add_pip_package("azureml-core")
env.python.conda_dependencies = conda_dep

# Inference config points at the scoring script
inference_config = InferenceConfig(
    environment=env,
    source_directory=".",
    entry_script="score.py"
)

# Deploy to Azure Container Instances
deployment_config = AciWebservice.deploy_configuration(
    cpu_cores=1,
    memory_gb=1,
    auth_enabled=True,
    enable_app_insights=True,
    description="MGH health prediction service"
)

# Service names must be lowercase, no underscores, max 32 chars, start with a letter.
# A timestamp keeps the name unique between redeploys.
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M")
service_name = f"mgh-pred-{timestamp}"
if len(service_name) > 32:
    service_name = f"mgh-pred-{timestamp[-8:]}"

print(f"Using service name: {service_name}")
print(f"Deploying model: {model}")

service = Model.deploy(
    workspace=ws,
    name=service_name,
    models=[model],
    inference_config=inference_config,
    deployment_config=deployment_config,
    overwrite=True
)

service.wait_for_deployment(show_output=True)
print(f"Deployment state: {service.state}")
print(f"Service URL: {service.scoring_uri}")
