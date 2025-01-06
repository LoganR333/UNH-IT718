# Azure												
1.	Review package elements (sample code provided).
2.	Deploy the function.
3.	Validate execution.
*Note:* The function needs to remain available until the lab is graded.

```
az functionapp create \
    --resource-group YOUR_RESOURCE_GROUP \
    --consumption-plan-location westus \
    --runtime python \
    --runtime-version 3.9 \
    --functions-version 4 \
    --name hello-world-webpage \
    --storage-account YOUR_STORAGE_ACCOUNT
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
