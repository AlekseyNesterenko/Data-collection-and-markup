import requests
import json

# Ваши учетные данные API
client_id = "PLECYCRCXF1AL4VNT24KY4AGUXWOVASF1ST4NEARVPIQ1Q5H"
client_secret = "YPS0ILL1PK3ULAN24VZX4H5HQ35KAY1ZVUDC0CQLCMJ0KTQY"

# Конечная точка API
endpoint = "https://api.foursquare.com/v3/places/search"

# Определение параметров для запроса API
city = input("Введите название города: ")
query = input("Какие заведения искать: ")
params = {
    "client_id": client_id,
    "client_secret": client_secret,
    "near": city,
    "query": query,
}

headers = {
    "Accept": "application/json",
    "Authorization": "fsq3YaCwEoKHjtg/2P/WglwUIn4pDTdqoKb1lr63UHGb3sI="
}

# Отправка запроса API и получение ответа
response = requests.get(endpoint, params=params,headers=headers)

# Проверка успешности запроса API
if response.status_code == 200:
    print("Успешный запрос API!")
    data = json.loads(response.text)
    venues = data["results"]
    for venue in venues:
        print("Название:", venue["name"])
        print("Адрес:", venue['location']['formatted_address'])
        print("\n")
else:
    print("Запрос API завершился неудачей с кодом состояния:", response.status_code)
    print(response.text)


# Пример вывода в консоли:


# Введите название города: кемерово
# Какие заведения искать: рестораны
# Успешный запрос API!
# Название: Чайхана42
# Адрес: Кузбасс, Кемерово, Черняховского, 2, 1, Кемерово


# Название: Rebro
# Адрес: Кемерово


# Название: Вегетарианское кафе - Цены на услуги
# Адрес: Кузнецкий пр-кт, д. 55, Кемерово


# Название: Самарканд
# Адрес: Черняховского Ул., д. 3, Кемерово


# Название: Mama Roma
# Адрес: Весенняя Ул., д. 19, 650000, Кемерово


# Название: Port 42
# Адрес: Притомская наб., 7, Кемерово


# Название: Belgiya (Бельгия)
# Адрес: Красноармейская Ул., д. 129 (Красноармейская / Красная), 650000, Кемерово


# Название: Port Coffee
# Адрес: Весенняя Ул., д. 13, Кемерово


# Название: Black Mist shop & lounge
# Адрес: Кузнецкий Пр., 33/1, Кемерово


# Название: Harat's Pub
# Адрес: Ноградская Ул., д. 5, 650000, Кемерово