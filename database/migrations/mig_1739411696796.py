from config.database import sql_exec


def up():
    sql_exec(
        """CREATE TABLE IF NOT EXISTS chats (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		senderId INTEGER NOT NULL,
		message TEXT NOT NULL,
		mimeType TEXT NOT NULL DEFAULT 'text/plain',
		createdAt TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
		updatedAt TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
	)"""
    )
