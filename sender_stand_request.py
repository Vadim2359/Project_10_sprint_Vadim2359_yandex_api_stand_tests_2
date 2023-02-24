import configuration
import requests
import data

# Создаётся новый пользователь
def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставялем полный url
                         json=user_body,  # тут тело
                         headers=data.headers)  # а здесь заголовки
user_response = post_new_user(data.user_body)

print(user_response.status_code) # выводится на экран статус
print(user_response.json()) # выводится на экран присвоенный authToken

auth_token = user_response.json()['authToken'] # присваивается переменной полученное значение authToken
data.headers["Authorization"] = "Bearer " + auth_token # прописывается значение authToken в headers

# Создаётся новоый набор с Token созданного пользователя
def post_new_kit(kit_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,  # подставялем полный url
                         json=kit_body,  # тут тело
                         headers=data.headers)  # а здесь заголовки

response = post_new_kit(data.kit_body)

print(response.status_code) # выводится на экран статус
print(response.json()) # выводится на экран тело ответа с authToken пользователя, authToken индентичен.

print("Новый headers:")
print(data.headers) # выводится на экран заголовок с authToken нового пользователя


