# Docker Build Args

If you want to pass arguments to a docker build you would use `ARG`

```
FROM image

ARG MY_VAR_1
ARG MY_VAR_2_WITH_DEFAULT="default value"

RUN echo "$MY_VAR_1"
```

and then from the docker build command:

```
docker build --build-arg MY_VAR_1=new_value
```

## links
- https://vsupalov.com/docker-arg-env-variable-guide/
