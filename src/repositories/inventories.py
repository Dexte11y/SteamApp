from models.inventories import Inventories
from utils.repository import SQLAlchemyRepositoryImplementation


class InventoriesRepository(SQLAlchemyRepositoryImplementation):
    model = Inventories
