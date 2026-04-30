import datetime

def get_now() -> dict:
    """Returns the current date and time."""
    return {
        "status": "success", 
        "current_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def search_hotels(location: str, price_max: int = 200) -> list:
    """
    Searches for hotels in a given location within a price range.
    Args:
        location: The city to search in.
        price_max: Maximum price per night.
    """
    return [
        {"name": "Hotel Alpha", "city": location, "price": 120},
        {"name": "Beta Resort", "city": location, "price": 180}
    ]

tools = [get_now, search_hotels]
