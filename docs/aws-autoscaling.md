# Auto Scaling

- Scaling Out only (not Scaling up)

## Auto Scaling Group

Auto Scaling Group is a collection of EC2 instances that are treated as a logical grouping for the purposes of automatic scaling and management.

### Launch Template

Launch Template is a versioned template that an Auto Scaling group uses to launch EC2 instances.

## Scaling Policies

Scaling Policies are used to scale an Auto Scaling group based on a metric.

### Target Tracking Scaling Policy

Target Tracking Scaling Policy is used to scale an Auto Scaling group based on a target value for a specific metric.

### Step Scaling Policy

Step Scaling Policy is used to scale an Auto Scaling group based on a set of scaling adjustments, known as step adjustments, that vary based on the size of the alarm breach.
