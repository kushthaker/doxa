"""empty message

Revision ID: f7001c500037
Revises: cd0b685103a7
Create Date: 2019-10-30 22:31:29.133387

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7001c500037'
down_revision = 'cd0b685103a7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('slack_users', sa.Column('is_bot', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('slack_users', 'is_bot')
    # ### end Alembic commands ###
