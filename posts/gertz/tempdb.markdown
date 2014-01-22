{
  "title": "Temporal databases",
  "date": "2014-01-21",
  "categories": [
    "unsorted"
  ],
  "tags": [
    
  ]
}

#Basics

##Goals
As events in real-life may happen in specific moments or cover specific timeframes, we want to
design a database to cover these cases.
To achieve this goal, we add temporal state to the data, which may evolve with time, in the form of
a time interval $$[t.start, t.end]$$.
Important to note: in our design, it is only possible to change the **present**, it is thus
impossible to change past states for the integrity of the database.
Closest real-life example for us: **Git**!

- Deletion is logical: To delete an object, we set its end date to a specific value.
- Otherwise, all objects are considered to be alive till "now", if that value is not set.

#####Requirements for index methods:
- Store past logical states
- Support addition/deletion/modification of the objects of the current state
- Efficiently access and query any database state

#####Some examples for queries:
- Timestamp (timeslice) queries: Give me all employees at 05/94
- Range-timeslice: Find all employees with id between 100 and 200 that worked in the
company on 05/94
- Interval (period) queries: Find all employees with id in [100,200] from 05/94 to 06/96


##Transaction time
- Models **Database reality**
- When a row is “deleted” from the table, the row is not physically deleted from the table. Instead,
the transaction-time column is automatically modified to have an ending bound that specifies the
time of the deletion, which marks the row as “closed,” and no longer available.
- When a row is “modified” in the table, the original row with the original values is marked as
closed, and a copy of the row having the modified values is automatically inserted into the table.
The resulting snapshots of deleted and modified rows, which are retained in the table, provide a
complete internal history of the table. 
- Any prior state of a table having a transaction-time column
can be reproduced. 
- However, closed rows are unavailable to most DML modifications or deletions.
Add transaction-time columns to tables for which historical changes should be automatically tracked
and maintained in the database. For example, transaction-time tables can be used for information
that must retain a history of all changes, such as for tables used for regulatory compliance
reporting.


##Valid time
- Models **Real world reality**
- Because they model the real world, valid-time tables can have rows
 with a PV in the future, because things like contracts and policies may not begin until a future
 date.
- Add valid-time columns to tables for which the information in a row is delimited by time, and for
 which row information should be maintained, tracked, and manipulated in a time-aware fashion. 

##Bitemporal
- Is a **Transaction time** database, each record is an interval
- At every timestamp it represents a "Valid time" db

##Summary
- It is possible to change the past / future with valid time models, not with transaction time.
- A valid time column is most appropriate when changes to rows occur relatively infrequently. To
 represent attributes that change very frequently, such as a point of sale table, an event table is
 preferable to a valid-time table. 

#Footnotes
Transaction time
: time when data was written into the database

Valid time
: timespan the data is valid (e.g. credit card)

Bi-temporal database
: supports both transaction and valid time


