def db_migrate():
    from database.migrations.mig_1739411674942 import up as up_1
    from database.migrations.mig_1739411696796 import up as up_2

    up_1()
    up_2()


def db_wipe():
    from pathlib import Path
    from config.database import database_path

    path = Path(database_path)

    if path.exists():
        Path(database_path).unlink()

    Path(database_path).touch()


from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("command", choices=["db:migrate", "db:wipe"])
args = parser.parse_args()

if args.command == "db:migrate":
    db_migrate()

if args.command == "db:wipe":
    db_wipe()
