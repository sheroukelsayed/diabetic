from azure.identity import DefaultAzureCredential
from azure.mgmt.web import WebSiteManagementClient
from azure.mgmt.web.models import (AppServicePlan, SkuDescription, Site, SiteConfig)

# Authenticate with Azure using the default credentials (this works if you're already logged in)
credential = DefaultAzureCredential()

# Specify your Azure subscription ID
subscription_id = 'Azure subscription 1'

# Initialize the client
web_client = WebSiteManagementClient(credential, subscription_id)



# Define your resource group, plan, and app name
resource_group_name = 'Medical'
location = 'West US 2'
app_service_plan_name = 'MyAppServicePlan'
app_name = 'MedicalApp'  # Must be globally unique


# Create the App Service Plan
app_service_plan = web_client.app_service_plans.begin_create_or_update(
    resource_group_name,
    app_service_plan_name,
    AppServicePlan(
        location=location,
        sku=SkuDescription(name='B1', capacity=1, tier='Basic'),
        reserved=True  # This specifies Linux hosting
    )
).result()

# Create the Web App
site_config = SiteConfig(
    linux_fx_version='PYTHON|3.11',  # Set Python version
    app_settings=[{'name': 'WEBSITE_RUN_FROM_PACKAGE', 'value': '1'}]
)

web_app = web_client.web_apps.begin_create_or_update(
    resource_group_name,
    app_name,
    Site(
        location=location,
        server_farm_id=app_service_plan.id,
        site_config=site_config
    )
).result()

print(f"Web App created at: https://{app_name}.azurewebsites.net")
