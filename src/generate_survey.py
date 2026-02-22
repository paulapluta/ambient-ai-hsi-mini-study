import random
from pathlib import Path

import pandas as pd

from generate_participants import load_config, generate_participants


def assign_conditions(participants, config):
    """
    Balanced random assignment to conditions based on config['assignment']['target_counts'].
    """
    target_counts = config["assignment"]["target_counts"]
    condition_ids = []
    for cond_id, count in target_counts.items():
        condition_ids.extend([cond_id] * count)

    # Safety check: ensure we have enough condition slots
    if len(condition_ids) < len(participants):
        raise ValueError(
            f"Not enough target_counts ({len(condition_ids)}) for participants ({len(participants)})."
        )

    # If we have more slots than participants, trim (keeps balanced-ish)
    condition_ids = condition_ids[: len(participants)]

    random.shuffle(condition_ids)

    for p, cond in zip(participants, condition_ids):
        p["condition_id"] = cond
        p["condition_label"] = config["conditions"][cond]["label"]

    return participants


def clamp_and_round(value, min_val=1, max_val=5):
    """Clamp to [min_val, max_val] and round to nearest int."""
    return int(round(max(min_val, min(max_val, value))))


def likert_response(base, noise_sd=0.9):
    """Generate a noisy Likert response around a base value."""
    return base + random.gauss(0, noise_sd)


def generate_survey_response(participant, config):
    """
    Generate comfort/trust/agency/adoption_intent + opt_out based on:
    - participant attributes (privacy_sensitivity, tech_familiarity, baseline_trust)
    - condition effects (no/binary/granular control)
    """
    cond = participant["condition_id"]

    privacy = participant["privacy_sensitivity"]       # 1–3
    tech = participant["tech_familiarity"]             # 1–3
    base_trust = participant["baseline_trust"]         # 1–3

    # --- Condition effects (you can tweak later) ---
    # Intuition:
    # - More control -> more agency
    # - Always-on -> less comfort for high-privacy people
    # - Baseline trust affects trust & adoption
    if cond == "no_control":
        agency_base = 2.0
        comfort_base = 3.0 - 0.5 * (privacy - 1)  # high privacy -> less comfort
    elif cond == "binary_control":
        agency_base = 3.0
        comfort_base = 3.2 - 0.35 * (privacy - 1)
    elif cond == "granular_control":
        agency_base = 4.0
        comfort_base = 3.6 - 0.2 * (privacy - 1)
    else:
        raise ValueError(f"Unknown condition_id: {cond}")

    # Trust influenced by baseline trust + agency + tech familiarity
    trust_base = 2.5 + 0.6 * (base_trust - 2) + 0.25 * (tech - 2) + 0.35 * (agency_base - 3)

    # Adoption intent influenced by comfort + trust
    adoption_base = 2.8 + 0.35 * (comfort_base - 3) + 0.5 * (trust_base - 3)

    # Add noise and clamp to Likert 1–5
    comfort = clamp_and_round(likert_response(comfort_base))
    agency = clamp_and_round(likert_response(agency_base))
    trust = clamp_and_round(likert_response(trust_base))
    adoption = clamp_and_round(likert_response(adoption_base))


    # --- Opt-out behavior (binary) ---
    # Concept:
    # - opt_out = fully disabling / shutting off the system
    # - In the no_control condition, opt_out represents avoidance/refusal (since there's no switch)
    # Intuition:
    # - Lower adoption intent -> higher chance to opt out
    # - Binary control makes full shut-off more likely than granular control
    base_p = 0.10 + 0.20 * (3 - adoption)  # adoption=1 => +0.40, adoption=5 => -0.20

    if cond == "binary_control":
        base_p += 0.15
    elif cond == "granular_control":
        base_p -= 0.05
    elif cond == "no_control":
        base_p += 0.05

    p_opt_out = max(0.0, min(1.0, base_p))
    opt_out = 1 if random.random() < p_opt_out else 0


    return {
        "participant_id": participant["participant_id"],
        "condition_id": participant["condition_id"],
        "condition_label": participant["condition_label"],
        "comfort": comfort,
        "trust": trust,
        "agency": agency,
        "adoption_intent": adoption,
        "opt_out": opt_out,
    }


def main():
    config_path = Path("configs/study_v1.json")
    config = load_config(config_path)

    # Reproducibility
    random.seed(config["random_seed"])

    # Generate participants
    n = config["participants"]["n_participants"]
    participants = generate_participants(n, config)

    # Assign conditions
    participants = assign_conditions(participants, config)

    # Generate survey responses
    responses = [generate_survey_response(p, config) for p in participants]

    # Save to CSV
    out_participants = Path("data/raw/participants_v1.csv")
    out_responses = Path("data/raw/survey_responses_v1.csv")

    pd.DataFrame(participants).to_csv(out_participants, index=False)
    pd.DataFrame(responses).to_csv(out_responses, index=False)

    print(f"Saved participants to: {out_participants}")
    print(f"Saved survey responses to: {out_responses}")
    print("Done ✅")


if __name__ == "__main__":
    main()
