"""1.3.2

Revision ID: 57c4146172c2
Revises: eb3437042cc8
Create Date: 2024-04-05 13:50:38.217641

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57c4146172c2'
down_revision = 'eb3437042cc8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('SITE_BRUSH_TASK', sa.Column('FRACTION_RULE', sa.Text(), nullable=True))
    op.add_column('SITE_BRUSH_TASK', sa.Column('BRUSHTASK_FREE_LIMIT_SPEED', sa.Text(), nullable=True))
    op.add_column('SITE_BRUSH_TORRENTS', sa.Column('FREE_DEADLINE', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('SITE_BRUSH_TORRENTS', 'FREE_DEADLINE')
    op.drop_column('SITE_BRUSH_TASK', 'BRUSHTASK_FREE_LIMIT_SPEED')
    op.drop_column('SITE_BRUSH_TASK', 'FRACTION_RULE')
    # ### end Alembic commands ###