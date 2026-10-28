# Orion Avto — Yandex feed

Репозиторий хранит YML-фид `feed.xml` для Яндекс.Директа/Вебмастера и закреплённые изображения в `images/pinned/`.

## Текущий фид

```
https://raw.githubusercontent.com/dessmond29-star/orion-avto-feed/main/feed.xml
```

## Структура

- `feed.xml` — основной YML-фид
- `images/pinned/` — закреплённые изображения автомобилей
- `generate_feed.py` — вспомогательный генератор/валидатор фида
- `.github/workflows/update-feed.yml` — обновление по расписанию

## Обновление фида

1. Обновите `feed.xml`.
2. Проверьте XML:

```bash
python generate_feed.py --check
```

3. Закоммитьте и запушьте в `main`.

## Автообновление

Файл `.github/workflows/update-feed.yml` проверяет XML и обновляет дату каталога. Проверка запускается вручную или по расписанию.
