
# Terraform AWS VPC Project

This project sets up a basic Virtual Private Cloud (VPC) in AWS using Terraform. It's intended as an educational exercise to help you understand how to work with Terraform modules and AWS infrastructure.

---

## 🚀 Getting Started from Scratch

Follow these steps to set up and run the project:

### 1. ✅ Prerequisites

Make sure the following are installed on your system:

- [Terraform](https://developer.hashicorp.com/terraform/downloads)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- An AWS account

### 2. 🔐 Configure AWS Access

Set up your AWS credentials so Terraform can create resources:

```bash
aws configure
```

You will be asked for:

- AWS Access Key ID
- AWS Secret Access Key
- Default region (use `us-east-1` for this project)
- Default output format (optional: `json`)

Alternatively, use environment variables:

```bash
export AWS_ACCESS_KEY_ID="your-access-key-id"
export AWS_SECRET_ACCESS_KEY="your-secret-access-key"
export AWS_DEFAULT_REGION="us-east-1"
```

### 3. 📦 Initialize the project

Navigate to the folder containing `main.tf` and run:

```bash
terraform init
```

This will download the required provider and modules.

### 4. ✅ (Optional) Validate and plan

```bash
terraform validate     # Checks for syntax/config issues
terraform plan         # Shows what Terraform intends to create
```

### 5. ⚙️ Apply the configuration

```bash
terraform apply
```

Type `yes` when prompted to approve creation.

### 6. 🧹 Clean up (optional)

To remove all resources:

```bash
terraform destroy
```

---

## ℹ️ Notes

- This project uses a public Terraform module to simplify VPC creation.
- The setup includes private and public subnets, NAT gateway, and tagging.
- You can expand this project later to include EKS, EC2, or RDS.

---

Happy Terraforming! ☁️
