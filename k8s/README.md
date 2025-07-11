# Flask Task Manager on Kubernetes

This project demonstrates how to deploy a simple **Flask-based Task Manager API** in a Kubernetes cluster. It includes configuration files for:

- A Pod running the Flask app
- A ConfigMap to inject environment variables
- A Service for exposing the app externally
- A utility Pod (`user-pod`) for internal testing/debugging (using Alpine)

---

## 📁 Project Structure

```bash
my_k8s/
├── flask_app_pod.yaml       # Pod definition for the Flask application
├── flask-configmap.yaml     # ConfigMap with environment variables
├── service.yaml             # NodePort Service to expose the Flask app
├── user_pod.yaml            # Alpine Pod for internal debugging
```

---

## ⚙️ Prerequisites

- Kubernetes cluster (Minikube, Kind, etc.)
- `kubectl` CLI configured to access your cluster
- Internet access from the cluster to pull the image: `codeislife771/flask-task-manager:latest`

---

## 🚀 How to Deploy

1. **Apply the ConfigMap**:
   ```bash
   kubectl apply -f flask-configmap.yaml
   ```

2. **Deploy the Flask Pod**:
   ```bash
   kubectl apply -f flask_app_pod.yaml
   ```

3. **Expose the Pod using a Service**:
   ```bash
   kubectl apply -f service.yaml
   ```

4. **(Optional) Deploy Debugging Pod**:
   ```bash
   kubectl apply -f user_pod.yaml
   ```

---

## 🌐 Accessing the Flask App

Once the Service is running, find the Node IP (if using Minikube):

```bash
minikube ip
```

Then access the app via:

```
http://<NODE_IP>:30080/tasks
```

You can test it using `curl`:

```bash
curl http://<NODE_IP>:30080/tasks
```

---

## 📦 Environment Variables (from ConfigMap)

Defined in `flask-configmap.yaml`:

```yaml
PORT: 5000
DEBUG: true
DB_HOST: localhost
```

These are automatically injected into the Flask container using `envFrom`.

---

## 🔍 Probes

Both **liveness** and **readiness** HTTP probes are configured to hit `/tasks` on port 5000.  
They help Kubernetes manage the health and availability of the app.

---

## 🛠 Debug with Alpine Pod

Use the `user-pod.yaml` to create a simple Alpine container for testing internal connectivity:

```bash
kubectl exec -it user-pod -- sh
```

From inside, you can use `wget` or `ping` (if installed) to check connectivity to the Flask app.

---

## 📌 Notes

- `restartPolicy: OnFailure` ensures the Flask pod restarts only if it crashes (non-zero exit code).
- `Service` is of type `NodePort`, exposing the app on port `30080`. You can change this if needed.
- Make sure `flask-config` ConfigMap is applied before the pod starts.

---

## ✅ Cleanup

To delete all created resources:

```bash
kubectl delete -f .
```

Or individually:

```bash
kubectl delete -f flask_app_pod.yaml
kubectl delete -f flask-configmap.yaml
kubectl delete -f service.yaml
kubectl delete -f user_pod.yaml
```

---

## 📄 License

This project is for educational and development purposes. No license included.
