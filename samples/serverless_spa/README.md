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
   aws --endpoint-url=http://localhost:4566 s3api create-bucket --bucket-name todo-app-bucket
   ```

2. Create a DynamoDB table:

   ```sh
   aws --endpoint-url=http://localhost:4566 dynamodb create-table --table-name todo-app-tasks --attribute-definitions AttributeName=id,AttributeType=N --key-schema AttributeName=id,KeyType=HASH --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5
   ```

3. Create an IAM role for the Lambda function:

   ```sh
   aws --endpoint-url=http://localhost:4566 iam create-role --role-name lambda-execution-role --assume-role-policy-document "{\"Version\": \"2012-10-17\",\"Statement\": [{\"Effect\": \"Allow\",\"Principal\": {\"Service\": \"lambda.amazonaws.com\"},\"Action\": \"sts:AssumeRole\"}]}"
   ```

4. Attach the necessary policies to the IAM role:

   ```sh
   aws --endpoint-url=http://localhost:4566 iam attach-role-policy --role-name lambda-execution-role --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
   aws --endpoint-url=http://localhost:4566 iam attach-role-policy --role-name lambda-execution-role --policy-arn arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess
   ```

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

4. Create the Lambda function:

   ```sh
   aws --endpoint-url=http://localhost:4566 lambda create-function --function-name todo-app-lambda --runtime nodejs14.x --handler index.handler --role arn:aws:iam::123456789012:role/lambda-execution-role --zip-file fileb://lambda.zip
   ```

## Step 7: Creating API Gateway

1. Create an API Gateway REST API:

   ```sh
   aws --endpoint-url=http://localhost:4566 apigateway create-rest-api --name todo-app-api
   ```

2. Retrieve the API Gateway REST API ID:

   ```sh
   aws --endpoint-url=http://localhost:4566 apigateway get-rest-apis
   ```

   Note down the value of the id field.

3. Create a new API Gateway resource:

   ```sh
   aws --endpoint-url=http://localhost:4566 apigateway create-resource --rest-api-id <api-id> --parent-id <root-resource-id> --path-part todos
   ```

   Replace <api-id> with the REST API ID obtained from the previous step and <root-resource-id> with the id of the root resource (usually /').

4. Create a new POST method for the /todos resource:

   ```sh
   aws --endpoint-url=http://localhost:4566 apigateway put-method --rest-api-id <api-id> --resource-id <todos-resource-id> --http-method POST --authorization-type NONE
   ```

   Replace <api-id> with the REST API ID and <todos-resource-id> with the id of the /todos resource obtained from the previous step.

5. Create a new Lambda integration for the POST method:

   ```sh
   aws --endpoint-url=http://localhost:4566 apigateway put-integration --rest-api-id <api-id> --resource-id <todos-resource-id> --http-method POST --type AWS_PROXY --integration-http-method POST --uri arn:aws:lambda:us-east-1:123456789012:function:todo-app-lambda
   ```

   Replace <api-id> with the REST API ID and <todos-resource-id> with the id of the /todos resource obtained from the previous steps.

6. Deploy the API Gateway API:

   ```sh
   aws --endpoint-url=http://localhost:4566 apigateway create-deployment --rest-api-id <api-id> --stage-name dev
   ```

   Replace <api-id> with the REST API ID obtained from previous steps.

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

       const addTask = async () => {
         const task = {
           id: Date.now(),
           name: newTask.value,
         };
         await axios.post("http://localhost:4566/restapis/<api-id>/dev/todos", task);
         tasks.value.push(task);
         newTask.value = "";
       };

       const deleteTask = async (taskId) => {
         await axios.delete(`http://localhost:4566/restapis/<api-id>/dev/todos/${taskId}`);
         tasks.value = tasks.value.filter((task) => task.id !== taskId);
       };

       onMounted(async () => {
         const response = await axios.get("http://localhost:4566/restapis/<api-id>/dev/todos");
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
   aws --endpoint-url=http://localhost:4566 s3 cp dist s3://todo-app-bucket/ --recursive
   ```

3. Retrieve the S3 bucket website URL:

   ```sh
   aws --endpoint-url=http://localhost:4566 s3api get-bucket-website --bucket todo-app-bucket
   ```

   Note down the value of the Endpoint field.

## Step 10: Testing the Deployed App

1. Open your browser and visit the S3 bucket website URL obtained from the previous step. You should see the deployed TODO app.

Congratulations! You have successfully created a simple TODO web app using Vue.js, composition API, and Vite. The app is hosted on an AWS serverless architecture, utilizing S3, API Gateway, Lambda Functions, DynamoDB, and CloudWatch Logs.
