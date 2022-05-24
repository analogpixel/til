# Clojure database access sqlite/jdbc

## update your dependencies
```
[org.clojure/java.jdbc "0.7.5"]
[org.xerial/sqlite-jdbc "3.7.2"]
```

## define your db
```
(def db
  {:classname   "org.sqlite.JDBC"
   :subprotocol "sqlite"
   :subname     "/Users/poepping/experiments/clojure_experiments/find-interesting-links/links.db"})
```

## insert data
`(sql/insert! db :links {:url link :links "" :words ""})`


## select data
`(sql/query db (str "select url from links where url='" url "'")`


