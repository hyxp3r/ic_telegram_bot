"""empty message

Revision ID: 06fd7ccdc37c
Revises: 
Create Date: 2024-03-10 17:14:20.477058

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '06fd7ccdc37c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('action',
    sa.Column('telegram_id', sa.String(length=255), nullable=False),
    sa.Column('action', sa.String(length=255), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_action'))
    )
    op.create_table('student',
    sa.Column('telegram_id', sa.String(length=255), nullable=False),
    sa.Column('fio', sa.String(length=255), nullable=False),
    sa.Column('personal_number', sa.String(length=10), nullable=False),
    sa.Column('form', sa.String(length=10), nullable=False),
    sa.Column('group', sa.String(length=100), nullable=False),
    sa.Column('program', sa.String(length=100), nullable=False),
    sa.Column('api_key', sa.String(length=255), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_student'))
    )
    op.create_index(op.f('ix_student_personal_number'), 'student', ['personal_number'], unique=False)
    op.create_index(op.f('ix_student_telegram_id'), 'student', ['telegram_id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_student_telegram_id'), table_name='student')
    op.drop_index(op.f('ix_student_personal_number'), table_name='student')
    op.drop_table('student')
    op.drop_table('action')
    # ### end Alembic commands ###
