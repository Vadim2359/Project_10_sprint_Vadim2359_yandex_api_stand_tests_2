import sender_stand_request
import data

def get_kit_body(name):

    # копирование в переменную current_body словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    current_body = data.kit_body.copy()
    # изменение значения ключа на переменную name
    current_body["name"] = name
    # возвращается новый словарь с нужным значением name
    return current_body
def positive_assert(name):

    # В переменную kit_body сохраняется обновленное тело запроса
    kit_body = get_kit_body(name)
    # В переменную kit_response сохраняется результат запроса на создание набора:
    kit_response = sender_stand_request.post_new_kit(kit_body)
    # Проверяется, что код ответа равен 201
    assert kit_response.status_code == 201
    # Проверяется, что имя набора в ответе соответствует заданному
    assert kit_response.json()['name'] == name

# Тест 1. Успешное создание имени набора
# Параметр name состоит из 1 символа
def test_kit_body_1_letter_in_kit_name_get_success_response():
    positive_assert('а')

# Тест 2. Успешное создание имени набора
# Параметр name состоит из допустимых 511 символов
def test_kit_body_511_lettes_in_kit_name_get_success_response():
    positive_assert('AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC')

# Тест 5. Успешное создание имени набора
# Параметр name состоит из разрешенных английских букв
def test_kit_body_inglish_letters_in_kit_name_get_success_response():
    positive_assert('QWErty')

# Тест 6. Успешное создание имени набора
# Параметр name состоит из разрешенных русских букв
def test_kit_body_russian_letters_in_kit_name_get_success_response():
    positive_assert('Мария')

# Тест 7. Успешное создание имени набора
# Параметр name состоит из разрешенных спецсимволов
def test_kit_body_special_symbols_in_kit_name_get_success_response():
    positive_assert('"№%@",')

# Тест 8. Успешное создание имени набора
# Параметр name состоит из разрешенных пробелов
def test_kit_body_space_symbols_in_kit_name_get_success_response():
    positive_assert('Человек и КО')

# Тест 9. Успешное создание имени набора
# Параметр name состоит из разрешенных цифр
def test_kit_body_digital_symbols_in_kit_name_get_success_response():
    positive_assert("123")

    # Функция негативной проверки, когда в ответе ошибка про символы
def negative_assert_code_400(name):
# В переменную kit_body сохраняется обновлённое тело запроса
    kit_body = get_kit_body(name)
# В переменную response сохраняется результат
    kit_response = sender_stand_request.post_new_kit(kit_body)
# Проверяется, что код ответа равен 400
    assert kit_response.status_code == 400

# Тест 3. Ошибка. Параметр состоит из пустой строки
def test_create_kit_empty_name_get_error_response():
    # В переменную user_body сохраняется обновлённое тело запроса
    negative_assert_code_400("")

# Тест 4. Ошибка. Количество символов больше допустимого (512)
def test_create_kit_511_letter_get_error_response():
    # В переменную user_body сохраняется обновлённое тело запроса
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Тест 11. Ошибка. Передан другой тип параметра (число)
def test_create_kit_digits_get_error_response():
    # В переменную user_body сохраняется обновлённое тело запроса
    negative_assert_code_400("123")

# Тест 10. Ошибка. Параметр не передан в запросе kit_body = {}
def test_create_new_kit_empty_kit_body_get_error_response():
# Телу запроса kit_body из файла data присваиваем пустое поле {}
    kit_body = {}
# В переменную response сохраняется результат
    response = sender_stand_request.post_new_kit(kit_body)
# Проверяется, что код ответа равен 400
    assert response.status_code == 400
