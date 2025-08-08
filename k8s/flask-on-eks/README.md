# Deploying Flask App on AWS EKS with Load Balancer (Step-by-Step)

This guide provides a complete, beginner-friendly walkthrough for deploying a Flask app using **Amazon EKS** (Elastic Kubernetes Service) with a **LoadBalancer**. It follows the manual approach (as learned in class) and contrasts it with Infrastructure as Code using **Terraform**.

---

## 🧭 Overview of the Architecture

- **EKS Cluster** with a managed Node Group (EC2)
- **VPC** with Public and Private subnets
- **Internet Gateway** for public access
- **NAT Gateway** in Public subnet to allow Private subnet outbound internet access
- **LoadBalancer** of type `Service` in Kubernetes
- **PVC (Persistent Volume Claim)** for data persistence (optional)
- **IAM Roles** for Cluster and Nodes

---

## 🏗️ STEP 1: Create VPC and Networking Components

1. **VPC with CIDR block** (e.g., `10.0.0.0/16`)
2. **Subnets**:
   - 2 Public Subnets (e.g., `10.0.1.0/24`, `10.0.2.0/24`)
   - 2 Private Subnets (e.g., `10.0.3.0/24`, `10.0.4.0/24`)
3. **Internet Gateway (IGW)**:
   - Attach it to your VPC
   - Update Public Route Table with 0.0.0.0/0 route pointing to IGW
4. **NAT Gateway**:
   - Allocate an Elastic IP
   - Create NAT Gateway in one Public Subnet
   - Update Private Route Table to route 0.0.0.0/0 via the NAT Gateway

📌 *Public Subnets are for LoadBalancer & NAT, Private Subnets are for Worker Nodes*

---

## 🛡️ STEP 2: Create IAM Roles

1. **EKS Cluster Role**
   - Policies: `AmazonEKSClusterPolicy`
2. **EKS Node Group Role**
   - Policies:
     - `AmazonEKSWorkerNodePolicy`
     - `AmazonEC2ContainerRegistryReadOnly`
     - `AmazonEKS_CNI_Policy`

---

## ☸️ STEP 3: Create the EKS Cluster

- Use AWS Console or CLI:
```bash
aws eks create-cluster   --name myEKS   --role-arn <EKS-Cluster-Role>   --resources-vpc-config subnetIds=<private-subnet-ids>,securityGroupIds=<sg-id>
```

Wait until status is **ACTIVE**

---

## 💻 STEP 4: Configure `kubectl`

```bash
aws eks update-kubeconfig --region <your-region> --name myEKS
```

Check:
```bash
kubectl get svc
kubectl get nodes
```

---

## 🧠 STEP 5: Add Node Group

- Use AWS Console → EKS Cluster → Compute → Add Node Group
- Choose:
  - Role: EKS Node Role
  - Capacity type: Spot / On-Demand
  - Instance type: `t3.small`
  - Min: 0, Max: 2, Desired: 1
  - Disk: 20GB default
- Choose **Private subnets**
- Create and wait for provisioning

---

## 🌐 STEP 6: Deploy Flask App with LoadBalancer

### `flask-deployment.yaml`
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: flask-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: flask
  template:
    metadata:
      labels:
        app: flask
    spec:
      containers:
      - name: flask
        image: <your-flask-image>
        ports:
        - containerPort: 5000
```

### `flask-service.yaml`
```yaml
apiVersion: v1
kind: Service
metadata:
  name: flask-lb
spec:
  selector:
    app: flask
  type: LoadBalancer
  ports:
    - port: 80
      targetPort: 5000
```

```bash
kubectl apply -f flask-deployment.yaml
kubectl apply -f flask-service.yaml
```

Check:
```bash
kubectl get svc
```

---

## 💾 STEP 7: Add Persistent Volume (PVC) [Optional]

For local JSON storage or SQLite:
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: flask-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
```

Mount inside deployment:
```yaml
volumeMounts:
- mountPath: /data
  name: flask-storage
volumes:
- name: flask-storage
  persistentVolumeClaim:
    claimName: flask-pvc
```

---

## 🧱 Terraform Alternative

With Terraform you can automate the above:
- `aws_vpc`, `aws_subnet`, `aws_nat_gateway`, `aws_eks_cluster`, `aws_eks_node_group`
- Use `kubernetes_manifest` or `kubectl` to deploy app and service

Benefits:
- Reproducibility
- Version control
- Easier cleanup

---

## 🧹 Cleanup

- Delete LoadBalancer:
```bash
kubectl delete svc flask-lb
kubectl delete deployment flask-app
```

- Delete EKS Node Group → Delete Cluster
- Remove VPC, NAT Gateway, EBS (manually)
- Check costs in:
  [AWS Billing Console](https://console.aws.amazon.com/billing/home)

---

## 📚 Tips

- Use RDS (e.g., PostgreSQL) for production-grade persistence
- Monitor NAT Gateway usage (it’s billable per hour + GB)
- Keep `replicas: 1` if you're using local JSON file

---

Happy Clustering! 🚀
