"""empty message

Revision ID: f2d064800e76
Revises: acedd8d0829b
Create Date: 2020-03-07 19:15:31.805103

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2d064800e76'
down_revision = 'acedd8d0829b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('github_comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('github_api_comment_id', sa.Integer(), nullable=False),
    sa.Column('github_api_author_id', sa.Integer(), nullable=False),
    sa.Column('comment_type', sa.String(length=30), nullable=False),
    sa.Column('github_api_parent_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('github_api_written_at', sa.DateTime(), nullable=False),
    sa.Column('github_api_edited_at', sa.DateTime(), nullable=False),
    sa.Column('impact_score', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('github_comments')
    # ### end Alembic commands ###