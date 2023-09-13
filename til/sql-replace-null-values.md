# SQL replace null values

you can use coalesce to replace null values with real values;  The function will return the first value that isn't null:

select coalesce(comm,0) from emp

another option using the case statement:

```
select case
  when comm is not null then comm
  else 0
  end
from emp
```
