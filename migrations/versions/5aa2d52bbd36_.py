"""empty message

Revision ID: 5aa2d52bbd36
Revises: c1186007f775
Create Date: 2017-01-16 15:38:35.512961

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5aa2d52bbd36'
down_revision = 'c1186007f775'
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dog', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'dog', 'user', ['user_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'dog', type_='foreignkey')
    op.drop_column('dog', 'user_id')
    ### end Alembic commands ###