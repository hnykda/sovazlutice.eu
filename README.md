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
