# ⚙️ Jenkins Setup for DevOps Projects – Step 1: Local WSL Installation

This repository documents the process of setting up **Jenkins** as part of a practical DevOps learning journey. The first step is focused on **installing Jenkins locally** using **WSL (Windows Subsystem for Linux)**.

This setup supports building a CI (Continuous Integration) pipeline for Python projects, such as the `cipher.py` tool developed in this repository.

---

## 📦 CI/CD Setup – 3 Deployment Options

We will gradually explore three ways to deploy Jenkins. This README covers **Step 1**.

| Step | Deployment Method             | Use Case                                | Status        |
|------|-------------------------------|------------------------------------------|---------------|
| 1    | 🖥️ Local via WSL              | Simple, lightweight, great for learning  | ✅ Completed  |
| 2    | 💻 Remote via VM (e.g. VMware) | Closer to production-like environments   | 🔜 Planned    |
| 3    | 📦 Docker container           | Portable and isolated CI setup           | 🔜 Planned    |

---

## ✅ Why Jenkins on WSL?

- No need to install heavy virtualization tools
- Seamless access to your local filesystem and Git
- Quick to get started with Python projects and scripting
- Easy to tear down and rebuild
- Great for learning CI pipelines in a controlled environment

---

## 🧰 Prerequisites

- Windows 10/11 with WSL2 enabled
- Ubuntu installed in WSL
- Git installed and configured
- Python installed inside WSL
- Basic familiarity with the command line

---

## 🛠️ Step-by-Step: Installing Jenkins on WSL

### 1. Launch Ubuntu in WSL

From the Start menu or terminal:

```bash
#1. Run Ubuntu
wsl -d Ubuntu
lsb_release -a

#2. Install Java (required by Jenkins)
sudo apt update
sudo apt install openjdk-11-jdk -y

#Confirm installation
java -version

#3. Add Jenkins GPG Key and Repository
curl -fsSL https://pkg.jenkins.io/debian/jenkins.io-2023.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null

echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null

#4. Install Jenkins
sudo apt update
sudo apt install jenkins -y

#5. Start Jenkins Manually (no systemd in WSL)
    sudo service jenkins start
    # If `sudo service jenkins start` fails (common in WSL), use this:
    # - Download Jenkins Manually via WAR - Checking jenkins.war stable version -> https://get.jenkins.io/war-stable/
    mkdir -p ~/jenkins
    cd ~/jenkins
    wget https://get.jenkins.io/war-stable/2.426.1/jenkins.war
    echo "Starting Jenkins..."

    # 2 Options to running jenkins.war file
        #A. Run Jenkins Manually
            # In your WSL shell:
                java -jar ~/jenkins/jenkins.war --httpPort=8080 --httpListenAddress=0.0.0.0

        #B. Run Jenkins in the Background (Recommended)
                cd ~/jenkins
                nohup java -jar jenkins.war \
                --httpPort=8080 \
                --httpListenAddress=0.0.0.0 \
                > jenkins.log 2>&1 &
                echo "Jenkins is running in the background (PID $!) and logging to jenkins.log."

#6. Verify Jenkins is Running
    # Check the process
    ps aux | grep [j]enkins

    # Confirm listening on port 8080
    sudo lsof -iTCP:8080 -sTCP:LISTEN

#6. Access Jenkins from Windows Browser
    #Find the IP address of your WSL instance
    ip addr show eth0 | grep inet
    # OR 
    hostname -I

    #Example output:
    inet 172.20.58.138/20

    #Open Jenkins in your Windows browser:
    http://172.20.58.138:8080
    # OR
    http://localhost:8080


#7. Retrieve the Initial Admin Password
        #By default, Jenkins generates an initial administrator password in its home directory. For manual WAR launches, the default Jenkins home is ~/.jenkins:
        cat ~/.jenkins/secrets/initialAdminPassword
        # OR - If you specified a custom home via the --prefix argument or the JENKINS_HOME environment variable, replace ~/.jenkins with that directory:
        cat $JENKINS_HOME/secrets/initialAdminPassword

    # - Paste the password into the Jenkins setup screen
    # - Install suggested plugins
    # - Create an admin user
