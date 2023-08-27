from models.accounts import Accounts
from utils.repository import SQLAlchemyRepository


class AccountsRepository(SQLAlchemyRepository):
    model = Accounts
