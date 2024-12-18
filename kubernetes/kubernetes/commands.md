kubectl create secret generic registry-secret \
--from-file=.dockerconfigjson=/Users/bimalrai/.docker> \
--type=kubernetes.io/dockerconfigjson


kubectl get secret registry-secret -o yaml


kubectl create secret docker-registry registry-secret --docker-server=https://index.docker.io/v1/ --docker-username=realhrsoft --docker-password=aayulogic --docker-email=bimal.rai@realhrsoft.com --namespace production

### create namespaces
kubectl create namespace <name>




### create config map file for store .env file secretes and create deployment
kubectl apply -f kubernetes/backend-configmap.yml
kubectl get configmap backend-config -n production -o yaml

kubectl rollout restart deployment/backend-deployment -n production
kubectl delete replicaset backend-replicaset -n production


### delete deployments

kubectl delete deployment backend-deployment  -n production
kubectl delete deployment frontend -n production
### create service
kubectl apply -f kubernetes/redis_service.yml -n database

### port forward or expose port
kubectl port-forward pod/backend-deployment-9459496d9-lf4tq 8000:8000 -n production

### list service
kubectl get svc -n database
### expose service using minikube
minikube service backend-service -n production
minikube service frontend -n production

## list pods
kubectl get pods -o wide -n production

## connect to  postgres db 
kubectl exec -it postgres-db-67b78867c4-6bfp2 -n database -- psql -h localhost -U realhrsoft -d realhrsoft_db
