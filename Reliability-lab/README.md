# AWS Reliability lab

[AWS Workshop source](https://catalog.workshops.aws/well-architected-reliability/en-US)

### Deploy using CloudShell  (Ohio)
From class lab clone
```
cd UNH-IT718/Reliability-lab
sh deploy.sh
```

This will take 4-5 minutes for each of the stacks to be created.

### Review Questions
- Does the order the stacks are created matter?
- What methods can be used to provide parameters to stack?
- What would it take to make the deployment multi-regional?
- What happens if one of EC2 servers dies?
- Does the deployment allow for scaling up based on demand?
- How can you change the OS used by the web app?
- Would this be a good application for use of spot instances?
  
> [!IMPORTANT]
> CLEAN UP
> Goto AWS Console: CloudFormation and delete the HealthCheckLab and WebApp1-VPC stacks
