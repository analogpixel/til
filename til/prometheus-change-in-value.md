# prometheus promql count change in value

- `changes` : (good for a metric that change from 0/1 1/0 or something) For each input time series, changes(v range-vector) returns the number of times its value has changed within the provided time range as an instant vector.
- `resets` : (good for a metric that counts up and the zeros out) For each input time series, resets(v range-vector) returns the number of counter resets within the provided time range as an instant vector. Any decrease in the value between two consecutive samples is interpreted as a counter reset.

## watch for number of restarts over 24hour period of java proc
`changes(java_lang_Runtime_StartTime{instance="hostname"}[24h])`


## links
* https://utcc.utoronto.ca/~cks/space/blog/sysadmin/PrometheusChangesFunction
* https://utcc.utoronto.ca/~cks/space/blog/sysadmin/PrometheusResetsFunction
