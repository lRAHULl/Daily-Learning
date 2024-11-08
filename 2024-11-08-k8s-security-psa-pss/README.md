# k8s Security - Pod Security Admission (PSA) and Pod Security Standard (PSS)

(and Pod Security Policy -- which are deprecated)

**Pod Security Admission (PSA)** is a Validation admission Controller which checks for labels in a given namespace with the format => `pod-security.kubernetes.io/<mode>:<security standard>`

A pod security admission rule can be applied to a namespace like this 👇🏻

```bash
kubectl label ns my-namespace` pod-security.kubernetes.io/warn=restricted
```

1. PSA is enabled by default in Kubernetes Cluster -- It is an admission controller named ***PodSecurity***.
2. It can be readily used on any namespace just by applying a label as shown in the above example.

### PSA supports 3 modes and 3 security standards

#### Modes

- Enforce - Rejects the apply if the pod definition violates the Security standard
- Audit - Allows the apply but logs a warning in audit logs that a Security standard id violated
- Warn - Allows the apply but displays a user-facing warning that a Security standard id violated

#### Security Standards

- Privileged - Allows everything - [more info](https://kubernetes.io/docs/concepts/security/pod-security-standards/#privileged)
- Baseline - Adds Baseline controls and does basic checks - [more info](https://kubernetes.io/docs/concepts/security/pod-security-standards/#privileged)
- Restricted - Adds Restrictive controls and does robust checks for Security standards - [more info](https://kubernetes.io/docs/concepts/security/pod-security-standards/#privileged)

## *Learn Something new everyday* - Rahul
