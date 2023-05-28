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
