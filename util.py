import json

def printUnitInfo(url: str, community: str, model: str, bedrooms: int, bathrooms: int, unit: str, area: int, rent: int, fees: int):
    print(json.dumps({
        'url': url,
        'community': community,
        'model': model,
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'unit': unit,
        'area': area,
        'rent': rent,
        'fees': fees,
    }))