"""empty message

Revision ID: e8fecf9046d1
Revises: a868f1749096
Create Date: 2020-02-12 12:59:39.590333

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8fecf9046d1'
down_revision = 'a868f1749096'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('github_comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('github_api_comment_id', sa.Integer(), nullable=False),
    sa.Column('writer_id', sa.Integer(), nullable=False),
    sa.Column('comment_type', sa.String(length=30), nullable=False),
    sa.Column('parent_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('impact_score', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id', 'comment_type')
    )
    op.create_table('github_commits',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('repository_id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('committer_id', sa.Integer(), nullable=True),
    sa.Column('pusher_id', sa.Integer(), nullable=True),
    sa.Column('sha', sa.String(length=100), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('comment_count', sa.Integer(), nullable=True),
    sa.Column('insertions', sa.Integer(), nullable=True),
    sa.Column('deletions', sa.Integer(), nullable=True),
    sa.Column('edit_points', sa.Integer(), nullable=True),
    sa.Column('files_changed', sa.Integer(), nullable=True),
    sa.Column('impact_score', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('github_issues',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('github_api_issue_id', sa.Integer(), nullable=False),
    sa.Column('creator_id', sa.Integer(), nullable=False),
    sa.Column('closer_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('state', sa.String(length=20), nullable=True),
    sa.Column('comment_count', sa.Integer(), nullable=True),
    sa.Column('creation_impact_score', sa.Float(), nullable=True),
    sa.Column('closure_impact_score', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('github_pull_requests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('github_api_pr_id', sa.Integer(), nullable=False),
    sa.Column('repository_id', sa.Integer(), nullable=False),
    sa.Column('contributor_id', sa.Integer(), nullable=False),
    sa.Column('base_sha', sa.String(length=100), nullable=False),
    sa.Column('head_sha', sa.String(length=100), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('comment_count', sa.Integer(), nullable=True),
    sa.Column('commit_count', sa.Integer(), nullable=True),
    sa.Column('insertions', sa.Integer(), nullable=True),
    sa.Column('deletions', sa.Integer(), nullable=True),
    sa.Column('edit_points', sa.Integer(), nullable=True),
    sa.Column('files_changed', sa.Integer(), nullable=True),
    sa.Column('percent_churn', sa.Float(), nullable=False),
    sa.Column('is_merged', sa.Boolean(), nullable=False),
    sa.Column('impact_score', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('github_repos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=300), nullable=False),
    sa.Column('github_api_repo_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('owner', sa.String(length=100), nullable=True),
    sa.Column('organization', sa.String(length=100), nullable=True),
    sa.Column('is_private', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('github_repos')
    op.drop_table('github_pull_requests')
    op.drop_table('github_issues')
    op.drop_table('github_commits')
    op.drop_table('github_comments')
    # ### end Alembic commands ###
