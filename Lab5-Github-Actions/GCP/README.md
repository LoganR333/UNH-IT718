# GCP

SERVICE_ACCOUNT_NAME=it718lab5
PROJECCT_ID=unh-it718
KEY_FILE_NAME=service_key

gcloud iam service-accounts create $SERVICE_ACCOUNT_NAME \
    --description="Service account for Cloud Storage admin tasks" \
    --display-name="Cloud Storage Admin Service Account"
### Grant role
gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:$SERVICE_ACCOUNT_NAME@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/storage.admin"

### Generate Key
gcloud iam service-accounts keys create $KEY_FILE_NAME.json \
    --iam-account=$SERVICE_ACCOUNT_NAME@$PROJECT_ID.iam.gserviceaccount.com


### Create service account

### Store Secrets:
Add the following secrets to your GitHub repository
- GCP_PROJECT_ID
- GCP_SERVICE_ACCOUNT_KEY (Base64-encoded service account key JSON file).

Edit the YOUR_BUCKET_NAME in gcp.yaml, then copy the file to .github/workflows/gcp.yaml
