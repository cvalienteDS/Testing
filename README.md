# testing_with_sqlite
![chart drawio](https://user-images.githubusercontent.com/65561135/178716843-042001e8-dbda-4dfa-8771-f109adf09ebf.png)
The code connects to a SQLite DB, fetch data and get some summary queries. Then, format the output for specified use case.

DB is a dummy dimensional model with 2 tables:
- visits (fact table)
- products (dimension)

## Testing
Set up a "in memory" SQLite mock database to isolate from production DB

An external SQL script called "data.db.sql" is executed to populate mock database
