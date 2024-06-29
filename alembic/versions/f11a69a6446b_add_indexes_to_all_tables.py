"""Add indexes to all tables

Revision ID: f11a69a6446b
Revises: 9ebfcd112d56
Create Date: 2024-06-09 10:36:41.464743

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

def index_exists(index_name, table_name):
    conn = op.get_bind()
    inspector = sa.inspect(conn)
    indexes = [idx['name'] for idx in inspector.get_indexes(table_name)]
    return index_name in indexes


# revision identifiers, used by Alembic.
revision: str = 'f11a69a6446b'
down_revision: Union[str, None] = '9ebfcd112d56'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Product1 table indexes
    if not index_exists('ix_pars_table1_name', 'pars_table1'):
        op.create_index('ix_pars_table1_name', 'pars_table1', ['name'], unique=False)
    if not index_exists('ix_pars_table1_brand_name', 'pars_table1'):
        op.create_index('ix_pars_table1_brand_name', 'pars_table1', ['brand_name'], unique=False)
    if not index_exists('ix_pars_table1_product_id', 'pars_table1'):
        op.create_index('ix_pars_table1_product_id', 'pars_table1', ['product_id'], unique=True)
    if not index_exists('ix_pars_table1_price', 'pars_table1'):
        op.create_index('ix_pars_table1_price', 'pars_table1', ['price'], unique=False)
    if not index_exists('ix_pars_table1_url_name', 'pars_table1'):
        op.create_index('ix_pars_table1_url_name', 'pars_table1', ['url_name'], unique=False)

    # Product2 table indexes
    if not index_exists('ix_pars_table2_name', 'pars_table2'):
        op.create_index('ix_pars_table2_name', 'pars_table2', ['name'], unique=False)
    if not index_exists('ix_pars_table2_brand_name', 'pars_table2'):
        op.create_index('ix_pars_table2_brand_name', 'pars_table2', ['brand_name'], unique=False)
    if not index_exists('ix_pars_table2_product_id', 'pars_table2'):
        op.create_index('ix_pars_table2_product_id', 'pars_table2', ['product_id'], unique=True)
    if not index_exists('ix_pars_table2_price', 'pars_table2'):
        op.create_index('ix_pars_table2_price', 'pars_table2', ['price'], unique=False)
    if not index_exists('ix_pars_table2_url_name', 'pars_table2'):
        op.create_index('ix_pars_table2_url_name', 'pars_table2', ['url_name'], unique=False)

    # ComparedProductsInstaBuy table indexes
    if not index_exists('ix_compared_products_insta_buy_name', 'compared_products_insta_buy'):
        op.create_index('ix_compared_products_insta_buy_name', 'compared_products_insta_buy', ['name'], unique=False)
    if not index_exists('ix_compared_products_insta_buy_brand_name', 'compared_products_insta_buy'):
        op.create_index('ix_compared_products_insta_buy_brand_name', 'compared_products_insta_buy', ['brand_name'], unique=False)
    if not index_exists('ix_compared_products_insta_buy_product_id', 'compared_products_insta_buy'):
        op.create_index('ix_compared_products_insta_buy_product_id', 'compared_products_insta_buy', ['product_id'], unique=True)
    if not index_exists('ix_compared_products_insta_buy_price', 'compared_products_insta_buy'):
        op.create_index('ix_compared_products_insta_buy_price', 'compared_products_insta_buy', ['price'], unique=False)
    if not index_exists('ix_compared_products_insta_buy_url_name', 'compared_products_insta_buy'):
        op.create_index('ix_compared_products_insta_buy_url_name', 'compared_products_insta_buy', ['url_name'], unique=False)

    # ComparedProductsInstaBuyDuplicate table indexes
    if not index_exists('ix_compared_products_insta_buy_duplicate_name', 'compared_products_insta_buy_duplicate'):
        op.create_index('ix_compared_products_insta_buy_duplicate_name', 'compared_products_insta_buy_duplicate', ['name'], unique=False)
    if not index_exists('ix_compared_products_insta_buy_duplicate_brand_name', 'compared_products_insta_buy_duplicate'):
        op.create_index('ix_compared_products_insta_buy_duplicate_brand_name', 'compared_products_insta_buy_duplicate', ['brand_name'], unique=False)
    if not index_exists('ix_compared_products_insta_buy_duplicate_product_id', 'compared_products_insta_buy_duplicate'):
        op.create_index('ix_compared_products_insta_buy_duplicate_product_id', 'compared_products_insta_buy_duplicate', ['product_id'], unique=True)
    if not index_exists('ix_compared_products_insta_buy_duplicate_price', 'compared_products_insta_buy_duplicate'):
        op.create_index('ix_compared_products_insta_buy_duplicate_price', 'compared_products_insta_buy_duplicate', ['price'], unique=False)
    if not index_exists('ix_compared_products_insta_buy_duplicate_url_name', 'compared_products_insta_buy_duplicate'):
        op.create_index('ix_compared_products_insta_buy_duplicate_url_name', 'compared_products_insta_buy_duplicate', ['url_name'], unique=False)

    # ComparedProductsInstaBuyDuplicateTelegram table indexes
    if not index_exists('ix_cpidt_name', 'compared_products_insta_buy_duplicate_telegram'):
        op.create_index('ix_cpidt_name', 'compared_products_insta_buy_duplicate_telegram', ['name'], unique=False)
    if not index_exists('ix_cpidt_brand_name', 'compared_products_insta_buy_duplicate_telegram'):
        op.create_index('ix_cpidt_brand_name', 'compared_products_insta_buy_duplicate_telegram', ['brand_name'], unique=False)
    if not index_exists('ix_cpidt_product_id', 'compared_products_insta_buy_duplicate_telegram'):
        op.create_index('ix_cpidt_product_id', 'compared_products_insta_buy_duplicate_telegram', ['product_id'], unique=True)
    if not index_exists('ix_cpidt_price', 'compared_products_insta_buy_duplicate_telegram'):
        op.create_index('ix_cpidt_price', 'compared_products_insta_buy_duplicate_telegram', ['price'], unique=False)
    if not index_exists('ix_cpidt_url_name', 'compared_products_insta_buy_duplicate_telegram'):
        op.create_index('ix_cpidt_url_name', 'compared_products_insta_buy_duplicate_telegram', ['url_name'], unique=False)

    # ComparedProductsConfirmPurchase table indexes
    if not index_exists('ix_cpcp_name', 'compared_products_confirm_purchase'):
        op.create_index('ix_cpcp_name', 'compared_products_confirm_purchase', ['name'], unique=False)
    if not index_exists('ix_cpcp_brand_name', 'compared_products_confirm_purchase'):
        op.create_index('ix_cpcp_brand_name', 'compared_products_confirm_purchase', ['brand_name'], unique=False)
    if not index_exists('ix_cpcp_product_id', 'compared_products_confirm_purchase'):
        op.create_index('ix_cpcp_product_id', 'compared_products_confirm_purchase', ['product_id'], unique=True)
    if not index_exists('ix_cpcp_price', 'compared_products_confirm_purchase'):
        op.create_index('ix_cpcp_price', 'compared_products_confirm_purchase', ['price'], unique=False)
    if not index_exists('ix_cpcp_url_name', 'compared_products_confirm_purchase'):
        op.create_index('ix_cpcp_url_name', 'compared_products_confirm_purchase', ['url_name'], unique=False)

    # ComparedProductsConfirmPurchaseDuplicate table indexes
    if not index_exists('ix_cpcpd_name', 'compared_products_confirm_purchase_duplicate'):
        op.create_index('ix_cpcpd_name', 'compared_products_confirm_purchase_duplicate', ['name'], unique=False)
    if not index_exists('ix_cpcpd_brand_name', 'compared_products_confirm_purchase_duplicate'):
        op.create_index('ix_cpcpd_brand_name', 'compared_products_confirm_purchase_duplicate', ['brand_name'], unique=False)
    if not index_exists('ix_cpcpd_product_id', 'compared_products_confirm_purchase_duplicate'):
        op.create_index('ix_cpcpd_product_id', 'compared_products_confirm_purchase_duplicate', ['product_id'], unique=True)
    if not index_exists('ix_cpcpd_price', 'compared_products_confirm_purchase_duplicate'):
        op.create_index('ix_cpcpd_price', 'compared_products_confirm_purchase_duplicate', ['price'], unique=False)
    if not index_exists('ix_cpcpd_url_name', 'compared_products_confirm_purchase_duplicate'):
        op.create_index('ix_cpcpd_url_name', 'compared_products_confirm_purchase_duplicate', ['url_name'], unique=False)

    # ComparedProductsConfirmPurchaseDuplicateTelegram table indexes
    if not index_exists('ix_cpcpdt_name', 'compared_products_confirm_purchase_duplicate_telegram'):
        op.create_index('ix_cpcpdt_name', 'compared_products_confirm_purchase_duplicate_telegram', ['name'], unique=False)
    if not index_exists('ix_cpcpdt_brand_name', 'compared_products_confirm_purchase_duplicate_telegram'):
        op.create_index('ix_cpcpdt_brand_name', 'compared_products_confirm_purchase_duplicate_telegram', ['brand_name'], unique=False)
    if not index_exists('ix_cpcpdt_product_id', 'compared_products_confirm_purchase_duplicate_telegram'):
        op.create_index('ix_cpcpdt_product_id', 'compared_products_confirm_purchase_duplicate_telegram', ['product_id'], unique=True)
    if not index_exists('ix_cpcpdt_price', 'compared_products_confirm_purchase_duplicate_telegram'):
        op.create_index('ix_cpcpdt_price', 'compared_products_confirm_purchase_duplicate_telegram', ['price'], unique=False)
    if not index_exists('ix_cpcpdt_url_name', 'compared_products_confirm_purchase_duplicate_telegram'):
        op.create_index('ix_cpcpdt_url_name', 'compared_products_confirm_purchase_duplicate_telegram', ['url_name'], unique=False)

    # NewProduct table indexes
    if not index_exists('ix_np_name', 'new_product_table'):
        op.create_index('ix_np_name', 'new_product_table', ['name'], unique=False)
    if not index_exists('ix_np_brand_name', 'new_product_table'):
        op.create_index('ix_np_brand_name', 'new_product_table', ['brand_name'], unique=False)
    if not index_exists('ix_np_product_id', 'new_product_table'):
        op.create_index('ix_np_product_id', 'new_product_table', ['product_id'], unique=True)
    if not index_exists('ix_np_price', 'new_product_table'):
        op.create_index('ix_np_price', 'new_product_table', ['price'], unique=False)
    if not index_exists('ix_np_url_name', 'new_product_table'):
        op.create_index('ix_np_url_name', 'new_product_table', ['url_name'], unique=False)

    # ParserStatus table indexes
    if not index_exists('ix_ps_parser_number', 'parsers_status'):
        op.create_index('ix_ps_parser_number', 'parsers_status', ['parser_number'], unique=False)
    if not index_exists('ix_ps_status', 'parsers_status'):
        op.create_index('ix_ps_status', 'parsers_status', ['status'], unique=False)
    if not index_exists('ix_ps_category', 'parsers_status'):
        op.create_index('ix_ps_category', 'parsers_status', ['category'], unique=False)


def downgrade() -> None:
    # Drop indexes for Product1 table
    op.drop_index('ix_pars_table1_name', table_name='pars_table1')
    op.drop_index('ix_pars_table1_brand_name', table_name='pars_table1')
    op.drop_index('ix_pars_table1_product_id', table_name='pars_table1')
    op.drop_index('ix_pars_table1_price', table_name='pars_table1')
    op.drop_index('ix_pars_table1_url_name', table_name='pars_table1')

    # Drop indexes for Product2 table
    op.drop_index('ix_pars_table2_name', table_name='pars_table2')
    op.drop_index('ix_pars_table2_brand_name', table_name='pars_table2')
    op.drop_index('ix_pars_table2_product_id', table_name='pars_table2')
    op.drop_index('ix_pars_table2_price', table_name='pars_table2')
    op.drop_index('ix_pars_table2_url_name', table_name='pars_table2')

    # Drop indexes for ComparedProductsInstaBuy table
    op.drop_index('ix_compared_products_insta_buy_name', table_name='compared_products_insta_buy')
    op.drop_index('ix_compared_products_insta_buy_brand_name', table_name='compared_products_insta_buy')
    op.drop_index('ix_compared_products_insta_buy_product_id', table_name='compared_products_insta_buy')
    op.drop_index('ix_compared_products_insta_buy_price', table_name='compared_products_insta_buy')
    op.drop_index('ix_compared_products_insta_buy_url_name', table_name='compared_products_insta_buy')

    # Drop indexes for ComparedProductsInstaBuyDuplicate table
    op.drop_index('ix_compared_products_insta_buy_duplicate_name', table_name='compared_products_insta_buy_duplicate')
    op.drop_index('ix_compared_products_insta_buy_duplicate_brand_name', table_name='compared_products_insta_buy_duplicate')
    op.drop_index('ix_compared_products_insta_buy_duplicate_product_id', table_name='compared_products_insta_buy_duplicate')
    op.drop_index('ix_compared_products_insta_buy_duplicate_price', table_name='compared_products_insta_buy_duplicate')
    op.drop_index('ix_compared_products_insta_buy_duplicate_url_name', table_name='compared_products_insta_buy_duplicate')

    # Drop indexes for ComparedProductsInstaBuyDuplicateTelegram table
    op.drop_index('ix_cpidt_name', table_name='compared_products_insta_buy_duplicate_telegram')
    op.drop_index('ix_cpidt_brand_name', table_name='compared_products_insta_buy_duplicate_telegram')
    op.drop_index('ix_cpidt_product_id', table_name='compared_products_insta_buy_duplicate_telegram')
    op.drop_index('ix_cpidt_price', table_name='compared_products_insta_buy_duplicate_telegram')
    op.drop_index('ix_cpidt_url_name', table_name='compared_products_insta_buy_duplicate_telegram')

    # Drop indexes for ComparedProductsConfirmPurchase table
    op.drop_index('ix_cpcp_name', table_name='compared_products_confirm_purchase')
    op.drop_index('ix_cpcp_brand_name', table_name='compared_products_confirm_purchase')
    op.drop_index('ix_cpcp_product_id', table_name='compared_products_confirm_purchase')
    op.drop_index('ix_cpcp_price', table_name='compared_products_confirm_purchase')
    op.drop_index('ix_cpcp_url_name', table_name='compared_products_confirm_purchase')

    # Drop indexes for ComparedProductsConfirmPurchaseDuplicate table
    op.drop_index('ix_cpcpd_name', table_name='compared_products_confirm_purchase_duplicate')
    op.drop_index('ix_cpcpd_brand_name', table_name='compared_products_confirm_purchase_duplicate')
    op.drop_index('ix_cpcpd_product_id', table_name='compared_products_confirm_purchase_duplicate')
    op.drop_index('ix_cpcpd_price', table_name='compared_products_confirm_purchase_duplicate')
    op.drop_index('ix_cpcpd_url_name', table_name='compared_products_confirm_purchase_duplicate')

    # Drop indexes for ComparedProductsConfirmPurchaseDuplicateTelegram table
    op.drop_index('ix_cpcpdt_name', table_name='compared_products_confirm_purchase_duplicate_telegram')
    op.drop_index('ix_cpcpdt_brand_name', table_name='compared_products_confirm_purchase_duplicate_telegram')
    op.drop_index('ix_cpcpdt_product_id', table_name='compared_products_confirm_purchase_duplicate_telegram')
    op.drop_index('ix_cpcpdt_price', table_name='compared_products_confirm_purchase_duplicate_telegram')
    op.drop_index('ix_cpcpdt_url_name', table_name='compared_products_confirm_purchase_duplicate_telegram')

    # Drop indexes for NewProduct table
    op.drop_index('ix_np_name', table_name='new_product_table')
    op.drop_index('ix_np_brand_name', table_name='new_product_table')
    op.drop_index('ix_np_product_id', table_name='new_product_table')
    op.drop_index('ix_np_price', table_name='new_product_table')
    op.drop_index('ix_np_url_name', table_name='new_product_table')

    # Drop indexes for ParserStatus table
    op.drop_index('ix_ps_parser_number', table_name='parsers_status')
    op.drop_index('ix_ps_status', table_name='parsers_status')
    op.drop_index('ix_ps_category', table_name='parsers_status')
