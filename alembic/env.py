import sys
import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

from database import Base, SQLALCHEMY_DATABASE_URL

# --- Добавляем корень проекта в sys.path, чтобы импортировать database и models ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

SYNC_SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace(
    "postgresql+asyncpg", "postgresql"
)

config = context.config
config.set_main_option("sqlalchemy.url", SYNC_SQLALCHEMY_DATABASE_URL)
fileConfig(config.config_file_name)

from models.user import User
from models.order import Order

# Указываем метаданные для автогенерации миграций
target_metadata = Base.metadata

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True  # Важно: отслеживать изменения типов колонок
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()