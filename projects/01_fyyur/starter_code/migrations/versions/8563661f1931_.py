"""empty message

Revision ID: 8563661f1931
Revises: b08a69d94250
Create Date: 2021-06-29 14:15:21.486470

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8563661f1931'
down_revision = 'b08a69d94250'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shows')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shows',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False)
    )
    # ### end Alembic commands ###