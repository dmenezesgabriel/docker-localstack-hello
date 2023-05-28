# Building a Simple Vue.js TODO Web App with AWS Serverless Architecture

In this tutorial, we will walk through the process of creating a simple TODO web app using Vue.js, composition API, and Vite. We will also cover how to host the app on an AWS serverless architecture, which includes S3, API Gateway, Lambda Functions, DynamoDB, and CloudWatch Logs.

Prerequisites:

- Basic knowledge of Vue.js and JavaScript
- Docker installed on your local machine

Let's begin!

## Step 1: Setting Up the Development Environment

1. Install Vue CLI:

   ```sh
   npm install -g @vue/cli
   ```

2. Create a new Vue project:

   ```sh
   vue create vue-todo-app
   ```

   Choose the default preset or customize it according to your preferences.

3. Change into the project directory:

   ```sh
   cd vue-todo-app
   ```

4. Install Vite:

   ```sh
   npm install --save-dev vite
   ```

## Step 2: Implementing the TODO App

1. Create a new file called App.vue in the src directory and replace its content with the following code:

   ```vue
   <template>
     <div>
       <h1>TODO App</h1>
       <input v-model="newTask" placeholder="Enter a task" />
       <button @click="addTask">Add</button>
       <ul>
         <li v-for="task in tasks" :key="task.id">
           {{ task.name }}
           <button @click="deleteTask(task.id)">Delete</button>
         </li>
       </ul>
     </div>
   </template>

   <script>
   import { ref } from "vue";

   export default {
     setup() {
       const tasks = ref([]);
       const newTask = ref("");

       const addTask = () => {
         const task = {
           id: Date.now(),
           name: newTask.value,
         };
         tasks.value.push(task);
         newTask.value = "";
       };

       const deleteTask = (taskId) => {
         tasks.value = tasks.value.filter((task) => task.id !== taskId);
       };

       return {
         tasks,
         newTask,
         addTask,
         deleteTask,
       };
     },
   };
   </script>
   ```

2. Open main.js in the src directory and replace its content with the following code:

   ```js
   import { createApp } from "vue";
   import App from "./App.vue";

   createApp(App).mount("#app");
   ```

## Step 3: Testing the App Locally

1. Start the development server:

   ```sh
   npm run dev
   ```

2. Open your browser and visit http://localhost:3000 to see the TODO app in action. You should be able to add and delete tasks.

## Step 4: Setting Up AWS Serverless Architecture with LocalStack

1. Install LocalStack using Docker:

   ```sh
   docker pull localstack/localstack
   ```

2. Run LocalStack with the required services:

   ```sh
   docker run -d --name localstack -p 4566:4566 -e SERVICES=s3,apigateway,lambda,dynamodb,logs localstack/localstack

   ```

3. Install the AWS CLI:

   ```sh
   pip install awscli
   ```

4. Configure the AWS CLI to use LocalStack:

```sh
aws configure
```

Set the Access Key ID and Secret Access Key to any values (they won't be used with LocalStack). Set the Default region name to us-east-1 and Default output format to json.

## Step 5: Provisioning AWS Resources

1. Create an S3 bucket:

   ```sh
   awslocal --endpoint-url=http://localhost:4566 s3 mb s3://todo-app-bucket
   ```

2. Create a DynamoDB table:

   ```sh
   awslocal --endpoint-url=http://localhost:4566 dynamodb create-table --table-name todo-app-tasks --attribute-definitions AttributeName=id,AttributeType=N --key-schema AttributeName=id,KeyType=HASH --billing-mode PAY_PER_REQUEST

   ```

3. Verify if the table was created:

   ```sh
   awslocal --endpoint-url=http://localhost:4566 dynamodb list-tables --profile localstack
   ```

4. Create an IAM role for the Lambda function:

   ```sh
   awslocal --endpoint-url=http://localhost:4566 iam create-role --role-name lambda-execution-role --assume-role-policy-document '{"Version": "2012-10-17","Statement": [{"Effect": "Allow","Principal": {"Service": "lambda.amazonaws.com"},"Action": "sts:AssumeRole"}]}'

   ```

5. Attach the necessary policies to the IAM role:

   ```sh
   awslocal --endpoint-url=http://localhost:4566 iam attach-role-policy --role-name lambda-execution-role --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole

   awslocal --endpoint-url=http://localhost:4566 iam attach-role-policy --role-name lambda-execution-role --policy-arn arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess

   ```

   _arn refers to Amazon Resource Name_

## Step 6: Implementing the Lambda Function

1. Create a new directory called lambda in the project root.
2. Change into the lambda directory and create a file called index.js with the following code:

   ```js
   const AWS = require("aws-sdk");

   const dynamoDB = new AWS.DynamoDB({ endpoint: "http://localhost:4566" });

   exports.handler = async (event) => {
     if (event.httpMethod === "GET") {
       const tasks = await dynamoDB.scan({ TableName: "todo-app-tasks" }).promise();
       return {
         statusCode: 200,
         body: JSON.stringify(tasks.Items),
       };
     }

     if (event.httpMethod === "POST") {
       const task = JSON.parse(event.body);
       await dynamoDB
         .putItem({
           TableName: "todo-app-tasks",
           Item: {
             id: { N: task.id.toString() },
             name: { S: task.name },
           },
         })
         .promise();
       return {
         statusCode: 200,
         body: JSON.stringify({ message: "Task added successfully" }),
       };
     }

     if (event.httpMethod === "DELETE") {
       const taskId = event.pathParameters.id;
       await dynamoDB
         .deleteItem({
           TableName: "todo-app-tasks",
           Key: {
             id: { N: taskId },
           },
         })
         .promise();
       return {
         statusCode: 200,
         body: JSON.stringify({ message: "Task deleted successfully" }),
       };
     }

     return {
       statusCode: 400,
       body: JSON.stringify({ message: "Invalid HTTP method" }),
     };
   };
   ```

3. Zip the lambda directory:

   ```sh
   zip -r lambda.zip .
   ```

   _In Windows use GUI or instal MSYS2 to use zip command with `pacman -S zip`_

4. Create the Lambda function:

   ```sh
   awslocal --endpoint-url=http://localhost:4566 lambda create-function --function-name todo-app-lambda --runtime nodejs14.x --handler index.handler --role arn:aws:iam::000000000000:role/lambda-execution-role --zip-file fileb://lambda.zip

   ```

   _got IAM ARN from command output in 5.3 item of this tutorial._

   Check if it is working:

   ```sh
   awslocal lambda invoke --function-name <function-name> --payload '{}' output.json
   ```

   example output:

   ```json
   {
     "StatusCode": 200,
     "ExecutedVersion": "$LATEST"
   }
   ```

## Step 7: Creating API Gateway

1. Create an API Gateway REST API:

   ```sh
   awslocal --endpoint-url=http://localhost:4566 apigateway create-rest-api --name todo-app-api
   ```

2. Retrieve the API Gateway REST API ID:

   ```sh
   awslocal --endpoint-url=http://localhost:4566 apigateway get-rest-apis
   ```

   _Note down the value of the id field._

   example output:

   ```json
   {
     "id": "aqnnns34m4",
     "name": "todo-app-api",
     "createdDate": 1685232928.0,
     "apiKeySource": "HEADER",
     "endpointConfiguration": {
       "types": ["EDGE"]
     },
     "disableExecuteApiEndpoint": false
   }
   ```

3. Create new API Gateway resources:

   **Get existing resources**:

   ```sh
   awslocal --endpoint-url=http://localhost:4566 apigateway get-resources --rest-api-id <api-id>
   ```

   _Example: `awslocal --endpoint-url=http://localhost:4566 apigateway get-resources --rest-api-id aqnnns34m4`_

   Example output:

   ```json
   {
     "items": [
       {
         "id": "3g6gi11nnl",
         "path": "/"
       }
     ]
   }
   ```

   **Create new resources**:

   ```sh
   awslocal --endpoint-url=http://localhost:4566 apigateway create-resource --rest-api-id <api-id> --parent-id <root-resource-id> --path-part todos
   ```

   Replace <api-id> with the REST API ID obtained from the previous step and <root-resource-id> with the id of the root resource (usually /').

   _Example: `awslocal --endpoint-url=http://localhost:4566 apigateway create-resource --rest-api-id aqnnns34m4 --parent-id 3g6gi11nnl --path-part todos`_

   example output:

   ```json
   {
     "id": "sls1wpqox9",
     "parentId": "3g6gi11nnl",
     "pathPart": "todos",
     "path": "/todos"
   }
   ```

   Replace <api-id> with the REST API ID obtained from the previous step and <root-resource-id> with the id of the root resource (usually /').

4. Create a new GET method for the /todos resource:

   ```sh
   awslocal --endpoint-url=http://localhost:4566 apigateway put-method --rest-api-id <api-id> --resource-id <todos-resource-id> --http-method GET --authorization-type NONE
   ```

   Replace <api-id> with the REST API ID and <todos-resource-id> with the id of the /todos resource obtained from the previous step.

   _Example: `awslocal --endpoint-url=http://localhost:4566 apigateway put-method --rest-api-id aqnnns34m4 --resource-id sls1wpqox9 --http-method GET --authorization-type NONE`_

   example output:

   ```json
   {
     "type": "AWS_PROXY",
     "httpMethod": "GET",
     "uri": "arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:000000000000:function:todo-app-lambda/invocations",
     "requestParameters": {},
     "cacheNamespace": "sls1wpqox9",
     "cacheKeyParameters": []
   }
   ```

5. Create a new POST method for the /todos resource:

   ```sh
   awslocal --endpoint-url=http://localhost:4566 apigateway put-method --rest-api-id <api-id> --resource-id <todos-resource-id> --http-method POST --authorization-type NONE
   ```

   Replace <api-id> with the REST API ID and <todos-resource-id> with the id of the /todos resource obtained from the previous step.

   _Example: `awslocal --endpoint-url=http://localhost:4566 apigateway put-method --rest-api-id aqnnns34m4 --resource-id sls1wpqox9 --http-method POST --authorization-type NONE`_

   example output:

   ```json
   {
     "httpMethod": "POST",
     "authorizationType": "NONE",
     "apiKeyRequired": false
   }
   ```

6. Create a new lambda integration for the GET method:

   ```sh
   awslocal --endpoint-url=http://localhost:4566 apigateway put-integration --rest-api-id aqnnns34m4 --resource-id sls1wpqox9 --http-method GET --type AWS_PROXY --integration-http-method GET --uri arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:000000000000:function:todo-app-lambda/invocations

   ```

7. Create a new Lambda integration for the POST method:

   Retrieve you account id use the command below:

   ```sh
   awslocal sts get-caller-identity --query "Account" --output text
   ```

   Check created lambdas with the command below:

   ```sh
   awslocal lambda list-functions --query 'Functions[*].FunctionName' --output text
   ```

   Get lambda region and path:

   ```sh
    awslocal lambda get-function --function-name <function-name> --query 'Configuration.[FunctionArn, Runtime]'
   ```

   example output:

   ```json
   ["arn:aws:lambda:us-east-1:000000000000:function:todo-app-lambda", "nodejs14.x"]
   ```

   ```sh
   awslocal --endpoint-url=http://localhost:4566 apigateway put-integration --rest-api-id <api-id> --resource-id <todos-resource-id> --http-method POST --type AWS_PROXY --integration-http-method POST --uri arn:aws:apigateway:<region>:lambda:path/2015-03-31/functions/arn:aws:lambda:<region>:<account-id>:function:todo-app-lambda/invocations
   ```

   Replace <api-id> with the REST API ID and <todos-resource-id> with the id of the /todos resource obtained from the previous steps.

   _Example code: `awslocal --endpoint-url=http://localhost:4566 apigateway put-integration --rest-api-id aqnnns34m4 --resource-id sls1wpqox9 --http-method POST --type AWS_PROXY --integration-http-method POST --uri arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:000000000000:function:todo-app-lambda/invocations`_

   ```json
   {
     "type": "AWS_PROXY",
     "httpMethod": "POST",
     "uri": "arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:000000000000:function:todo-app-lambda/invocations",
     "requestParameters": {},
     "cacheNamespace": "sls1wpqox9",
     "cacheKeyParameters": []
   }
   ```

8. Deploy the API Gateway API:

   ```sh
   awslocal --endpoint-url=http://localhost:4566 apigateway create-deployment --rest-api-id <api-id> --stage-name dev
   ```

   Replace <api-id> with the REST API ID obtained from previous steps.

   example output:

   ```json
   {
     "id": "oxy64561ga",
     "createdDate": 1685241182.0
   }
   ```

   ```sh
   http://localhost:4566/restapis/aqnnns34m4/dev/_user_request_/todos
   ```

   [Troubeshooting](https://docs.aws.amazon.com/pt_br/apigateway/latest/developerguide/http-api-troubleshooting-lambda.html)

## Step 8: Connecting the Vue App to the Serverless Backend

1. Open App.vue in the src directory and replace the existing <script> section with the following code:

   ```vue
   <script>
   import { ref, onMounted } from "vue";
   import axios from "axios";

   export default {
     setup() {
       const tasks = ref([]);
       const newTask = ref("");

       const apiId = "<api-id>"; // Replace with your actual REST API ID
       const stage = "dev"; // Replace with your actual stage name

       const apiEndpoint = `http://localhost:4566/restapis/${apiId}/${stage}/_user_request_`;

       const addTask = async () => {
         const task = {
           id: Date.now(),
           name: newTask.value,
         };
         await axios.post(`${apiEndpoint}/todos`, task);
         tasks.value.push(task);
         newTask.value = "";
       };

       const deleteTask = async (taskId) => {
         await axios.delete(`${apiEndpoint}/todos/${taskId}`);
         tasks.value = tasks.value.filter((task) => task.id !== taskId);
       };

       onMounted(async () => {
         const response = await axios.get(`${apiEndpoint}/todos`);
         tasks.value = response.data;
       });

       return {
         tasks,
         newTask,
         addTask,
         deleteTask,
       };
     },
   };
   </script>
   ```

   Replace <api-id> with the REST API ID obtained in Step 7.

## Step 9: Hosting the App on AWS S3

1. Build the Vue app:

   ```sh
   npm run build
   ```

2. Upload the contents of the dist directory to the S3 bucket:

   ```sh
   awslocal --endpoint-url=http://localhost:4566 s3 cp dist s3://todo-app-bucket/ --recursive
   ```

3. Set the bucket's website configuration using the put-bucket-website command:

   ```sh
   awslocal --endpoint-url=http://localhost:4566 s3api put-bucket-website --bucket todo-app-bucket --website-configuration '{
     "IndexDocument": {"Suffix": "index.html"},
     "ErrorDocument": {"Key": "error.html"}
   }'

   ```

4. Retrieve the S3 bucket website URL:

   ```sh
   awslocal --endpoint-url=http://localhost:4566 s3api get-bucket-website --bucket todo-app-bucket
   ```

   example output:

   ```json
   {
     "IndexDocument": {
       "Suffix": "index.html"
     },
     "ErrorDocument": {
       "Key": "error.html"
     }
   }
   ```

## Step 10: Testing the Deployed App

1. Open your browser and visit the S3 bucket website URL `https://todo-app-bucket.s3-website.localhost.localstack.cloud:4566/` You should see the deployed TODO app.

Congratulations! You have successfully created a simple TODO web app using Vue.js, composition API, and Vite. The app is hosted on an AWS serverless architecture, utilizing S3, API Gateway, Lambda Functions, DynamoDB, and CloudWatch Logs.
