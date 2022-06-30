# Wikidata query

WIP

## Get the url of all news websites
```
SELECT DISTINCT ?item ?itemLabel ?url WHERE {
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE]". }
  {
    SELECT DISTINCT ?item ?url WHERE {
      ?item p:P31 ?statement0.
      ?item wdt:P856 ?url.
      ?statement0 (ps:P31/(wdt:P279*)) wd:Q1153191.
    }
    LIMIT 10000
  }
}
```
