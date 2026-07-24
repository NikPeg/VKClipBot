# Как получить USER_TOKEN (токен владельца)

`USER_TOKEN` — пользовательский токен VK, от имени которого бот загружает клипы на стену
сообщества. Если в логах появляется `User authorization failed` (VK error code 5) — токен
протух, и его нужно перевыпустить по этой инструкции.

## Шаги

1. **Залогиньтесь на [vk.com](https://vk.com)** в браузере под аккаунтом **владельца/админа
   группы** (тем, у кого есть права на публикацию в сообщество).

2. **Откройте эту ссылку** в том же браузере (Implicit Flow через приложение Kate Mobile):

   ```
   https://oauth.vk.com/authorize?client_id=2685278&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=video,wall,groups,photos,offline&response_type=token&v=5.199
   ```

   Права (`scope`):
   - `video`, `wall`, `groups`, `photos` — нужны для загрузки клипа на стену сообщества;
   - `offline` — делает токен **бессрочным**, чтобы он больше не отваливался.

3. **Нажмите «Разрешить».** Вас перекинет на пустую страницу `blank.html`. Смотрите в
   **адресную строку** — там будет:

   ```
   https://oauth.vk.com/blank.html#access_token=vk1.a.XXXXXXXX...&expires_in=0&user_id=...
   ```

4. **Скопируйте значение** между `access_token=` и `&expires_in`.
   `expires_in=0` означает, что токен бессрочный — то, что нужно.

5. **Вставьте его** в `.env` в поле `USER_TOKEN=` и перезапустите бота:

   ```bash
   docker compose down && docker compose up -d --build
   ```

## Проверить, живой ли токен

```bash
curl -s "https://api.vk.com/method/users.get?access_token=ВАШ_ТОКЕН&v=5.199"
```

- Ответ с `"response": [...]` — токен рабочий.
- Ответ с `"error_code": 5` — токен мёртвый, перевыпустите заново.
