from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.service import Service as FirefoxService
import pytest
import requests
from utils.api import URL, Endpoint
import random

def get_driver(name):
    if name == 'Chrome':
        service = ChromeService(executable_path=ChromeDriverManager().install())
        return webdriver.Chrome(service=service)
    elif name == 'Firefox':
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        return webdriver.Firefox(service=service)
    else:
        raise TypeError('Driver is not found')


@pytest.fixture(params=['Chrome', 'Firefox'])
def web_driver(request):
    driver = get_driver(request.param)
    driver.maximize_window()
    driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver

    driver.quit()

@pytest.fixture
def create_user_and_delete_user():
    # создаём список, чтобы метод мог его вернуть
    new_user = []
    # Генератор никнейма

    def generate_name(length=random.randint(5,6)):
        name = ''.join(str(random.randint(0, 9)) for i in range(length))
        return name
    # Генератор логинов
    def generate_login(name="Nikita", surname="Semenov", cohort_number="9", domain="yandex.com"):
        return f"{name}{surname}{cohort_number}{random.randint(100, 999)}@{domain}"

    # Генератор паролей
    def generate_password(length=random.randint(6, 10)):
        password = ''.join(str(random.randint(0, 9)) for i in range(length))
        return password

    # Постоянный пользователь в системе:
    cred_login = 'NikitaSemenov7251@yandex.com'
    cred_pass = '93585982'

    # генерируем имя, почту и логин пользователя
    name = generate_name()
    email = generate_login()
    password = generate_password()

    new_user.append(name)
    new_user.append(email)
    new_user.append(password)

    # собираем тело запроса
    payload = {
        "name": name,
        "email": email,
        "password": password
    }

    cr = requests.post(f'{URL.MAIN_PAGE_URL}{Endpoint.CREATE_USER}', data=payload)  # создание user
    yield new_user

    login_user = requests.post(f'{URL.MAIN_PAGE_URL}{Endpoint.LOGIN_USER}', data=payload)  # логин user
    token = login_user.json()['accessToken']  # получение accessToken
    del_user = requests.delete(f'{URL.MAIN_PAGE_URL}{Endpoint.DEL_USER}', headers={'Authorization': token})  # удаление user