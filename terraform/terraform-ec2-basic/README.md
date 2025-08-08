# 🌱 Mini Terraform Project – DevOps Course Starter

This is a simple Terraform project designed for **beginners** as part of a DevOps course.

It launches a **t2.micro EC2 instance** (Free Tier eligible) in **us-east-1** region on AWS.

---

## 📁 Files to Create

Inside a folder named `mini-terraform-project`, create the following files:

1. `main.tf` – The Terraform configuration file.
2. `README.md` – This guide file.

---

## 🔧 main.tf Content

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "example" {
  ami           = "ami-0c2b8ca1dad447f8a"  # Amazon Linux 2 (Free Tier)
  instance_type = "t2.micro"

  tags = {
    Name = "DevOpsCourseInstance"
  }
}
```

---

## ✅ Requirements

- AWS account with an IAM user that has EC2 permissions (e.g., `AmazonEC2FullAccess`)
- AWS CLI installed and configured (`aws configure`)
- Terraform installed (`terraform --version`)

---

## 🚀 How to Use This Project

```bash
# 1. Create and enter the project directory
mkdir mini-terraform-project
cd mini-terraform-project

# 2. Create the main.tf file and paste the content above

# 3. Initialize Terraform
terraform init

# 4. Validate the configuration
terraform validate

# 5. (Optional) See the execution plan
terraform plan

# 6. Apply the configuration to launch the EC2 instance
terraform apply
# When prompted, type: yes
```

---

## 🧹 Clean Up (To Avoid Charges)

```bash
terraform destroy
# When prompted, type: yes
```

---

## 💡 Notes

- This example uses **Amazon Linux 2** AMI in `us-east-1` (adjust if needed).
- The instance type is **t2.micro**, which is Free Tier eligible.
- No SSH, no key pair, no outputs – this is a minimal beginner demo.

Happy Terraforming! 🌍
