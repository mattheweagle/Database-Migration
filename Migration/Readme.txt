Scripts handling migration and logging files related to migration



FILE DISCRIPTIONS:

generateRequests.py:
script for generating requests during migration. In its current configuration
25 requests are being sent to the APIs every second
Requests that add a new user/review/business are logged to requestAdds.txt
Requests that update or delete an entry are logged to requestUpdatesDeletes.txt
Logs are separated for easier testing

migration.py:
script for transferring the contents from MongoDB to PostgreSQL. Logs progress
to migrationLog.txt

transferRequests.py:
Runs all update and delete requests that were made during migration on Postgres
after contents are done being migrated by migration.py

migrationTest.py:
Checks every entry that was updated or deleted during migration across databases.
Also checks a random assortment of 10000 entries using a generated list of random
IDs
