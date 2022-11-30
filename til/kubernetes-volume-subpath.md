# kubernetes mount single file with subpath

if you want to just insert 1 file from a configmap, and not have it create an entire
directory, you can use a [subpath](https://kubernetes.io/docs/concepts/storage/volumes/#using-subpath)


```yaml
apiVersion: v1
kind: Service
metadata:
  name: mysql
spec:
  ports:
  - port: 3306
  selector:
    app: mysql
  clusterIP: None
---
apiVersion: apps/v1 
kind: Deployment
metadata:
  name: mysql
spec:
  selector:
    matchLabels:
      app: mysql
  strategy:
    type: Recreate
  template:
    metadata:
      labels:
        app: mysql
    spec:
      containers:
      - image: mysql:5.6
        name: mysql
        env:
          # Use secret in real usage
        - name: MYSQL_ROOT_PASSWORD
          value: password
        ports:
        - containerPort: 3306
          name: mysql
        volumeMounts:
        - name: mysql-configmap-volume
          mountPath: /etc/mysql/conf.d/binlog_format.cnf
          subPath: binlog_format.cnf
      volumes:
      - name: mysql-configmap-volume
        configMap:
          name: mysql-configmap
          items:
          - key: mysql_binlog_format.cnf
            path: binlog_format.cnf
```
