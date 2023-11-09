black .
isort .
flake8

sudo -i -u postgres - подключение к постгрес
psql - вход в консоль постгреса
create database trainee; 

\l - просмотр списка БД
\q - выход

alembic init migrations - первый раз

alembic revision --autogenerate -m "Added notes table" - проверяет все изменеия в классах и создаёт миграцию
alembic upgrade head - примерняет миграцию к БД
alembic downgrade base - удаляет миграцию