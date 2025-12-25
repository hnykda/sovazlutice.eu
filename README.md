# Sovazlutice.eu

Django website for the village of Sovažlutice.

## Development

```bash
docker-compose up
```

## Deployment

Deployed to Hera K8s cluster via Woodpecker CI.

**Automatic**: Push to `master` triggers build + deploy.

**Manual deploy**:
```bash
# Build and push
docker build -f Dockerfile.k8s -t localhost:32000/sovazlutice:latest .
docker push localhost:32000/sovazlutice:latest

# Deploy secrets (first time or after changes)
sops -d secrets/secrets.yaml | kubectl apply -f -

# Deploy
helm upgrade --install sovazlutice ./chart --namespace apps
```

**Secrets**: SOPS-encrypted in `secrets/secrets.yaml`. Edit with:
```bash
SOPS_AGE_KEY_FILE=/path/to/age-key.txt sops secrets/secrets.yaml
```

## Media Files

Media files (django/media/pictures/) are stored on a Persistent Volume Claim (PVC) in Kubernetes, not in the Docker image.

**Restore media files to PVC** (after fresh deployment or if media is missing):
```bash
# On the Hera server
cd /root/server-files/repos/sovazlutice
tar czf /tmp/media-pictures.tar.gz -C django/media pictures

# Copy to local machine and then to pod
POD=$(kubectl get pods -n apps -l app=sovazlutice -o jsonpath='{.items[0].metadata.name}')
kubectl cp /tmp/media-pictures.tar.gz apps/$POD:/tmp/media-pictures.tar.gz -c django
kubectl exec -n apps $POD -c django -- sh -c "cd /src/media && tar xzf /tmp/media-pictures.tar.gz"
```

**Backup media files from PVC**:
```bash
POD=$(kubectl get pods -n apps -l app=sovazlutice -o jsonpath='{.items[0].metadata.name}')
kubectl exec -n apps $POD -c django -- tar czf /tmp/media-backup.tar.gz -C /src/media pictures
kubectl cp apps/$POD:/tmp/media-backup.tar.gz /tmp/media-backup-$(date +%Y%m%d).tar.gz -c django
```
