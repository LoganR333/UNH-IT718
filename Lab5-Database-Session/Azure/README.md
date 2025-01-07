# Azure: Database Session												
1.	Review package elements (sample code provided).
2.	Deploy a function that maintains session state.
3.	Validate execution.

*Note: functionapp names must be globally unique.  Thus you will need to replace "session-uuid" in the commands below, as well as renaming the "code/session-uuid" folder.*

### Set up your environment:
```
ACCOUNT=it718lab4
RESOURCE_GROUP=it718lab4
REGION=eastus
APP_NAME=session-uuid
```
###  Recreate (if needed) resource group and storage account from Lab4
```
az group create --name $RESOURCE_GROUP --location $REGION
az storage account create --name "$ACCOUNT" --resource-group $RESOURCE_GROUP \
    --location $REGION --sku Standard_LRS
```
### Create Table storage
```
az storage table create \
    --name sessionuuid \
    --account-name $ACCOUNT
```
### Set environment value
```
TABLE_CONNECT=`az storage account show-connection-string \
    --name $ACCOUNT \
    --resource-group $RESOURCE_GROUP \
    --query connectionString \
    --output tsv`
az functionapp config appsettings set \
    --name $APP_NAME \
    --resource-group $RESOURCE_GROUP \
    --settings "AzureWebJobsStorage=$TABLE_CONNECT"
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
```

```
```
### Create functionzip
```
cd code
zip -r functionapp.zip .
```
### Deploy the code
```
az functionapp deployment source config-zip \
    --resource-group $RESOURCE_GROUP \
    --name $APP_NAME \
    --src functionapp.zip
```
# Lab report

*Note: The function needs to remain available until the lab is graded.*

The functionapp URL is https://<your-function-name>.azurewebsitea.net/api/<your-function-name>?

Show screenshots of using wget from the cloud sheel and a browser fetch.
![cloudshell](Lab4-Azure-cli.png)
![browser](Lab4-Azure-browser.png)

