# AWS CLOUD RESUME
- This project showcases hands on experience with cloud technologies in this case AWS,it involves building a web-based resume hosted on cloud with practical skills in cloud computing,serveless architecture,and DevOps practices.

## Key components
- HTML/CSS
- Responsiv Design:ensures the resume is mobile-friendly and works well on various devices
- DNS
  - Amazon Route 53-to point the domain to the S3 website
  - Custom domain(not a must though)
- DynamoDB: servers as a Database and stores visitor counter data in an AWS DynamoDB table
- A certification either the AWS Cloud Practitioner or AWS-Certified-Solutions-Architect
- A Static website,the HTML resume will be deployed online
- Amazon CloudFront:the S3 Website will utilize HTTPS for security purposes
- API-AWS API Gateway:using REST API the website can call and get an update of the visitor count
- Lambda Functions:use AWS Lambda to handle requests to your API and interact with DynamoDB
- Infrastructure as Code (IaC)
   - AWS CloudFormation:define your infrastructure using CloudFormation templates
   - IaC Tools:tools like AWS CDK or Terraform for infrastructure management
   - AWS SAM CLI
- Source control
- CI/CD Pipeline
   - Github Actions:to implement continuous intergration and deployment pipelines using Github Actions
   - Automated Testing:set up tests to run autmatically when you push changes
- Python
- Javascript
 