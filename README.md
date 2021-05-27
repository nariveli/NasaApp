
**Deploying using docker-compose:**
1. Create an environment variable API_KEY for NASA API token in `.env` file in the root directory of the repository. \
Eg: `API_KEY=<your nasa api token>`
2. Run the command: `docker-compose -f docker-compose.yaml up`

_Use the APIs:_
- [http://localhost:5000/](url)
- [http://localhost:5000/neos](url)
- [http://localhost:5000/neo/week](url)
- [http://localhost:5000/neo/next?hazardous=true](url)


**Deploying in kubernetes:**
1. Run the following commands from the root directory of the repository:
```
kubectl apply -f k8-deployment/pv-volume.yaml 
kubectl apply -f k8-deployment/pv-claim.yaml
kubectl apply -f k8-deployment/server-secret.yaml
kubectl apply -f k8-deployment/server-deployment.yaml
```
2. Run the command: `minikube service flask-service` to access the APIs.

_Use the APIs:_
- [http://<host_ip>:30000/](url)
- [http://<host_ip>:30000/neos](url)
- [http://<host_ip>:30000/neo/week](url)
- [http://<host_ip>:30000/neo/next?hazardous=true](url)


**Deployment using helm chart:**
1. Run the command from root directory of the repo: `helm install < deployment name > helm`
2. Run the command: `minikube service flask-service` to access the APIs.

**_Note: The images are pulled from a private repository. So deployment using helm will fail._**
