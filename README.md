# Ion Lab Regenerative Value Model Simulation Mini-Desktop App
In-house use; will be open source as it matures

## Network Value Regeneration Simulation Dashboard
An interactive Python desktop application designed to model and simulate **exponential network growth** combined with dynamic individual member productivity curves. It allows you to analyze and visualize both immediate round performance and cumulative network value while accounting for member tenure and active churn.

## The Exponential Network Output Lab 🔬
The primary objective of this simulation environment is to study a powerful mathematical contrast: **how a network's total value behaves when its member count grows exponentially, but individual performance grows linearly or hits a plateau.**

Because the network size doubles every round ( M(t) = n • 2^t ), the total group value ($Y$) scales **exponentially over time**, completely overpowering individual limitations. 

## Core Mathematical Concept

The simulation runs a composite model where a macro exponential population interacts with micro-level individual growth:

1. **Network Population: EXPONENTIAL GROWTH**
   * Formula: M(t) = n • 2^t
   * Why: Because every active member recruits exactly 1 new person every round, causing the total headcount to double each step.


2. **Single Member Output (Individual Value) = LINEAR OR DIMINISHING GROWTH**
   * Lab Value y produced at time t, with m members: y(t) = v • m • (2^t)
   * Linear Regeneration: y = v0 +  k  • t(A) (An individual's personal skill adds a flat, constant amount each round).
   * Diminishing Mode: $y = v_{max} \cdot (1 - e^{-k \cdot t})$ (An individual's capacity slows down as they approach a hard ceiling).

3. **Cummulative Total Network Value (Y). HYPER-EXPONENTIAL COMPOUNDING**
   * Formula: (Y(t) = v • m ((2^t+1)-1)
   * Why: By multiplying an exponentially growing population by a steadily improving workforce, the total group output explodes even faster than standard exponential duplication.

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

### Formula snapshot
<img width="844" height="555" alt="Screenshot 2026-09-16 at 12 25 57 AM" src="https://github.com/user-attachments/assets/6bf65b9e-fbf5-42ce-818e-c97854ecdb73" />

