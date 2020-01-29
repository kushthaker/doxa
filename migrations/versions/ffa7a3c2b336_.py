"""empty message

Revision ID: ffa7a3c2b336
Revises: e8be42e6bcb5
Create Date: 2020-01-29 14:48:26.655593

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ffa7a3c2b336'
down_revision = 'e8be42e6bcb5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('github_users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('github_oauth_access_token', sa.String(length=200), nullable=True),
    sa.Column('github_email_address', sa.String(length=300), nullable=True),
    sa.Column('github_username', sa.String(length=100), nullable=True),
    sa.Column('is_authenticated', sa.Boolean(), nullable=False),
    sa.Column('is_deleted_on_github', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('github_users')
    # ### end Alembic commands ###
