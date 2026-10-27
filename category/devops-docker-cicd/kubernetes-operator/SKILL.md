---
name: kubernetes-operator
description: Kubernetes orchestration, Helm chart authoring, production manifest design, and cluster debugging. Use when writing k8s manifests, configuring Helm charts, troubleshooting CrashLoopBackOff, defining ingress/services, or setting up pod autoscaling.
allowed-tools: Read, Write, Edit, Glob, Grep
version: 1.0
category: devops-docker-cicd
---

# Kubernetes Operator

> **Production K8s Manifests, Helm Charts, Pod Diagnostics & Cloud-Native Scaling**

---

## 🏗️ Core Principles

| Principle | Rule |
|-----------|------|
| **Explicit Resource Quotas** | Always set `resources.requests` and `resources.limits` (CPU and Memory) for every container to prevent node eviction. |
| **Liveness & Readiness Probes** | Never deploy pods without HTTP or exec probes. Prevent traffic hitting uninitialized containers. |
| **Immutable Pod Disruption Budgets** | Set PDBs (`minAvailable` / `maxUnavailable`) for high-availability workloads during cluster upgrades. |
| **Stateless by Default** | Keep application pods stateless; offload state to managed databases or persistent volumes with CSI drivers. |
| **Non-Root Security Context** | Run pods with `securityContext.runAsNonRoot: true` and `readOnlyRootFilesystem: true`. |

---

## 📋 Production Deployment Manifest Pattern

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-service
  labels:
    app: api-service
spec:
  replicas: 3
  selector:
    matchLabels:
      app: api-service
  template:
    metadata:
      labels:
        app: api-service
    spec:
      securityContext:
        runAsNonRoot: true
        runAsUser: 10001
      containers:
      - name: api
        image: ghcr.io/myorg/api:v1.4.2
        imagePullPolicy: IfNotPresent
        ports:
        - containerPort: 8080
        resources:
          requests:
            cpu: "100m"
            memory: "128Mi"
          limits:
            cpu: "500m"
            memory: "512Mi"
        readinessProbe:
          httpGet:
            path: /healthz/ready
            port: 8080
          initialDelaySeconds: 5
          periodSeconds: 10
        livenessProbe:
          httpGet:
            path: /healthz/live
            port: 8080
          initialDelaySeconds: 10
          periodSeconds: 15
```

---

## 📋 Diagnostics & Troubleshooting Runbook

- **CrashLoopBackOff**: Inspect logs: `kubectl logs <pod-name> --previous` and describe pod: `kubectl describe pod <pod-name>`.
- **OOMKilled**: Verify if limits are too tight or memory leak exists: `kubectl get pod <pod-name> -o jsonpath='{.status.containerStatuses[*].lastState.terminated.reason}'`.
- **Pending Pods**: Check cluster resource exhaustion, node affinity/taints, or PVC mounting failures via `kubectl describe pod`.

---

## ❌ Anti-Patterns

- ❌ Using `:latest` tags in Kubernetes Deployment manifests.
- ❌ Omission of memory limits leading to cluster-wide OOM cascade.
- ❌ Hardcoding secrets in ConfigMaps rather than Kubernetes Secrets / External Secrets Operator.
