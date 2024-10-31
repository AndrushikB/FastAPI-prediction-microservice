import requests
import time
import random

# отправляем на сервис запросы
for i in range(40):
    flat_id = i
    model_params = {
          "num__spl__latitude_sp_1": random.uniform(0, 0.9),
          "num__spl__longitude_sp_4": random.uniform(0, 0.9),
          "num__spl__longitude_sp_0": random.uniform(0, 0.9),
          "num__spl__latitude_sp_5": random.uniform(0, 0.9),
          "building_id": 19350,
          "num__pol__total_area ceiling_height": random.uniform(100, 250),
          "num__spl__latitude_sp_0": random.uniform(0, 0.9),
          "num__spl__latitude_sp_4": random.uniform(0, 0.9),
          "num__spl__longitude_sp_1": random.uniform(0, 0.9),
          "floor": random.randrange(1, 30)
      }

    response = requests.post(f'http://localhost:8081/api/flats/?flat_id={flat_id}', json=model_params)
    
    # на 30 запросе перерыв 30 секунд
    if i == 30:
        time.sleep(30)
    
    # после каждого запроса перерыв 2 секунды
    time.sleep(2) 