# Demo assets: screenshots & video guide

Этот файл содержит точный чек‑лист скриншотов и короткий сценарий для 1.5–2 минутного демонстрационного видео, а также команды/рекомендации по записи.

## Папка для артефактов

- Сохраните все материалы в папке `demo_assets/` в корне проекта.
- Пример структуры:
```
demo_assets/
  screenshots/
    01_login.png
    02_user_list.png
    03_chat_with_ai.png
    04_message_sent.png
    05_refresh_restore.png
    06_logout.png
  video/
    demo.mp4
```

## Список обязательных скриншотов (имена файлов)

1. `01_login.png` — Окно с формой логина (пустое поле username). 
2. `02_user_list.png` — Список пользователей (sidebar), видно несколько юзеров.
3. `03_chat_with_ai.png` — Открыт чат с `AI`, видно историю (исходящие и входящие сообщения).
4. `04_message_sent.png` — Отправленное сообщение (синяя карточка) и метка времени.
5. `05_refresh_restore.png` — Скрин после обновления страницы: видно, что сессия восстановлена (username в верхнем блоке).
6. `06_logout.png` — Вид с активной кнопкой Logout и пустой формой логина после выхода.

Советы по скриншотам:
- Используйте Snipping Tool (Win+Shift+S) или `PrtSc` + вставка в Paint.
- Держите браузер в 1280×800 или 1366×768 для совместимости.
- Добавьте короткие подписи к файлам, если нужно.

## Сценарий видео (пример 1:30–2:00 мин)

0–10s — Вступление (название проекта: ChatApp, ваше имя)
10–30s — Показ логина: введите `username`, нажмите Login (объясните: логин или автоматическая регистрация)
30–55s — Откройте чат с `AI`, отправьте сообщение; покажите, как сообщение появляется у получателя.
55–70s — Обновите страницу → покажите, что сессия восстановлена (session persistence).
70–90s — Нажмите Logout, затем войдите под другим пользователем → покажите переключение аккаунтов и сохранённую историю.
90–110s — Краткое завершение: где код (GitHub), где задеплоено (Render) и как запустить локально.

## Рекомендации для записи

- Используйте OBS или встроенный рекордер Windows (Win+G). OBS даёт лучший контроль звука и качества.
- Настройки OBS рекомендуемые:
  - Resolution: 1280x720
  - Framerate: 30 fps
  - Encoder: x264, bitrate 2500–4000 kbps
  - Audio: микрофон + системные звуки (если нужно)
- Простое ffmpeg (вариант для записи экрана в Windows):
```
ffmpeg -f gdigrab -framerate 30 -i title="Google Chrome" -f dshow -i audio="Microphone (Realtek)" -vcodec libx264 -preset veryfast -crf 23 demo_assets/video/demo.mp4
```
Замените `title` и `audio` на реальные значения (проверьте через `ffmpeg -list_devices true -f dshow -i dummy`).

## Монтаж и экспорт

- Обрежьте лишние паузы, подпишите ключевые шаги (Login, Send, Refresh, Logout).
- Экспорт в MP4 (H.264) 1280×720, 30fps.

## Загрузка и README

1. Загрузите `demo.mp4` на YouTube (Unlisted).
2. В `README.md` замените плейсхолдеры Live URL и Demo Video на реальные ссылки.
3. В репозитории добавьте папку `demo_assets/screenshots/` и `demo_assets/video/demo.mp4` (если размер позволяет).

## Краткая команда для конвертации/сжатия видео (ffmpeg)

```
ffmpeg -i raw_demo.mp4 -vcodec libx264 -crf 23 -preset medium -acodec aac -b:a 128k demo_assets/video/demo.mp4
```

## Подсказки по озвучке

- Говорите чётко и коротко — 1–2 предложения на шаг.
- Подчеркните: login (existing/new), session persistence (localStorage), logout, chat history persisted in DB, deployment link.

---

Если хотите, могу автоматически сгенерировать файл `demo_assets/recording_checklist.txt` с шагами, или помочь подготовить OBS‑сцену. Хотите это сделать сейчас?
