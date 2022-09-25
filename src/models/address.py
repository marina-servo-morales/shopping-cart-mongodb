from src.schemas.address import Address


async def create_address(address_collection,address):
    try:
        address = await address_collection.insert_one(address)

        if address.inserted_id:
            address = await get_address(address_collection,address.inserted_id)
            return address
        
    except Exception as e:
        print(f'create_address.error: {e}')


async def get_address(address_collection,address_id):
    try:
        data = await address_collection.find_one({'_id': address_id})
        if data:
            return data
    except Exception as e:
        print(f'create_address.error: {e}')


async def delete_address(address_collection, address_id):
    try:
        address = await address_collection.delete_one(
            {'_id': address_id}
        )
        if address.deleted_count:
            return {'status': 'Address deleted'}
    except Exception as e:
        print(f'delete_address.error: {e}')