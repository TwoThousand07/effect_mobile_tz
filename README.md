# 🔐 Custom Authentication & Authorization System (Django + DRF)

## 📌 Описание проекта

Backend-приложение с **кастомной системой аутентификации и авторизации**, реализованной без использования встроенных механизмов Django (сессий и стандартного auth workflow).

Проект демонстрирует:

* работу JWT-аутентификации
* разграничение доступа (RBAC)
* архитектуру backend-приложения
* контроль доступа к ресурсам

---

## 🧠 Основные возможности

### 🔐 Аутентификация

* Регистрация пользователя
* Логин по email и паролю
* Хеширование пароля (bcrypt)
* Генерация JWT-токена
* Stateless-аутентификация через header

---

### 🛡️ Авторизация (RBAC)

* Пользователь связан с ролью (Role)
* Роль определяет доступ к ресурсам
* Поддержка действий:

  * read
  * create
  * update
  * delete
* Централизованная проверка прав через:

  * `has_permission`
  * декоратор `@permission_required`

---

### ⚙️ Middleware

* Кастомный middleware:

  * извлекает JWT из заголовка
  * валидирует токен
  * определяет пользователя
  * записывает его в `request.user`

---

## 🧱 Архитектура проекта

```text
accounts/      # Пользователи и аутентификация
permissions/   # Роли и права доступа (RBAC)
core_api/      # API и mock-ресурсы
```

---

## 🗂️ Модели

### User

* email (уникальный)
* password (bcrypt)
* role (FK)
* is_active

---

### Role

* name (admin, user)

---

### Permission

* role (FK)
* resource (например: products)
* can_read
* can_create
* can_update
* can_delete

---

## 🌐 API

### 🔑 Аутентификация

#### Регистрация

```http
POST /api/auth/register/
```

#### Логин

```http
POST /api/auth/login/
```

Ответ:

```json
{
  "token": "JWT_TOKEN"
}
```

---

### 📦 Ресурсы (mock)

#### Получить список продуктов

```http
GET /api/products/
```

#### Создать продукт

```http
POST /api/products/create/
```

---

### 🛠 Управление правами (только admin)

```http
POST /api/permissions/update/
```

---

## 🔑 Использование токена

Каждый защищённый запрос должен содержать header:

```text
Authorization: Bearer <your_token>
```

---

## 🚫 Обработка ошибок

| Код | Значение                         |
| --- | -------------------------------- |
| 401 | Пользователь не аутентифицирован |
| 403 | Нет доступа к ресурсу            |

---

## 🧪 Тестовые данные

```text
email: user@test.com
password: 123456
```

---

## ⚙️ Установка и запуск

### 📦 Вариант 1 (рекомендуется, через uv)

```bash
uv sync
uv run python manage.py migrate
uv run python manage.py runserver
```

---

### 📦 Вариант 2 (через pip)

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 📌 Технологии

* Django
* Django REST Framework
* bcrypt
* PyJWT
* uv / pip

---

## 🧠 Особенности реализации

* Полностью кастомная аутентификация (без Django sessions)
* Stateless JWT-аутентификация
* Role-Based Access Control (RBAC)
* Декораторы для проверки доступа
* Middleware для определения пользователя
* Централизованная маршрутизация API

---

## 📈 Вывод

В рамках проекта реализована полноценная backend-система:

* аутентификация пользователей через JWT
* авторизация на основе ролей
* контроль доступа к ресурсам

Проект демонстрирует практическое понимание архитектуры backend-приложений и механизмов безопасности.
