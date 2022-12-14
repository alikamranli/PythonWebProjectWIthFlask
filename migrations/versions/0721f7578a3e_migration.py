"""migration

Revision ID: 0721f7578a3e
Revises: 
Create Date: 2022-08-17 21:50:19.947913

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0721f7578a3e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('brand', sa.String(length=100), nullable=True))
    op.add_column('products', sa.Column('model', sa.String(length=100), nullable=True))
    op.add_column('products', sa.Column('description', sa.String(length=200), nullable=True))
    op.drop_column('products', 'productName')
    op.drop_column('products', 'add_date')
    op.drop_column('products', 'is_active')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('is_active', sa.BOOLEAN(), nullable=True))
    op.add_column('products', sa.Column('add_date', sa.DATETIME(), nullable=True))
    op.add_column('products', sa.Column('productName', sa.INTEGER(), nullable=True))
    op.drop_column('products', 'description')
    op.drop_column('products', 'model')
    op.drop_column('products', 'brand')
    # ### end Alembic commands ###
