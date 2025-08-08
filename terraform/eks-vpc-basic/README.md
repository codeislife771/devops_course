
# Terraform Exercise - VPC Setup (main.tf only)

This Terraform script (`main.tf`) sets up a basic AWS Virtual Private Cloud (VPC) using a public module. It is intended as a classroom exercise and demonstrates how to declare a provider and use a VPC module.

## ✅ What this script does

- Uses the AWS provider in region `us-east-1`
- Creates a VPC with CIDR `10.0.0.0/16`
- Defines:
  - 2 Availability Zones: `us-east-1a`, `us-east-1b`
  - 2 Private Subnets: `10.0.1.0/24`, `10.0.2.0/24`
  - 2 Public Subnets: `10.0.3.0/24`, `10.0.4.0/24`
- Enables a single NAT Gateway to allow internet access from private subnets
- Tags the VPC with `Owner = Chen`, `Environment = dev`

## 💡 Purpose

This configuration helps students understand how to:

- Declare a Terraform provider
- Use a Terraform module from the public registry
- Pass inputs like subnets, AZs, and tags to a module

## ▶️ How to run

> Before you begin, make sure your AWS credentials are configured (via `aws configure` or environment variables).

Run the following commands from the folder where `main.tf` is located:

```bash
terraform init         # Download required providers and modules
terraform validate     # Optional: Check for syntax or config errors
terraform plan         # Optional: Preview what will be created
terraform apply        # Run and approve to create infrastructure
```

---

