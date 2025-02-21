# Cloud Resume
## Requirements
1. Frontend for a static Website
  - HTML/CSS and Javascript
  - Hosting on Amazon S3 as a static website
  - CloudFront for global CDN caching
  - Enable HTTPS with an SSL certificate via AWS Certificate Manager(ACM)
  - Adding a custom domain using Route 53(optional)

2. Backend(Serveless API)
  - AWS Lambda(Python/Nodejs) to count website visitors
  - DynamoDB to store visitor count
  - An API Gateway endpoint for the frontend to call
  - Secure API access using IAM roles and CORS

3. Infrastructure as Code
 - Terraform or AWS CloudFormation to define and deploy resources

4. CI/CD Pipeline- to automate deployments with Github Actions 
- Automatically update the site when changes are pushed to Github


## Steps
1. Build a simple resume page using HTML/CSS and Javascript or use an existing one if you have one
2. Log into AWS management console,search for S3 bucket and enable static website hosting,upload your HTML,CSS and JS files and set public read access for the bucket(or use CloudFront for security)
3. Enable CloudFront for fast and secure delivery,set up an Amazon CloudFront distribution with your S3 bucket as the origin
4. Enable HTTPS(SSL certificate via AWS Certificate Manager) and update S3 bucket policy to restrict direct access(only allow CloudFront)
5. Use Route 53 for a custom domain(optional as you need to purchase and register a domain in Route 53 )

## Create a Backend API for visitor count
- The website should display the number of visitors using an API Gateway + Lambda + DynamoDB setup

1. Create a DynamoDB table,table name:Visitor count,Partition key:id(set value to '1')for a single record,Attribute:count(stores the visitor count)
2. Create a Lambda Function(I have a file called main.py)
3. Use AWS Management Console or Terraform/CDK to deploy
4. Create an API Gateway point
  - Set up an API Gateway HTTP API to trigger the Lambda function
  - Enable CORS to allow JavaScript to fetch data from your website.
5. Connect API to the Frontend


