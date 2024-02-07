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

You can also tweak the Anchor when called by entering <<: before the Alias.
Below this, you can write any desired changes. Mappings are overridden if the
new mapping has the same name or is added afterward if different.

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
    master:
      - step: 
          <<: *build-test
          name: Testing on Master #override
          ongoing: false #extension
```


- https://www.educative.io/blog/advanced-yaml-syntax-cheatsheet#anchors
- https://support.atlassian.com/bitbucket-cloud/docs/yaml-anchors/

