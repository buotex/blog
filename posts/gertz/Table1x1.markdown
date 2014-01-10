{
  "title": "Table1x1",
  "date": "2013-12-16",
  "categories": [
	"databases",
"basics"

  ],
 "widgets": {
        "google_prettify": {
            "use": "sql"
        }
    }
}

##Erstellen einer Tabelle
Eine Tabelle hat einen **Namen**
```CREATE TABLE testtable;```

sowie einige Datentypen
So z.B.
```
CREATE TABLE polygons(polygon_id int, point_id int);
```

###Important tricks

####Replace outer join with a subquery

~~~sql
select distinct mems.firstname || ' ' ||  mems.surname as member,
  (select recs.firstname || ' ' || recs.surname as recommender 
    from cd.members recs 
    where recs.memid = mems.recommendedby
  )
  from 
    cd.members mems
order by member;
~~~


The use of where in a _subquery_ allows null results, which can be used to
emulate outer joins (in this case, a left outer join)
The alternative solution by using a join is

~~~sql
select distinct mems.firstname || ' ' ||  mems.surname as member,
recs.firstname || ' ' || recs.surname as recommender
from cd.members mems left join cd.members as recs 
on recs.memid = mems.recommendedby
order by member;
~~~

``A subquery that uses information from the outer query in this way (and thus has
to be run for each row in the result set) is known as a correlated subquery.``




####Extracting part of a field:
``extract(month from starttime)``


####Common table expressions

[Doc](http://www.postgresql.org/docs/9.2/static/queries-with.html)

~~~sql
with sum as (select facid, sum(slots) as totalslots
  from cd.bookings
  group by facid
)
select facid, totalslots 
  from sum
  where totalslots = (select max(totalslots) from sum);
~~~

####String functions
- trim() #remove extra spaces
- to_char(34.234, '999999D99') #output with 6 in front, 2 after decimal point



####Window functions

[PGExercises](http://pgexercises.com/questions/aggregates/countmembers.html)
[Docs](http://www.postgresql.org/docs/9.1/static/functions-window.html)

Window functions operate on the result set of your (sub-)query, after the WHERE
clause and all standard aggregation. They operate on a window of data. By
default this is unrestricted: the entire result set, but it can be restricted to
provide more useful results. For example, suppose instead of wanting the count
of all members, we want the count of all members who joined in the same month as
that member:

###Open questions:

- Union vs Union All?
- Outer vs inner join
-dd







References:

- http://www.postgresql.org/docs/9.2/static/tutorial-join.html

