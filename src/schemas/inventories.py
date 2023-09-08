from pydantic import BaseModel, ConfigDict


class InventoriesSchemaBase(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )
    id: int
    inventory: str


class InventoriesSchemaAdd(InventoriesSchemaBase):
    pass

