# Azure: Cloud Functions												
1.	Review package elements (sample code provided).
2.	Deploy the function.
3.	Validate execution.

> [!NOTE]
> functionapp names must be globally unique.  

### Set up your environment:
```
ACCOUNT=it718lab4
RESOURCE_GROUP=it718lab4
REGION=eastus
APP_NAME=return-uuid
```
### Create a resource group
```
az group create --name $RESOURCE_GROUP --location $REGION
```
### Create a storage account
```
az storage account create \
    --name "$ACCOUNT" \
    --resource-group $RESOURCE_GROUP \
    --location $REGION \
    --sku Standard_LRS
```
### Create cloud function
```
az functionapp create \
    --resource-group $RESOURCE_GROUP \
    --consumption-plan-location $REGION \
    --runtime python \
    --runtime-version 3.11 \
    --functions-version 4 \
    --name $APP_NAME \
    --storage-account $ACCOUNT  --os-type Linux
az functionapp cors add \
    --name $APP_NAME \
    --resource-group $RESOURCE_GROUP \
    --allowed-origins "*"
```
### Create functionzip
```
cd <code-folder>  # i.e. ~/UNH71.../Azure/code
zip -r functionapp.zip .
```
### Deploy the code
```
az functionapp deployment source config-zip \
    --resource-group $RESOURCE_GROUP \
    --name $APP_NAME \
    --src functionapp.zip
```
## Lab report

> [!NOTE]
> The function needs to remain available until the lab is graded.

The functionapp URL is https://**your-app-name**.azurewebsites.net/api/return-uuid

Show screenshots of using wget from the cloud shell and a browser fetch.  
![cloudshell](Lab4-Azure-cli.png)
![browser](Lab4-Azure-browser.png)

