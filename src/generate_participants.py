import json
import random
from pathlib import Path


def load_config(config_path):
    with open(config_path, "r") as f:
        return json.load(f)


def generate_participant(participant_id, config):
    attributes = config["participants"]["attributes"]

    participant = {
        "participant_id": participant_id
    }

    for attr_name, attr_info in attributes.items():
        participant[attr_name] = random.choice(attr_info["values"])

    return participant


def generate_participants(n, config):
    participants = []
    prefix = config["participants"]["id_prefix"]

    for i in range(1, n + 1):
        participant_id = f"{prefix}{i:03d}"
        participants.append(generate_participant(participant_id, config))

    return participants


if __name__ == "__main__":
    config_path = Path("configs/study_v1.json")
    config = load_config(config_path)

    random.seed(config["random_seed"])

    participants = generate_participants(10, config)

    for p in participants:
        print(p)
