# HELM library chart values

## Creating the library chart

Create a Library chart and update the Chart.yaml file with the following content:

```yaml
apiVersion: v2
name: sample_library
description: a test library chart
type: library
version: 0.1.0
appVersion: "1.16.0"
```

not the difference between the normal chart and the library chart is the type field. The type field is set to library for library charts.

now, edit the values.yaml file and add the following content:

```yaml
myvar: 1
```

to create the package you can now run `helm package .` in the root of the library chart.

## Linking to the Library Chart

to link to the library chart, update your chart.yaml in the main chart with the following content:

```yaml
dependencies:
- name: sample_library
  version: 0.1.0
  repository: file://../sample_library/
```

make sure the version and name match the library chart.

now you can run `helm dep build` and `helm dep list` and you should see your library chart listed with a STATUS of `ok`

## Using the Variables

`{{ .Values.sample_library.myvar }}`
