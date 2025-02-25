from azureml.core import Workspace, Model
from azureml.core.webservice import AciWebservice
from azureml.core.model import InferenceConfig
from azureml.core.environment import Environment
from azureml.core.conda_dependencies import CondaDependencies

# Load workspace
ws = Workspace.from_config()

# Register the model
model = Model.register(workspace=ws, model_path="diabetes_model.pkl", model_name="diabetes_model")

# Create environment
env = Environment(name="diabetes-env")
conda_dep = CondaDependencies()
conda_dep.add_conda_package("scikit-learn")
conda_dep.add_conda_package("joblib")
env.python.conda_dependencies = conda_dep

# Define inference config
inference_config = InferenceConfig(entry_script="score.py", environment=env)

# Deploy to ACI (Azure Container Instance)
deployment_config = AciWebservice.deploy_configuration(cpu_cores=1, memory_gb=1)
service = Model.deploy(ws, "diabetes-service", [model], inference_config, deployment_config)
service.wait_for_deployment(show_output=True)
print(f"Service deployed at: {service.scoring_uri}")