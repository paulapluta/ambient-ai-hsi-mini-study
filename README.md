# Ambient AI Control Granularity Study

This project explores how different levels of control over ambient AI sensing affect user comfort, trust, agency, and willingness to adopt such systems, using synthetic data.

## Findings

See [Mini-Project Findings](reports/mini_findings_v1.md) for full results and interpretation.

---

## Setup

Create and activate a virtual environment, then install dependencies:
```bash
pip install -r requirements.txt
```

---

## Research Question

How does the granularity of control over ambient AI sensing affect perceived comfort, trust, sense of agency, and willingness to adopt?

---

## Hypotheses

- **H1:** Granular control leads to higher perceived agency than binary or no control.
- **H2:** Higher perceived agency is positively correlated with trust across conditions.
- **H3:** Binary control increases opt-out behavior compared to granular control.

---

## Study Design

Synthetic participants with varying trait-level attributes are exposed to different sensing control conditions, producing measurable outcomes.

### Participants (Synthetic)

| Attribute           | Description                    | Values                    |
|---------------------|--------------------------------|---------------------------|
| Privacy sensitivity | Baseline concern about sensing | 1–3 (low / medium / high) |
| Tech familiarity    | Comfort with new technology    | 1–3 (low / medium / high) |
| Baseline trust      | General trust in AI systems    | 1–3 (low / medium / high) |

### Experimental Conditions

| Condition        | Control Type       | Description                                                                           |
|------------------|--------------------|---------------------------------------------------------------------------------------|
| No control       | None               | Sensing is always on; no visibility into what is sensed; no ability to pause or edit  |
| Binary control   | On / Off (opt-out) | User can pause all sensing (switch off / opt out from); no modality-level control     |
| Granular control | Per-modality       | User controls audio, vision, context; temporary pauses; visible indicators of sensing |

### Outcome Metrics

| Metric          | Meaning                                | Scale |
|-----------------|----------------------------------------|-------|
| Comfort         | Ease of coexisting with the system     | 1–5   |
| Perceived trust | Belief system behaves as intended      | 1–5   |
| Perceived agency| Perceived ability to influence sensing | 1–5   |
| Adoption intent | Likelihood of regular use              | 1–5   |

In addition to self-reported measures, a binary opt-out behavior is simulated, representing a user fully disabling the system in a given scenario.