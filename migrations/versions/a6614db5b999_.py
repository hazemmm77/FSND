"""empty message

Revision ID: a6614db5b999
Revises: b4f49407f96d
Create Date: 2021-02-18 13:38:19.385471

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6614db5b999'
down_revision = 'b4f49407f96d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venues', sa.Column('website', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venues', 'website')
    # ### end Alembic commands ###
