import json
from pathlib import Path

SAVE_DIR = Path("saves")
USERS_FILE = SAVE_DIR / "users.json"


def _ensure_save_dir():
    SAVE_DIR.mkdir(parents=True, exist_ok=True)


def _sanitize_username(username):
    return "".join(ch for ch in username.strip() if ch.isalnum() or ch in ("_", "-")).lower()


def get_users():
    _ensure_save_dir()
    if not USERS_FILE.exists():
        return []

    try:
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            users = json.load(f)
        return users if isinstance(users, list) else []
    except Exception as e:
        print("Błąd przy odczycie użytkowników:", e)
        return []


def create_user(username):
    clean_name = username.strip()
    if not clean_name:
        return False, "Nazwa użytkownika nie może być pusta."

    slug = _sanitize_username(clean_name)
    if not slug:
        return False, "Nazwa użytkownika zawiera niedozwolone znaki."

    users = get_users()
    if clean_name in users:
        return False, "Taki użytkownik już istnieje."

    users.append(clean_name)

    try:
        _ensure_save_dir()
        with open(USERS_FILE, "w", encoding="utf-8") as f:
            json.dump(users, f, ensure_ascii=False, indent=4)
        return True, "Użytkownik został utworzony."
    except Exception as e:
        print("Błąd przy zapisie użytkowników:", e)
        return False, "Błąd zapisu użytkownika."


def _get_save_file(user_name):
    slug = _sanitize_username(user_name)
    return SAVE_DIR / f"savegame_{slug}.json"


def save_game_state(player, world_position, selected_land, completed_realms, user_name):
    state = {
        "player": {
            "x": player.x,
            "y": player.y,
            "health": player.health,
            "xp": player.xp,
            "coins": player.coins,
            "character": player.character,
            "inventory": player.inventory
        },
        "world_position": world_position,
        "selected_land": selected_land,
        "completed_realms": list(completed_realms),
        "user": user_name
    }

    save_file = _get_save_file(user_name)

    try:
        _ensure_save_dir()
        with open(save_file, "w", encoding="utf-8") as f:
            json.dump(state, f, ensure_ascii=False, indent=4)
        print(f"Stan gry zapisany dla użytkownika {user_name}.")
    except Exception as e:
        print("Błąd przy zapisywaniu stanu gry:", e)


def load_game_state(user_name):
    save_file = _get_save_file(user_name)

    try:
        with open(save_file, "r", encoding="utf-8") as f:
            state = json.load(f)
        print(f"Stan gry wczytany dla użytkownika {user_name}.")
        return state
    except Exception as e:
        print("Błąd przy ładowaniu stanu gry:", e)
        return None


def has_saved_game(user_name):
    return _get_save_file(user_name).exists()
