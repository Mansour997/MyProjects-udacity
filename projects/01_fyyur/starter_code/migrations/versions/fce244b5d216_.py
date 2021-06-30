"""empty message

Revision ID: fce244b5d216
Revises: 4fc298c7670a
Create Date: 2021-06-24 18:47:23.836425

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'fce244b5d216'
down_revision = '4fc298c7670a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('shows', 'venue_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('shows', 'artist_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('shows', 'id')
    op.drop_column('shows', 'start_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shows', sa.Column('start_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('shows', sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.alter_column('shows', 'artist_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('shows', 'venue_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###