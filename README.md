# Ion Lab Regenerative Value Model Simulation Mini-Desktop App
In-house use; will be open source as it matures

## Network Value Regeneration Simulation Dashboard
An interactive Python desktop application designed to model and simulate **exponential network growth** combined with dynamic individual member productivity curves. It allows you to analyze and visualize both immediate round performance and cumulative network value while accounting for member tenure and active churn.

## Core Mathematical Concept

The dashboard evaluates network production across two distinct individual behaviors:
1. **Linear Growth**: Members increase their value by a flat amount each round ($y = v_0 + k \cdot t$).
2. **Diminishing Returns**: Members approach a hard capacity or market exhaustion ceiling ($y = v_{max} \cdot (1 - e^{-k \cdot t})$).

Because members join at different rounds (cohorts), the application uses a phased matrix calculation to apply the correct productivity score to each cohort based on their exact tenure, adjusting for active member **churn rates**.

---

## Installation & Setup

### Prerequisites
Newer operating systems (especially macOS) require the explicit use of `python3` and `pip3`.

1. **Clone or navigate** to your project directory:
   ```bash
   cd path/to/simulation_app
   ```

2. **Install the required packages** (Matplotlib and NumPy):
   ```bash
   pip3 install matplotlib numpy
   ```

---

## 🚀 Running the Application

Launch the interactive graphical dashboard using your terminal:

```bash
python3 app.py
```

*Note: If you have configured an alias for your environment, `python app.py` will also work.*

---

## Dynamic Controls Guide

Once the application window launches, you can tweak the system using live sliders:

| Control Slider | Description |
| :--- | :--- |
| **Initial n** | The starting number of founding members at Round 0. |
| **Linear v0** | The initial value a member produces on their very first round. |
| **Linear k** | The flat value added to an individual's output each round. |
| **Diminish Max** | The absolute performance ceiling ($V_{max}$) an individual can reach. |
| **Diminish k** | The speed factor. High levels mean fast training; low levels mean slow mastery. |
| **Churn Rate** | The percentage of members that leave or stop producing each round. |
| **Radio Buttons**| Toggle between **Linear** and **Diminishing** mathematical modes. |

---

## Visualized Subplots

The dashboard live-renders four distinct quadrants to monitor your model:
* **Network Member Scale $M(t)$**: Evaluates the pure exponential headcount expansion.
* **Individual Output**: Tracks the trajectory of a single member as they gain tenure.
* **Snapshot Output at Round $t$**: Displays the total value generated *strictly inside* that round.
* **Grand Cumulative Output $Y$**: Tracks the compounding financial or structural grand total since day zero.

***Formula snapshot***
<img width="526" height="324" alt="Screenshot 2026-09-15 at 11 21 18 PM" src="https://github.com/user-attachments/assets/8ea6b63f-94c3-4276-ad11-c955b8c95acd" />

