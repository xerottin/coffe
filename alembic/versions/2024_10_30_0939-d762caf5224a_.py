"""empty message

Revision ID: d762caf5224a
Revises: 
Create Date: 2024-10-30 09:39:08.995405

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd762caf5224a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('name', 'id')
    )
    op.create_index(op.f('ix_admin_id'), 'admin', ['id'], unique=False)
    op.create_table('company',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('owner', sa.String(), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_company_id'), 'company', ['id'], unique=False)
    op.create_table('user',
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_table('client',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_client_id'), 'client', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_client_id'), table_name='client')
    op.drop_table('client')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_company_id'), table_name='company')
    op.drop_table('company')
    op.drop_index(op.f('ix_admin_id'), table_name='admin')
    op.drop_table('admin')
    # ### end Alembic commands ###