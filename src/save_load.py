import json

SAVE_FILE = "savegame.json"


def save_game_state(player, world_position, selected_land, completed_realms):
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
        "completed_realms": list(completed_realms)
    }

    try:
        with open(SAVE_FILE, "w") as f:
            json.dump(state, f, indent=4)
        print("Stan gry zapisany.")
    except Exception as e:
        print("Błąd przy zapisywaniu stanu gry:", e)


def load_game_state():
    try:
        with open(SAVE_FILE, "r") as f:
            state = json.load(f)
        print("Stan gry wczytany.")
        return state
    except Exception as e:
        print("Błąd przy ładowaniu stanu gry:", e)
        return None
