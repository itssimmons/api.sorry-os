from config.database import sql_exec


def up():
    sql_exec(
        """CREATE TABLE IF NOT EXISTS users (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		username TEXT NOT NULL,
		avatar TEXT NOT NULL,
		createdAt TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
		updatedAt TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
		)"""
    )
