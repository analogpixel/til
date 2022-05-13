# kubernetes Job

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: pi
spec:
  template:
    spec:
      containers:
      - name: pi
        image: perl
        command: ["perl",  "-Mbignum=bpi", "-wle", "print bpi(2000)"]
      restartPolicy: Never
  backoffLimit: 4
```

> When a Job completes, no more Pods are created, but the Pods are usually not deleted either. Keeping them around allows you to still view the logs of completed pods to check for errors, warnings, or other diagnostic output. The job object also remains after it is completed so that you can view its status. It is up to the user to delete old jobs after noting their status. Delete the job with kubectl (e.g. kubectl delete jobs/pi or kubectl delete -f ./job.yaml). When you delete the job using kubectl, all the pods it created are deleted too.

## Terminate after time
`.spec.activeDeadlineSeconds`  will terminate the pod after a number of seconds. A [ttl controller](https://kubernetes.io/docs/concepts/workloads/controllers/ttlafterfinished/) can be used to clean up jobs after a certain time.

## links
* https://kubernetes.io/docs/concepts/workloads/controllers/job/
* https://kubernetes.io/docs/concepts/workloads/controllers/ttlafterfinished/

