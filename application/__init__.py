# this makes certain things importable via from application.folder_name import thing_in_folder

'''
dev setup commands:
Install PostgreSQL 11.5
(on MacOS use Homebrew -> brew install postgresql@11.5)
(not sure how on PC, but there is certainly an easy way)
start PostgreSQL -> brew services start postgresql
Then:
createdb doxa-db-dev
pip install -r requirements.txt
python manage.py db migrate (if you have new database changes)
Then inspect the new migration! Does it look okay?
python manage.py db upgrade (upgrades your database with new models)

you can query / inspect your database using:
psql -d doxa-db-dev

if the migration does not work, you can run 
python manage.py db downgrade
to undo it.

PR any new migrations
'''
