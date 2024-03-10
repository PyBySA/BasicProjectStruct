from typing import Optional

from sqlmodel import SQLModel, Field
import datetime
import cred
import cred


class InventoryTableMaster(SQLModel, table=True):
    __tablename__ = "inventory_master_status"

    vendor_name: str = Field(max_length=100, default=cred.vendor_name, primary_key=False)
    product_name: Optional[str] = Field(max_length=255, nullable=True)
    product_sku: str = Field(max_length=100, primary_key=True)
    product_status: str = Field(max_length=1000)
    product_details_int1: Optional[int] = None
    product_details_int2: Optional[int] = None
    product_details_int3: Optional[int] = None
    product_details_str1: Optional[str] = Field(max_length=255, nullable=True)
    product_details_str2: Optional[str] = Field(max_length=255, nullable=True)
    product_details_str3: Optional[str] = Field(max_length=255, nullable=True)
    inventory_availability: Optional[str] = Field(max_length=255, nullable=True)
    inventory_qtyvalue: Optional[int] = None
    inventory_qtyavailabledate: Optional[str] = None  # Assuming timestamp is stored as a string
    inventory_ref1: Optional[str] = Field(max_length=255, nullable=True)
    inventory_ref2: Optional[str] = Field(max_length=255, nullable=True)
    inventory_ref3: Optional[str] = Field(max_length=255, nullable=True)
    created_by: str = Field(max_length=100)
    updated_by: str = Field(max_length=100)
    updated_at: str = Field(default=None)  # Assuming timestamp is stored as a string
    created_at: str = Field(default=None)  # Assuming timestamp is stored as a string


class CreationProductDescription(SQLModel, table=True):
    __tablename__ = "creation_product_description"
    __table_args__ = {"schema": cred.db_schema}  # Specify the schema name

    product_id: str = Field(primary_key=True, index=True, max_length=100)
    description: str = Field(max_length=50000, nullable=True)
    warranty: str = Field(max_length=50000, nullable=True)
    shippinginformations: str = Field(max_length=50000, nullable=True)
    features: str = Field(max_length=50000, nullable=True)
    specification_link_id: str = Field(max_length=100, nullable=True)
    createdby: str = Field(max_length=100)
    modifiedby: str = Field(max_length=100)
    createdat: str = ''
    modifiedat: str = ''


class CreationProductSpecification(SQLModel, table=True):
    __tablename__ = "creation_product_specification"
    __table_args__ = {"schema": cred.db_schema}

    link_id: str = Field(max_length=100, primary_key=True)
    key: str = Field(max_length=100, primary_key=True)
    value: str = Field(max_length=100, primary_key=True)


class CreationProduct(SQLModel, table=True):
    __tablename__ = "creation_product"
    __table_args__ = {"schema": cred.db_schema}
    id: str = Field(primary_key=True)
    title: str = None
    body_html: str = None
    vendor: str = None
    product_type: str = None
    created_at: str = None
    handle: str = None
    updated_at: str = None
    published_at: str = None
    template_suffix: str = None
    status: str = None
    published_scope: str = None
    tags: str = None
    admin_graphql_api_id: str = None
    variants_link_id: str = None
    options_link_id: str = None
    images_link_id: str = None
    image_id: str = None
    metafields_link_id: str = None
    createdby: str
    modifiedby: str
    createdat: str = ''
    modifiedat: str = ''


class CreationProductImage(SQLModel, table=True):
    __tablename__ = "creation_product_images"
    __table_args__ = {"schema": cred.db_schema}

    link_id: str = Field(primary_key=True)
    product_id: Optional[str] = None
    id: str = Field(primary_key=True)
    position: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    alt: Optional[str] = None
    width: Optional[str] = None
    height: Optional[str] = None
    vendor_src: Optional[str] = None
    src: Optional[str] = None
    variant_ids: Optional[str] = None
    admin_graphql_api_id: Optional[str] = None
    createdby: str
    modifiedby: str
    createdat: str
    modifiedat: str


class CreationProductOptions(SQLModel, table=True):
    __tablename__ = "creation_product_options"
    __table_args__ = {"schema": cred.db_schema}
    link_id: str = Field(primary_key=True, max_length=100)
    id: Optional[str] = Field(primary_key=True, max_length=500)
    product_id: Optional[str] = Field(max_length=500, default=None)
    name: Optional[str] = Field(max_length=500, default=None)
    position: Optional[str] = Field(max_length=500, default=None)
    values: Optional[str] = Field(max_length=5000, default=None)
    createdby: str = Field(max_length=100)
    modifiedby: str = Field(max_length=100)
    createdat: str
    modifiedat: str


class CreationProductVariants(SQLModel, table=True):
    __tablename__ = "creation_product_variants"
    __table_args__ = {"schema": cred.db_schema}
    link_id: str = Field(primary_key=True, max_length=100)
    id: str = Field(primary_key=True, max_length=100)
    product_id: Optional[str] = Field(max_length=500, default=None)
    title: Optional[str] = Field(max_length=500, default=None)
    price: Optional[str] = Field(primary_key=True,max_length=500, default=None)
    sku: Optional[str] = Field(max_length=500, default=None)
    position_: Optional[str] = Field(max_length=500, default=None)
    inventory_policy: Optional[str] = Field(max_length=500, default=None)
    compare_at_price: Optional[str] = Field(max_length=500, default=None)
    fulfillment_service: Optional[str] = Field(max_length=500, default=None)
    inventory_management: Optional[str] = Field(max_length=500, default=None)
    option1: Optional[str] = Field(max_length=500, default=None)
    option2: Optional[str] = Field(max_length=500, default=None)
    option3: Optional[str] = Field(max_length=500, default=None)
    created_at: Optional[str] = Field(max_length=500, default=None)
    updated_at: Optional[str] = Field(max_length=500, default=None)
    taxable: Optional[str] = Field(max_length=500, default=None)
    barcode: Optional[str] = Field(max_length=500, default=None)
    grams: Optional[str] = Field(max_length=500, default=None)
    image_id: Optional[str] = Field(max_length=500, default=None)
    weight: Optional[str] = Field(max_length=500, default=None)
    weight_unit: Optional[str] = Field(max_length=500, default=None)
    inventory_item_id: Optional[str] = Field(max_length=500, default=None)
    inventory_quantity: Optional[str] = Field(max_length=500, default=None)
    old_inventory_quantity: Optional[str] = Field(max_length=500, default=None)
    tax_code: Optional[str] = Field(max_length=500, default=None)
    requires_shipping: Optional[str] = Field(max_length=500, default=None)
    admin_graphql_api_id: Optional[str] = Field(max_length=500, default=None)
    createdby: str = Field(max_length=100)
    modifiedby: str = Field(max_length=100)
    createdat: str
    modifiedat: str
