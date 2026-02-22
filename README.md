## Ambient AI Control Granularity Study
This project explores how different levels of control over ambient AI sensing affect user comfort, trust, and willingness to adopt such systems, using synthetic data.


## Setup
Create and activate a virtual environment, then install dependencies:
pip install -r requirements.txt


## RESEARCH QUESTION - What are we trying to understand?
Primary question:
How does the granularity of control over ambient AI sensing affect perceived comfort, trust, sense of agency, and willingness to adopt?


## HYPOTHESES - What do we expect to happen, and why?
H1: Granular control leads to higher perceived agency than binary or no control.
H2: Higher perceived agency is positively correlated with trust (across conditions).
H3: Binary control increases opt-out behavior compared to granular control.


## STUDY DESIGN - How will we test those hypotheses? Participants, conditions, measurements.
People with certain traits
are exposed to different conditions
which produces outcomes.

### Participants (Synthetic) - What a "synthetic person" is?
- What attributes people have
- How they vary
- What stays fixed vs variable

| Attribute              | Description                     | Type                           |
|------------------------|---------------------------------|--------------------------------|
| Privacy sensitivity    | Baseline concern about sensing  | 1-3 (low / medium / high)      |
| Tech familiarity       | Comfort with new technology     | 1-3 (low / medium / high)      |
| Baseline trust         | General trust in AI systems     | 1-3 (low / medium / high)      |

### Experimental Conditions
- What is manipulated
- How conditions differ
- What users can and cannot do

| Condition           | Control Type        | Description                                                                           |
|---------------------|---------------------|---------------------------------------------------------------------------------------|
| No control          | None                | Sensing is always on; no visibility into what is sensed; no ability to pause or edit  |
| Binary control      | On / Off (Opt-out)  | User can pause (switch off / opt out from) all sensing; no modality-level control     |
| Granular control    | Per-modality        | User controls audio, vision, context; temporary pauses; visible indicators of sensing |

### Outcome Metrics
- What is measured
- How it is represented numerically

| Metric           | Meaning                                | Scale |
|------------------|----------------------------------------|-------|
| Comfort          | Ease of coexisting with the system     | 1–5   |
| Trust            | Belief system behaves as intended      | 1–5   |
| Agency           | Perceived ability to influence sensing | 1–5   |
| Adoption intent  | Likelihood of regular use              | 1–5   |

In addition to self-reported measures (survey responses), we simulate a binary “opt-out” behavior, representing a user fully disabling (shutting off) the system in a given scenario.


