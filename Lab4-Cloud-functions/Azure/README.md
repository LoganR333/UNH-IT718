# Azure												
1.	Review package elements (sample code provided).
2.	Deploy the function.
3.	Validate execution.
4.	
*Note: The function needs to remain available until the lab is graded.*

### Set up your environment:
```
ACCOUNT=it718lab4
RESOURCE_GROUP=it718lab4
REGION=eastus
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
    --name get-uuid \
    --storage-account $ACCOUNT  --os-type Linux
```
Add Function Code: Save the following code as __init__.py:
import logging

```
az functionapp deployment source config-zip \
    --resource-group YOUR_RESOURCE_GROUP \
    --name hello-world-webpage \
    --src function.zip
```
### Get the URL: Use the following command to retrieve the function’s URL:
```
az functionapp show --name hello-world-webpage --resource-group YOUR_RESOURCE_GROUP --query defaultHostName
```
