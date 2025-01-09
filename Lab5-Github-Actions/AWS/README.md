# AWS: Github Actions

### Set environment
```
SERVICE_ACCOUNT_NAME=it718lab5
PROJECCT_ID=unh-it718
KEY_FILE_NAME=service_key
```
### Create service account
```
gcloud iam service-accounts create $SERVICE_ACCOUNT_NAME \
    --description="Service account for Cloud Storage admin tasks" \
    --display-name="Cloud Storage Admin Service Account"
```
### Grant role for access to Cloud Storage
```
gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:$SERVICE_ACCOUNT_NAME@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/storage.admin"
```
### Generate Key
It is the base64 output you add to Github
```
gcloud iam service-accounts keys create $KEY_FILE_NAME.json \
    --iam-account=$SERVICE_ACCOUNT_NAME@$PROJECT_ID.iam.gserviceaccount.com
base64 $KEY_FILE_NAME
```

### Store Secrets:
Add the following secrets to your GitHub repository
- GCP_PROJECT_ID
- GCP_SERVICE_ACCOUNT_KEY (base64).

### Create a basic index.html
> [!WARNING]
> I will edited this file during grading

### Deploy repo workflow
Replace the YOUR_BUCKET_NAME in `gcp.yaml`, then copy the result to `.github/workflows/gcp.yaml`

### If successful
You will see under the actios tab a workflow run.
Your storage based website will show your index.html edits.

