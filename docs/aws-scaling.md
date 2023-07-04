# Scaling

> If you’ve tried to access a website that wouldn’t load and frequently timed out, the website might have received more requests than it was able to handle. This situation is similar to waiting in a long line at a coffee shop, when there is only one barista present to take orders from customers. (Cloud Practitioner, skill builder)

- [Scalability](concepts.md#scalability)

## Auto Scaling

If you’ve tried to access a website that wouldn’t load and frequently timed out, the website might have received more requests than it was able to handle. This situation is similar to waiting in a long line at a coffee shop, when there is only one barista present to take orders from customers.

### Auto Scaling Group

Auto Scaling Group is a collection of EC2 instances that are treated as a logical grouping for the purposes of automatic scaling and management.

#### Launch Template

Launch Template is a versioned template that an Auto Scaling group uses to launch EC2 instances.

### Auto Scaling approaches

#### Manual Scaling

Manual Scaling is the simplest approach to scaling.

It involves manually adding or removing EC2 instances.

#### Dynamic Scaling

Dynamic Scaling is the most common approach to scaling.

It involves automatically adding or removing EC2 instances based on the load or other metrics.

#### Predictive Scaling

Predictive Scaling is an advanced approach to scaling.

It involves automatically adding or removing EC2 instances based on the predicted load or other metrics.

### Scaling Policies

Scaling Policies are used to scale an Auto Scaling group based on a metric.

#### Target Tracking Scaling Policy

Target Tracking Scaling Policy is used to scale an Auto Scaling group based on a target value for a specific metric.

It is triggered according to the traffic load.

#### Step Scaling Policy

Step Scaling Policy is used to scale an Auto Scaling group based on a set of scaling adjustments, known as step adjustments, that vary based on the size of the alarm breach.

It is triggered when a CloudWatch alarm is triggered.
