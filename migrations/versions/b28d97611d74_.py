"""empty message

Revision ID: b28d97611d74
Revises: cd0b685103a7
Create Date: 2019-11-24 16:13:17.041072

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b28d97611d74'
down_revision = 'cd0b685103a7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('slack_user_events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('slack_user_id', sa.Integer(), nullable=False),
    sa.Column('raw_slack_event_id', sa.Integer(), nullable=True),
    sa.Column('slack_event_api_id', sa.String(length=100), nullable=False),
    sa.Column('event_datetime', sa.DateTime(), nullable=False),
    sa.Column('last_updated', sa.DateTime(), nullable=False),
    sa.Column('slack_event_type', sa.String(length=100), nullable=False),
    sa.Column('slack_event_subtype', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['raw_slack_event_id'], ['raw_slack_events.id'], ),
    sa.ForeignKeyConstraint(['slack_user_id'], ['slack_users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('slack_user_events')
    # ### end Alembic commands ###
