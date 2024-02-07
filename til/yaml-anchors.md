# yaml anchors

Allows you to reuse parts of your yaml somewhere else:

- The anchor '&' which defines a chunk of configuration
- The alias '*' used to refer to that chunk elsewhere


```yaml
definitions: 
  steps:
    - step: &build-test
        name: Build and test
        script:
          - mvn package
        artifacts:
          - target/**

pipelines:
  branches:
    develop:
      - step: *build-test
    main:
      - step: *build-test
```


https://support.atlassian.com/bitbucket-cloud/docs/yaml-anchors/

