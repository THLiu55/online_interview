"""empty message

Revision ID: 7134388adcc7
Revises: 
Create Date: 2022-09-26 15:20:28.820064

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7134388adcc7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('email_captcha',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.CHAR(length=100), nullable=False),
    sa.Column('captcha', sa.CHAR(length=10), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('user',
    sa.Column('user_name', sa.CHAR(length=200), nullable=False),
    sa.Column('user_password', sa.CHAR(length=200), nullable=False),
    sa.Column('user_email', sa.CHAR(length=200), nullable=False),
    sa.PrimaryKeyConstraint('user_email'),
    sa.UniqueConstraint('user_email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('email_captcha')
    # ### end Alembic commands ###
