# ruDialoGPT-TelegramBot
Это конечно не чат джипити, но зато умеет вести диалоги.

# Как запустить
ну во-первых нужен установленный пайтон (бота запускал на 3.9)
https://www.python.org/downloads/

я ваш requirements.txt в душе не знаю, поэтому:
```
pip install transformers torch aiogram
```
чтобы запустить:
```
git clone https://github.com/GDManjaro/ruDialoGPT-TelegramBot
cd ruDialoGPT-TelegramBot
python3 run.py
```

# Тесты
На айфоне или айпаде не запускать: не ставится torch (с cuda и без)
На винде работает замечательно, но надо чтобы у вас была хотя-бы GTX 1050 (!!НЕ РАДЕОН!!)
На линуксе вроде норм работает, но без cuda.

p.s. я забыл сказать что надо в config.py написать токен бота и ещё 
если мне будет лень исправлять, то надо поставить torch с поддержкой cuda\
