from environs import Env

env = Env()
env.read_env()
# Забираем токен как переменную среды# Забираем токен как переменную среды# Забираем токен как переменную среды
# Забираем токен как переменную среды
# Забираем токен как переменную среды
# Забираем токен как переменную среды
BOT_TOKEN = env.str("BOT_TOKEN")
# Если токен не найден - заканчиваем программу
if BOT_TOKEN:
    print('BOT_TOKEN found')
else:
    exit("Error: no BOT_TOKEN provided")

# Забираем ID-шники как переменные среды
ADMIN_IDS = env.list("ADMIN_IDS")
# Если токен не найден - заканчиваем программу
if ADMIN_IDS:
    print('ADMIN_IDS are found')
else:
    exit("Error: no ADMIN_IDS are provided")

