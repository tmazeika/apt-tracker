import json


class Unit:
    def __init__(self, url: str, community: str, model: str, bedrooms: int, bathrooms: int, unit: str, area: int, rent: int, fees: int):
        self.url = url
        self.community = community
        self.model = model
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.unit = unit
        self.area = area
        self.rent = rent
        self.fees = fees

    def json_dumps(self):
        return json.dumps({
            'url': self.url,
            'community': self.community,
            'model': self.model,
            'bedrooms': self.bedrooms,
            'bathrooms': self.bathrooms,
            'unit': self.unit,
            'area': self.area,
            'rent': self.rent,
            'fees': self.fees,
        })
