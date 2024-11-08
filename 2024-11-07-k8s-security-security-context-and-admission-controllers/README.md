# K8s Security - Security Context and Admission Controller

## [Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)

Security context in k8s is used to control what permissions the pods (and containers with the pods) are run with.

It has two main specifications.

1. runAsUser - Configures which system user the pod/container is run with (0 represents root user)
2. capabilities - Configures which system capabilities to add/remove to a pod/container (eg: SYS_CAP_ADMIN - this gives all the root persmissions to the system)

Refer [this](https://linux.die.net/man/7/capabilities) for list of available system capabilities.

## [Admission Contollers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/)

Admission Controller is component in k8s that are used to modify/validate object definition before they are applied in k8s.

There are two types:

1. Mutating - Modifies the objects based on rules before they are applied.
2. Validating - Validates the objects based on rules before they are applied.

There are Admission controllers which come pre-packaged with k8s and few are enabled by default (ex: DefaultStorageClass)

[Here](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/) is the full list of available Admission Contollers.

However we are not limited to these provided by k8s.

We can create our own by deploying our own webhook server.

It should have 2 POST api methods.

1. `/mutate`
2. `/validate`

And after the webhook service is hosted (either in the same cluster/externally) it should be registered with `ValidatingWebhookConfiguration` and `MutatingWebhookConfiguration`

After this we can use this based on the rules specified in the registration objects.

Refer this [blog1](https://medium.com/@platform.engineers/building-custom-admission-controllers-in-go-for-kubernetes-271168ec56b5) and [blog2](https://bshayr29.medium.com/build-your-own-admission-controllers-in-kubernetes-using-go-bef8ba38d595) for reference in building and registring custom admission controllers.

Some of the common usecases for Admission Controller that i noticed/encountered before:

1. Injecting sidecars into pods based on annotations/some other rules - [Istio](https://istio.io/latest/blog/2019/data-plane-setup/#automatic-injection)
2. Injecting Secrets into pods based on annotations - [Vault](https://developer.hashicorp.com/vault/tutorials/kubernetes/kubernetes-sidecar#apply-a-template-to-the-injected-secrets)

<!-- Today was a longer session of learning - and writing this took more than 30 mins 👨‍💻 -->

## *Learn Something New Everyday* - Rahul
