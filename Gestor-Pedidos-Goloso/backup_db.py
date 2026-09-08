import shutil
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ORIGEN = BASE_DIR / "db.sqlite3"
CARPETA_BACKUPS = BASE_DIR / "backups"


def main():
    if not ORIGEN.exists():
        print(f"No se encontró la base en {ORIGEN}")
        return

    CARPETA_BACKUPS.mkdir(exist_ok=True)
    marca = datetime.now().strftime("%Y%m%d_%H%M%S")
    destino = CARPETA_BACKUPS / f"db_{marca}.sqlite3"
    shutil.copy2(ORIGEN, destino)
    print(f"Backup creado: {destino}")


if __name__ == "__main__":
    main()