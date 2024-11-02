import requests
import time
import random
import os
from dotenv import load_dotenv

load_dotenv()
MAIN_APP_PORT = os.getenv("APP_PORT")

# отправляем на сервис запросы
for i in range(40):
    flat_id = i
    model_params = {
          "build_year": random.randrange(1900, 2020),
          "building_type_int": random.randrange(0, 6),
          "latitude": random.uniform(55.0, 55.9),
          "longitude": random.uniform(37.0, 37.9),
          "ceiling_height": random.uniform(2.5, 3),
          "flats_count": random.randrange(1, 500),
          "floors_total": random.uniform(1, 30),
          "has_elevator": bool(random.getrandbits(1)),
          "floor": random.randrange(1, 30),
          "kitchen_area": random.uniform(5, 15),
          "living_area": random.uniform(15, 100),
          "rooms": random.randrange(1, 7),
          "is_apartment": bool(random.getrandbits(1)),
          "total_area": random.uniform(20, 115)
      }

    response = requests.post(f'http://localhost:{MAIN_APP_PORT}/api/flats/?flat_id={flat_id}', json=model_params)
    
    # на 30 запросе перерыв 30 секунд
    if i == 30:
        time.sleep(30)
    
    # после каждого запроса перерыв 2 секунды
    time.sleep(2) 