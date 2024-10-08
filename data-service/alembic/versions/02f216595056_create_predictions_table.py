"""Create predictions table

Revision ID: 02f216595056
Revises: 
Create Date: 2024-10-01 16:04:50.562684

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '02f216595056'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('predictions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('input_data', sa.String(), nullable=True),
    sa.Column('prediction', sa.Integer(), nullable=True),
    sa.Column('probabilities', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_predictions_id'), 'predictions', ['id'], unique=False)
    op.create_index(op.f('ix_predictions_input_data'), 'predictions', ['input_data'], unique=False)
    op.create_index(op.f('ix_predictions_user_id'), 'predictions', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_predictions_user_id'), table_name='predictions')
    op.drop_index(op.f('ix_predictions_input_data'), table_name='predictions')
    op.drop_index(op.f('ix_predictions_id'), table_name='predictions')
    op.drop_table('predictions')
    # ### end Alembic commands ###
