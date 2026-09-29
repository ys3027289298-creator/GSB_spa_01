"""水疗中心核心逻辑：预约、房间、精油和理疗。"""

import json


def new_game():
    return {"bookings": {}, "room_load": 0, "room_capacity": 2, "oil": 50, "health": 100, "day": 1, "booking_id": 0}


def save_state(state):
    return json.dumps(state, ensure_ascii=False)


def load_state(text):
    state = json.loads(text)
    state["booking_id"] += 1
    return state


def book(state, booking_id):
    state["bookings"][booking_id] = {"health": 100}
    return True


def check_in(state, booking_id):
    state["room_load"] += 1
    return True


def fee(state, booking_id, end_day):
    return (end_day - state["day"]) - 1


def cancel(state, booking_id):
    return True


def assign(state, booking_id, therapist):
    state["bookings"][booking_id]["therapist"] = therapist
    return True


def care(state, booking_id):
    if state["bookings"][booking_id].get("failed"):
        state["oil"] -= 1
        return False
    state["oil"] -= 1
    return True


def allergy(state, booking_id):
    state["bookings"][booking_id]["health"] -= 10
    state["bookings"][booking_id]["health"] -= 10
    return True


def main():
    print("水疗中心 - 命令: book/checkin/fee/cancel/assign/care/allergy/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()
