from models.accounts import Accounts
from utils.repository import SQLAlchemyRepositoryImplementation


class AccountsRepository(SQLAlchemyRepositoryImplementation):
    model = Accounts
