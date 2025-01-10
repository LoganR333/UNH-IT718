# AWS: Github Actions

### Set environment
```
SERVICE_ACCOUNT_NAME=YOUR_ACCOUNT
PROJECCT_ID=YOUR_PROJECT
KEY_FILE_NAME=YOUR_KEY_FILE
```


### Store Secrets:
Add the following secrets to your GitHub repository
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_REGION
- AWS_BUCKET_NAME

### Create a basic index.html
> [!WARNING]
> I will edited this file during grading

### Deploy repo workflow
Replace the YOUR_BUCKET_NAME in `gcp.yaml`, then copy the result to `.github/workflows/gcp.yaml`

### If successful
You will see under the actios tab a workflow run.
Your storage based website will show your index.html edits.

