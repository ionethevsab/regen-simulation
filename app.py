import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons

# 1. EXPONENTIAL MEMBER GROWTH 
def get_member_count(n, t):
    return n * (2 ** t)

def get_cohort_size(n, c_round):
    return n if c_round == 0 else n * (2 ** (c_round - 1))

# 2. NETWORK AGGREGATOR WITH CHURN 
def simulate_network(n, t_max, mode, v0, k_lin, vmax, k_dim, churn_rate):
    round_vals = []
    cum_vals = []
    running_total = 0
    
    for t in range(t_max + 1):
        r_total = 0
        for c_round in range(t + 1):
            base_size = get_cohort_size(n, c_round)
            tenure = t - c_round
            
            # Apply churn reduction: retention = (1 - churn_rate)^tenure
            active_size = base_size * ((1.0 - churn_rate) ** tenure)
            
            if mode == 'Linear':
                val = v0 + (k_lin * tenure)
            else:
                val = vmax * (1.0 - np.exp(-k_dim * tenure))
                
            r_total += active_size * val
            
        running_total += r_total
        round_vals.append(r_total)
        cum_vals.append(running_total)
        
    return round_vals, cum_vals

# 3. INTERACTIVE DESKTOP INTERFACE 
t_max = 10
initial_n = 5
init_v0 = 10
init_klin = 5.0
init_vmax = 100
init_kdim = 0.5
init_churn = 0.05
init_mode = 'Diminishing'

fig, axs = plt.subplots(2, 2, figsize=(12, 8))
plt.subplots_adjust(left=0.1, bottom=0.38, hspace=0.4, wspace=0.3)

t_space = np.arange(t_max + 1)
r_vals, c_vals = simulate_network(initial_n, t_max, init_mode, init_v0, init_klin, init_vmax, init_kdim, init_churn)
m_vals = [get_member_count(initial_n, x) for x in t_space]

# Plot 1: Member Count
p1, = axs[0, 0].plot(t_space, m_vals, 'b-o')
axs[0, 0].set_title("Network Member Scale M(t)")
axs[0, 0].grid(True)

# Plot 2: Individual Curve
if init_mode == 'Linear':
    ind_vals = [init_v0 + (init_klin * x) for x in t_space]
else:
    ind_vals = [init_vmax * (1 - np.exp(-init_kdim * x)) for x in t_space]
p2, = axs[0, 1].plot(t_space, ind_vals, 'g-o')
axs[0, 1].set_title(f"Individual Output ({init_mode})")
axs[0, 1].grid(True)

# Plot 3: Snapshot Output At Time t
p3, = axs[1, 0].plot(t_space, r_vals, 'r-o')
axs[1, 0].set_title("Snapshot Output at Round t")
axs[1, 0].grid(True)

# Plot 4: Cumulative Value Y
p4, = axs[1, 1].plot(t_space, c_vals, 'm-o')
axs[1, 1].set_title("Grand Cumulative Output Y")
axs[1, 1].grid(True)

# SLIDERS & CONTROLS 
ax_n = plt.axes([0.1, 0.25, 0.3, 0.03])
ax_v0 = plt.axes([0.1, 0.19, 0.3, 0.03])
ax_klin = plt.axes([0.1, 0.13, 0.3, 0.03])
ax_vmax = plt.axes([0.55, 0.25, 0.3, 0.03])
ax_kdim = plt.axes([0.55, 0.19, 0.3, 0.03])
ax_churn = plt.axes([0.55, 0.13, 0.3, 0.03])
ax_mode = plt.axes([0.1, 0.03, 0.15, 0.07])

s_n = Slider(ax_n, 'Initial n', 1, 20, valinit=initial_n, valstep=1)
s_v0 = Slider(ax_v0, 'Linear v0', 0, 50, valinit=init_v0)
s_klin = Slider(ax_klin, 'Linear k', 0.0, 20.0, valinit=init_klin)
s_vmax = Slider(ax_vmax, 'Diminish Max', 10, 500, valinit=init_vmax)
s_kdim = Slider(ax_kdim, 'Diminish k', 0.05, 2.0, valinit=init_kdim)
s_churn = Slider(ax_churn, 'Churn Rate', 0.0, 0.5, valinit=init_churn)
r_mode = RadioButtons(ax_mode, ('Diminishing', 'Linear'), active=0)

def update(val):
    mode = r_mode.value_selected
    n = int(s_n.val)
    r_vals, c_vals = simulate_network(n, t_max, mode, s_v0.val, s_klin.val, s_vmax.val, s_kdim.val, s_churn.val)
    
    # Update populations
    m_new = [get_member_count(n, x) for x in t_space]
    p1.set_ydata(m_new)
    axs[0, 0].relim()
    axs[0, 0].autoscale_view()
    
    # Update individual trajectories
    if mode == 'Linear':
        ind_new = [s_v0.val + (s_klin.val * x) for x in t_space]
    else:
        ind_new = [s_vmax.val * (1.0 - np.exp(-s_kdim.val * x)) for x in t_space]
    p2.set_ydata(ind_new)
    axs[0, 1].set_title(f"Individual Output ({mode})")
    axs[0, 1].relim()
    axs[0, 1].autoscale_view()
    
    # Aggregate snapshots and cumulative totals
    p3.set_ydata(r_vals)
    axs[1, 0].relim()
    axs[1, 0].autoscale_view()
    
    p4.set_ydata(c_vals)
    axs[1, 1].relim()
    axs[1, 1].autoscale_view()
    
    fig.canvas.draw_idle()

for slider in [s_n, s_v0, s_klin, s_vmax, s_kdim, s_churn]:
    slider.on_changed(update)
r_mode.on_clicked(update)

plt.show()
