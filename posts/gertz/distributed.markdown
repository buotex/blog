{
  "title": "Distributed Database Management System",
  "date": "2014-01-23",
  "categories": [
   "database" 
  ],
  "tags": [
    "data structure"
  ]
}

#Fragmentation
: Partitinoing of global relation R into fragments R_1, R_2 etc.

- primary horizontal
- derived horizontal
- vertical
- hybrid

> Access patterns and application behavior must be known

primary horizontal
: Split on attributes, i.e. attr > 50

derived horizontal
: semi-join to fragments which were split up according to primary horizontal
: works if you want to split on foreign keys 
: allows *SIMPLE JOIN*, only accordings parts have to be joined to each other, 1:1 relation




#Order of transactions
- add <prepare> to server-log
- either <no> or <ready> on client logs
- <commit> or <abort> on server-log