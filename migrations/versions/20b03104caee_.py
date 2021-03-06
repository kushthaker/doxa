"""empty message

Revision ID: 20b03104caee
Revises: 85945c7ca481
Create Date: 2020-02-21 12:10:18.258957

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20b03104caee'
down_revision = '85945c7ca481'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('activity_report_unique_user_datetime', 'activity_report_rows', ['user_id', 'datetime_utc'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('activity_report_unique_user_datetime', table_name='activity_report_rows')
    # ### end Alembic commands ###
