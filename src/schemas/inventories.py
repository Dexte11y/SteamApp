from pydantic import BaseModel, ConfigDict


class InventoriesSchemaBase(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )
    id: int
    inventoryItem: str


class InventoriesSchemaAdd(InventoriesSchemaBase):
    pass


class InventoriesSchemaInDb(InventoriesSchemaBase):
    id: int
    inventoryItem: str
