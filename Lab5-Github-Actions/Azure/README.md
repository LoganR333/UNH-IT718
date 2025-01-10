# Azure: Github Actions

### Set environment
```
ACCOUNT=YOUR_ACCOUNT
RESOURCE_GROUP=YOUR_RESOURCE_GROUP
```

### Retrieve Storage Key
```
az storage account keys list --resource-group $RESOURCE_GROUP --account-name $ACCOUNT
```

### Store Secrets:
Add the following secrets to your GitHub repository
- AZURE_CLIENT_ID
- AZURE_CLIENT_SECRET
- AZURE_STORAGE_ACCOUNT
- AZURE_STORAGE_KEY
- AZURE_CONTAINER_NAME 

### Create a basic index.html
> [!WARNING]
> I will edited this file during grading

### Deploy repo workflow
Replace any customizations in `azure.yaml`, then copy the result to `.github/workflows/azure.yaml`

### If successful
You will see under the actions tab a workflow run.
Your storage based website will show your index.html edits.

