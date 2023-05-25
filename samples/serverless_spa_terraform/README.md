# Building a Serverless Vue.js TODO Web App on AWS with Terraform

In this tutorial, we will walk through the process of creating a simple Vue.js TODO web app with create, edit, and delete functionality. We will leverage the power of the Vue.js composition API and Vite for development, and we will host our application on an AWS serverless architecture using services such as S3, API Gateway, Lambda Functions, DynamoDB, and CloudWatch Logs. Additionally, we will use Terraform for provisioning and managing our AWS infrastructure.

## Prerequisites

Before we begin, please ensure you have the following:

- Node.js and npm installed on your local machine.
- AWS CLI installed and configured with your AWS credentials.
- Terraform installed on your local machine.
- Docker installed to run LocalStack for local development and testing.

## Setting up the Project

To get started, let's set up our project structure and install the necessary dependencies. Open your terminal and run the following commands:

```sh
# Create a new Vue.js project using Vite
npm init vite@latest my-todo-app
cd my-todo-app
npm install

# Add Vue Router and Axios for API communication
npm install vue-router axios
```

## Creating the TODO App

Now, let's create the necessary components and API calls for our TODO app.

1. Create a file called src/components/TodoList.vue with the following content:

   ```vue
   <template>
     <div>
       <h2>TODO List</h2>
       <ul>
         <li v-for="todo in todos" :key="todo.id">
           {{ todo.title }}
           <button @click="deleteTodo(todo.id)">Delete</button>
         </li>
       </ul>
       <form @submit.prevent="createTodo">
         <input type="text" v-model="newTodo" placeholder="Add a new TODO" />
         <button type="submit">Add</button>
       </form>
     </div>
   </template>

   <script>
   import { ref, reactive, onMounted } from "vue";
   import axios from "axios";

   export default {
     setup() {
       const todos = ref([]);
       const newTodo = ref("");

       const fetchTodos = async () => {
         const response = await axios.get("/todos");
         todos.value = response.data.todos;
       };

       const createTodo = async () => {
         await axios.post("/todos", { title: newTodo.value });
         newTodo.value = "";
         await fetchTodos();
       };

       const deleteTodo = async (id) => {
         await axios.delete(`/todos/${id}`);
         await fetchTodos();
       };

       onMounted(fetchTodos);

       return { todos, newTodo, createTodo, deleteTodo };
     },
   };
   </script>
   ```

2. Create a file called src/components/EditTodo.vue with the following content:

   ```vue
   <template>
     <div>
       <h2>Edit Todo</h2>
       <form @submit.prevent="updateTodo">
         <input type="text" v-model="editedTodo.title" />
         <button type="submit">Update</button>
       </form>
     </div>
   </template>

   <script>
   import { ref } from "vue";
   import axios from "axios";

   export default {
     props: ["todo"],

     setup(props) {
       const editedTodo = ref({ ...props.todo });

       const updateTodo = async () => {
         await axios.put(`/todos/${props.todo.id}`, editedTodo.value);
         // Emit an event to notify the parent component
         // about the update and close the modal.
         // You can implement this part based on your preference.
       };

       return { editedTodo, updateTodo };
     },
   };
   </script>
   ```

3. Update src/App.vue with the following content:

   ```vue
   <template>
     <div>
       <router-view></router-view>
     </div>
   </template>

   <script>
   export default {
     name: "App",
   };
   </script>
   ```

4. Create a file called src/router/index.js with the following content:

   ```js
   import { createRouter, createWebHistory } from "vue-router";
   import TodoList from "../components/TodoList.vue";

   const routes = [
     {
       path: "/",
       name: "TodoList",
       component: TodoList,
     },
   ];

   const router = createRouter({
     history: createWebHistory(),
     routes,
   });

   export default router;
   ```

5. Update src/main.js with the following content:

   ```js
   import { createApp } from "vue";
   import App from "./App.vue";
   import router from "./router";

   createApp(App).use(router).mount("#app");
   ```

## Setting up AWS Infrastructure with Terraform

Now, let's provision our AWS infrastructure using Terraform. We'll create an S3 bucket, API Gateway, Lambda functions, DynamoDB table, and CloudWatch Logs.

1. Create a new file called main.tf in the project root directory with the following content:

   ```terraform
   terraform {
   required_providers {
       aws = {
       source = "hashicorp/aws"
       version = "~> 3.0"
       }
   }
   }

   provider "aws" {
   region = "us-west-2"
   }

   resource "aws_s3_bucket" "todo_app_bucket" {
   bucket = "my-todo-app-bucket"
   }

   resource "aws_dynamodb_table" "todo_app_table" {
   name           = "TodoAppTable"
   billing_mode   = "PAY_PER_REQUEST"
   hash_key       = "id"
   attribute {
       name = "id"
       type = "S"
   }
   }

   resource "aws_apigatewayv2_api" "todo_app_api" {
   name = "TodoAppAPI"
   }

   resource "aws_apigatewayv2_integration" "todo_app_integration" {
   api_id             = aws_apigatewayv2_api.todo_app_api.id
   integration_type   = "AWS_PROXY"
   integration_uri    = aws_lambda_function.todo_app_lambda.arn
   integration_method = "POST"
   }

   resource "aws_apigatewayv2_route" "todo_app_route" {
   api_id    = aws_apigatewayv2_api.todo_app_api.id
   route_key = "ANY /{proxy+}"
   target    = "integrations/${aws_apigatewayv2_integration.todo_app_integration.id}"
   }

   resource "aws_lambda_function" "todo_app_lambda" {
   function_name = "TodoAppLambda"
   runtime = "nodejs14.x"
   handler = "index.handler"
   timeout = 5

   lifecycle {
       create_before_destroy = true
   }

   depends_on = [aws_s3_bucket.todo_app_bucket, aws_dynamodb_table.todo_app_table]

   provisioner "local-exec" {
       command = "npm run build && cd dist && zip -r ../todo-app.zip ."
   }

   provisioner "local-exec" {
       command = "aws --endpoint-url=http://localhost:4566 s3 cp todo-app.zip s3://my-todo-app-bucket/todo-app.zip"
   }

   provisioner "local-exec" {
       command = <<EOT
       aws --endpoint-url=http://localhost:4566 lambda create-function \
           --function-name TodoAppLambda \
           --runtime nodejs14.x \
           --role arn:aws:iam::123456789012:role/lambda-execution-role \
           --handler index.handler \
           --memory-size 128 \
           --timeout 5 \
           --code S3Bucket=my-todo-app-bucket,S3Key=todo-app.zip
       EOT
   }
   }

   output "api_gateway_endpoint" {
   value = aws_apigatewayv2_api.todo_app_api.api_endpoint
   }
   ```

2. Create a new file called variables.tf in the project root directory with the following content:

   ```terraform
   variable "aws_access_key" {
   type    = string
   default = ""
   }

   variable "aws_secret_key" {
   type    = string
   default = ""
   }

   variable "aws_session_token" {
   type    = string
   default = ""
   }

   variable "aws_region" {
   type    = string
   default = "us-west-2"
   }
   ```

3. Create a new file called backend.tf in the project root directory with the following content:

   ```terraform
   terraform {
   backend "s3" {
       bucket = "my-todo-app-tfstate"
       key    = "terraform.tfstate"
       region = "us-west-2"
   }
   }
   ```

4. Run the following commands to initialize and apply the Terraform configuration:

   ```terraform
   # Initialize Terraform
   terraform init

   # Apply the Terraform configuration
   terraform apply
   ```

During the terraform apply command execution, Terraform will provision the AWS resources defined in main.tf and store the state in an S3 bucket defined in backend.tf.

## Configuring LocalStack for Local Development

For local development and testing, we'll use LocalStack to emulate the AWS services. LocalStack provides a Docker-based environment that replicates the behavior of various AWS services.

1. Run the following command to start LocalStack:

   ```sh
   docker run --rm -it -p 4566:4566 -p 4571:4571 localstack/localstack
   ```

2. Set up the necessary AWS CLI environment variables:

   ```sh
   export AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY_ID
   export AWS_SECRET_ACCESS_KEY=YOUR_SECRET_ACCESS_KEY
   export AWS_DEFAULT_REGION=us-west-2
   ```

## Testing the Serverless Infrastructure

Now that our infrastructure is provisioned and LocalStack is running, let's test our serverless architecture.

1. Update the API endpoint in the src/components/TodoList.vue file to use the LocalStack endpoint:

   ```js
   const apiEndpoint = process.env.NODE_ENV === "production" ? "/todos" : "http://localhost:4566/todos";
   ```

2. Build and run the Vue.js TODO app:

   ```sh
   npm run build
   npm run serve
   ```

3. Open your web browser and navigate to http://localhost:8080 to access the TODO app.

4. Test the app by adding, editing, and deleting TODOs.

## Conclusion

Congratulations! You have successfully built a simple Vue.js TODO web app with create, edit, and delete functionality. You have also provisioned an AWS serverless architecture using Terraform, which includes S3, API Gateway, Lambda Functions, DynamoDB, and CloudWatch Logs.

This tutorial covered the basics, but there are numerous ways to enhance and extend this application. Consider implementing user authentication, adding additional features, or optimizing performance.

Remember to clean up your AWS resources by running terraform destroy when you're finished with the tutorial to avoid any unnecessary costs.

Feel free to explore and customize the application to fit your specific needs. Happy coding!
