import json
from azure.identity import DefaultAzureCredential
from azure.mgmt.web import WebSiteManagementClient
from azure.mgmt.web.models import (
    SkuDescription,
    AppServicePlan,
    Site,
)

# Load configuration from a JSON file
with open("config.json", 'r') as file:
    data = json.load(file)

subscription_id = data["subscription_id"]
resource_group = data["resource_group"]
app_service_plan_name = data["app_service_plan"]
web_app_name = data["web_app_name"]
region = data["region"]

# Authenticate with Azure using DefaultAzureCredential
credential = DefaultAzureCredential()

# Initialize the WebSite Management Client
web_client = WebSiteManagementClient(credential, subscription_id)

# Create an App Service Plan
app_service_plan = AppServicePlan(
    location=region,
    sku=SkuDescription(
        name="S1",  # Change this to your desired SKU (e.g., B1, S1)
        tier="Standard",
        size="S1",
        family="S",
        capacity=1
    )
)

# Create the App Service Plan
web_client.app_service_plans.begin_create_or_update(
    resource_group_name=resource_group,
    name=app_service_plan_name,
    app_service_plan=app_service_plan  # Pass the app_service_plan object here
).result()  # Wait for the operation to complete

print(f"App Service Plan '{app_service_plan_name}' created successfully.")

# Create a Web App
web_app = Site(
    location=region,
    server_farm_id=app_service_plan_name,
    site_config={
        "app_settings": [
            {"name": "WEBSITE_NODE_DEFAULT_VERSION", "value": "14"},  # Adjust for your app
        ]
    }
)

# Create the Web App
web_client.web_apps.begin_create_or_update(
    resource_group_name=resource_group,
    name=web_app_name,
    site_envelope=web_app
).result()  # Wait for the operation to complete

print(f"Web App '{web_app_name}' created successfully.")


# Create the Web App
web_client.web_apps.begin_create_or_update(
    resource_group_name=resource_group,
    name=web_app_name,
    site_envelope=web_app
).result()  # Wait for the operation to complete

print(f"Web App '{web_app_name}' created successfully.")
