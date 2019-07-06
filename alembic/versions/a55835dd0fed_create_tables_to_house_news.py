"""Create tables to house news.

Revision ID: a55835dd0fed
Revises: 
Create Date: 2019-07-06 13:58:07.952324

"""
from alembic import op
import sqlalchemy as sa
import datetime


# revision identifiers, used by Alembic.
revision = 'a55835dd0fed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'sources',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('text_id', sa.String, nullable=True),
        sa.Column('name', sa.String, nullable=True),
        sa.Column('description', sa.String, nullable=True),
        sa.Column('url', sa.String, nullable=True),
        sa.Column('category', sa.String, nullable=True),
        sa.Column('language', sa.String, nullable=True),
        sa.Column('country', sa.String, nullable=True),
        sa.Column(
            'created_at',
            sa.DateTime,
            default=datetime.datetime.utcnow,
            nullable=False
        ),
        sa.Column('created_by', sa.String, default='netlbot', nullable=True),
        sa.Column('updated_at', sa.DateTime, nullable=True),
        sa.Column('updated_by', sa.String, nullable=True),
    )

    op.create_table(
        'articles',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('source_id', sa.Integer, sa.ForeignKey("sources.id"), nullable=True),
        sa.Column('author', sa.String, nullable=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('description', sa.String, nullable=True),
        sa.Column('url', sa.String, nullable=False),
        sa.Column('url_to_image', sa.String, nullable=True),
        sa.Column('published_at', sa.DateTime, nullable=True),
        sa.Column('content', sa.String, nullable=True),
        sa.Column(
            'created_at',
            sa.DateTime,
            default=datetime.datetime.utcnow,
            nullable=False
        ),
        sa.Column('created_by', sa.String, default='netlbot', nullable=True),
        sa.Column('updated_at', sa.DateTime, nullable=True),
        sa.Column('updated_by', sa.String, nullable=True),
    )

def downgrade():
    op.drop_table('articles')
    op.drop_table('sources')

