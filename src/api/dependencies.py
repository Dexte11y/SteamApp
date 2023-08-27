from repositories.accounts import AccountsRepository
from services.accounts import AccountsService


def accounts_service():
    return AccountsService(AccountsRepository)
