import logging
import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# ==============================================================================
# --- Tokens are read from environment variables ---
BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')

# --- Параметри пошуку квитків ---
STATION_FROM_CODE = '2200300'  # Хмельницький
STATION_TO_CODE = '2218214'    # Лазещина
DEPARTURE_DATE = '2025-06-29'

# --- Інтервали перевірки ---
SEARCH_INTERVAL_SECONDS = 300  # 5 хвилин для режиму ПОШУКУ
ALARM_INTERVAL_SECONDS = 5     # 5 секунд для режиму СИГНАЛІЗАЦІЇ
# ==============================================================================

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def send_telegram_message(message):
    import requests
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {'chat_id': CHAT_ID, 'text': message, 'parse_mode': 'Markdown'}
    try:
        requests.post(url, json=payload, timeout=10).raise_for_status()
        logging.info("Повідомлення успішно надіслано в Telegram.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Помилка надсилання повідомлення в Telegram: {e}")


def does_train_exist():
    """Return True if at least one train card is present on the page."""
    search_url = f"https://booking.uz.gov.ua/search-trips/{STATION_FROM_CODE}/{STATION_TO_CODE}/list?startDate={DEPARTURE_DATE}"

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36')

    current_folder = os.getcwd()
    driver_path = os.path.join(current_folder, 'chromedriver.exe')
    chrome_binary_path = os.path.join(current_folder, 'chrome-win64', 'chrome.exe')

    if not os.path.exists(chrome_binary_path):
        logging.error(f"НЕ ЗНАЙДЕНО БРАУЗЕР! Перевірте шлях: {chrome_binary_path}")
        return False

    chrome_options.binary_location = chrome_binary_path

    driver = None
    try:
        service = ChromeService(executable_path=driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get(search_url)

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "TripUnit"))
        )

        logging.info("ЗНАЙДЕНО КАРТКУ ПОТЯГА!")
        return True

    except TimeoutException:
        logging.info("Потяги на маршруті не знайдено.")
        return False
    except Exception as e:
        logging.error(f"Сталася невідома помилка: {e}")
        return False
    finally:
        if driver:
            driver.quit()


if __name__ == "__main__":
    if not BOT_TOKEN or not CHAT_ID:
        logging.error("Будь ласка, задайте BOT_TOKEN і CHAT_ID як змінні середовища.")
    else:
        logging.info("Бот запущено в режимі 'сигналізації'.")

        send_telegram_message(
            f"✅ **Бот запущений!**\n\n"
            f"Починаю моніторинг потягів за маршрутом **Хмельницький → Лазещина** на **{DEPARTURE_DATE}**.\n\n"
            f"Перевірка кожні {SEARCH_INTERVAL_SECONDS} секунд. У разі знахідки - перехід в режим 'сигналізації'."
        )

        try:
            while True:
                if does_train_exist():
                    logging.info("ПОТЯГ ЗНАЙДЕНО! Переходжу в режим флуду кожні 5 секунд.")
                    alarm_message = (
                        f"🚨 **УВАГА! Є ПОТЯГ!** 🚨\n\n"
                        f"З'явився потяг на маршруті **Хмельницький → Лазещина** на **{DEPARTURE_DATE}**.\n\n"
                        f"**ТЕРМІНОВО ПЕРЕВІРЯЙТЕ САЙТ!**"
                    )
                    while True:
                        send_telegram_message(alarm_message)
                        time.sleep(ALARM_INTERVAL_SECONDS)
                else:
                    logging.info(f"Потягів немає. Наступна перевірка через {SEARCH_INTERVAL_SECONDS / 60:.0f} хвилин.")
                    time.sleep(SEARCH_INTERVAL_SECONDS)

        except KeyboardInterrupt:
            logging.info("Роботу скрипта зупинено вручну.")
