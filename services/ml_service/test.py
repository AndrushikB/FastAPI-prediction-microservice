# Конвертация в json для тестового запроса
import json

model_params = {
          "build_year": 2008,
          "building_type_int": 4,
          "latitude": 55.990021,
          "longitude": 37.232895,
          "ceiling_height": 2.65,
          "flats_count": 107,
          "floors_total": 14,
          "has_elevator": True,
          "floor": 9,
          "kitchen_area": 9.3,
          "living_area": 18.900000,
          "rooms": 1,
          "is_apartment": False,
          "total_area": 37.599998
      }

print(json.dumps(model_params))