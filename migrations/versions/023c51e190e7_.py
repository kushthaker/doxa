"""empty message

Revision ID: 023c51e190e7
Revises: 206841683ce2
Create Date: 2019-10-22 23:55:12.631115

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '023c51e190e7'
down_revision = '206841683ce2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('slack_teams',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('api_scope', sa.String(length=1000), nullable=True),
    sa.Column('install_slack_user_id', sa.String(length=100), nullable=True),
    sa.Column('slack_team_id', sa.String(length=100), nullable=False),
    sa.Column('slack_team_name', sa.String(length=100), nullable=False),
    sa.Column('api_access_token', sa.String(length=100), nullable=True),
    sa.Column('datetime_authenticated', sa.DateTime(), nullable=True),
    sa.Column('last_updated', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slack_team_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('slack_teams')
    # ### end Alembic commands ###
