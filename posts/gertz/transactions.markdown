{
  "title": "Transactions",
  "date": "2014-01-23",
  "categories": [
   "database" 
  ],
  "tags": [
    "data structure"
  ]
}

A transaction is a sequence of one or more SQL operations treated as a unit

On "commit" a transaction ends and a nother one starts

The transaction is executed either all or nothing.

#ACID

Isolation
: Transaction may interleave, but then their result has to be equivalent to *some* sequential ordering of all these transactions


Transaction Rollback
: Undoes partial effects of transaction
: on failure or client reversal

Read Uncommited
- allowed to read data that was changed in the middle of another transaction

Read Commited
- only read commited data
- may still differ from serial order

Repeatable Read


#Serializability
- Is a history serializable?
- Create graph for serialization
- Possible if acyclic
({{urls.media}}/gertz/db/Kapitel11.pdf)

