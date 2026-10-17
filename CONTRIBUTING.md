# Правила работы с репозиторием (Git Flow)

## Постоянные ветки
- `main` — то, что выпущено. Прямые коммиты запрещены. Слияния — только из `release/*` и `hotfix/*`.
- `develop` — интеграция готовой работы. Прямые коммиты запрещены. Слияния — из `feature/*`, `release/*`, `hotfix/*`.

## Временные ветки
| Ветка | От чего | Куда сливается | Пример |
|---|---|---|---|
| `feature/<кратко>` | `develop` | `develop` | `feature/courier-shifts` |
| `release/<версия>` | `develop` | `main` и `develop` | `release/0.1.0` |
| `hotfix/<версия>` | `main` | `main` и `develop` | `hotfix/0.1.1` |

## Порядок работы
1. `git checkout develop && git pull`
2. `git checkout -b feature/<кратко>`
3. Коммиты небольшие, сообщение в стиле `orders: добавить проверку статуса (#12)`, где `#12` — задача Redmine.
4. `git push -u origin feature/<кратко>`, затем pull request в `develop`.
5. Слияние после одобрения. Слияния делаем с сохранением истории ветки (`--no-ff`, на GitHub — «Create a merge commit»).
6. Выпуск: ветка `release/x.y.z`, исправления, слияние в `main`, тег `vX.Y.Z`, обратное слияние в `develop`.

## Границы сервисов
См. `docs/architecture.md`.