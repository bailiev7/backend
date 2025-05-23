"""add user_role table and fk

Revision ID: fb8758098594
Revises: c481f1945748
Create Date: 2025-05-10 19:11:58.766303

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'fb8758098594'
down_revision: Union[str, None] = 'c481f1945748'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_role',
                    sa.Column('id', sa.UUID(), nullable=False),
                    sa.Column('role_name', sa.Enum(
                        'admin', 'default_user', name='roleenum'), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
#     op.drop_table('memberships')
#     op.drop_table('classes')
#     op.drop_table('trainers')
#     op.drop_table('clients')
#     op.drop_table('bookings')
#     op.add_column('users', sa.Column('role_id', sa.UUID(), nullable=True))
#     op.create_foreign_key(None, 'users', 'user_role', ['role_id'], ['id'])
#     # ### end Alembic commands ###


# def downgrade() -> None:
#     """Downgrade schema."""
#     # ### commands auto generated by Alembic - please adjust! ###
#     op.drop_constraint(None, 'users', type_='foreignkey')
#     op.drop_column('users', 'role_id')
#     op.create_table('bookings',
#                     sa.Column('booking_id', sa.INTEGER(),
#                               autoincrement=True, nullable=False),
#                     sa.Column('client_id', sa.INTEGER(),
#                               autoincrement=False, nullable=True),
#                     sa.Column('class_id', sa.INTEGER(),
#                               autoincrement=False, nullable=True),
#                     sa.Column('booking_date', postgresql.TIMESTAMP(), server_default=sa.text(
#                         'CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
#                     sa.ForeignKeyConstraint(
#                         ['class_id'], ['classes.class_id'], name='bookings_class_id_fkey'),
#                     sa.ForeignKeyConstraint(
#                         ['client_id'], ['clients.client_id'], name='bookings_client_id_fkey'),
#                     sa.PrimaryKeyConstraint('booking_id', name='bookings_pkey')
#                     )
#     op.create_table('clients',
#                     sa.Column('client_id', sa.INTEGER(), server_default=sa.text(
#                         "nextval('clients_client_id_seq'::regclass)"), autoincrement=True, nullable=False),
#                     sa.Column('name', sa.VARCHAR(length=100),
#                               autoincrement=False, nullable=True),
#                     sa.Column('phone', sa.VARCHAR(length=20),
#                               autoincrement=False, nullable=True),
#                     sa.Column('email', sa.VARCHAR(length=100),
#                               autoincrement=False, nullable=True),
#                     sa.PrimaryKeyConstraint('client_id', name='clients_pkey'),
#                     postgresql_ignore_search_path=False
#                     )
#     op.create_table('trainers',
#                     sa.Column('trainer_id', sa.INTEGER(), server_default=sa.text(
#                         "nextval('trainers_trainer_id_seq'::regclass)"), autoincrement=True, nullable=False),
#                     sa.Column('name', sa.VARCHAR(length=100),
#                               autoincrement=False, nullable=True),
#                     sa.Column('specialization', sa.VARCHAR(length=100),
#                               autoincrement=False, nullable=True),
#                     sa.Column('phone', sa.VARCHAR(length=20),
#                               autoincrement=False, nullable=True),
#                     sa.PrimaryKeyConstraint(
#                         'trainer_id', name='trainers_pkey'),
#                     postgresql_ignore_search_path=False
#                     )
#     op.create_table('classes',
#                     sa.Column('class_id', sa.INTEGER(),
#                               autoincrement=True, nullable=False),
#                     sa.Column('trainer_id', sa.INTEGER(),
#                               autoincrement=False, nullable=True),
#                     sa.Column('name', sa.VARCHAR(length=100),
#                               autoincrement=False, nullable=True),
#                     sa.Column('schedule', postgresql.TIMESTAMP(),
#                               autoincrement=False, nullable=True),
#                     sa.Column('duration', sa.INTEGER(),
#                               autoincrement=False, nullable=True),
#                     sa.ForeignKeyConstraint(
#                         ['trainer_id'], ['trainers.trainer_id'], name='classes_trainer_id_fkey'),
#                     sa.PrimaryKeyConstraint('class_id', name='classes_pkey')
#                     )
#     op.create_table('memberships',
#                     sa.Column('membership_id', sa.INTEGER(),
#                               autoincrement=True, nullable=False),
#                     sa.Column('client_id', sa.INTEGER(),
#                               autoincrement=False, nullable=True),
#                     sa.Column('name', sa.VARCHAR(length=50),
#                               autoincrement=False, nullable=True),
#                     sa.Column('duration', sa.INTEGER(),
#                               autoincrement=False, nullable=True),
#                     sa.Column('price', sa.DOUBLE_PRECISION(precision=53),
#                               autoincrement=False, nullable=True),
#                     sa.ForeignKeyConstraint(
#                         ['client_id'], ['clients.client_id'], name='memberships_client_id_fkey'),
#                     sa.PrimaryKeyConstraint(
#                         'membership_id', name='memberships_pkey')
#                     )
