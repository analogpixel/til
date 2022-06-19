# Python Sqlite

## Connect to a database
```python
import sqlite3

con = sqlite3.connect("data_collect/links.db")
cur = con.cursor()
...
con.commit()
con.close()
```

## Update a row
`cur.execute("update links set scanned=? where url=?", (True, url) )`

## Insert if doesn't exist

* Create a table that has a unique `CREATE TABLE links (url TEXT, rating INTEGER, words TEXT, scanned BOOLEAN, UNIQUE(url)) ;`
* use `REPLACE`
  * `cur.executemany( "REPLACE into links (url, rating, scanned) values (?,?,?)", insert )`
