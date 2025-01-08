# GCP										
1.	Review package elements (sample code provided).
2.	Deploy the function.
3.	Validate execution.


gcloud functions deploy hello-world-webpage \
    --runtime python39 \
    --trigger-http \
    --allow-unauthenticated \
    --entry-point hello_world \
    --region us-central1

## Lab report
> [!NOTE]
> The function needs to remain available until the lab is graded.

The URL is https://REGION-PROJECT_ID.cloudfunctions.net/hello-world-webpage  

Show screenshots of using wget from the cloud shell and a browser fetch.  
![cloudshell](Lab4-GCP-cli.png)
![browser](Lab4-GCP-browser.png)
