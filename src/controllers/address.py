from src.models.address import (
    create_address,
    get_address_by_user,
    update_address,
    delete_address,
    get_addresses
)
from src.server.database import connect_db, db, disconnect_db


async def adresses_crud():
    ...