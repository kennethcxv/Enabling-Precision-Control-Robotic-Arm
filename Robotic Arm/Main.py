import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display


table = widgets.Output()
display(table)

clicks = []

def plot_robotic_arm(theta1, theta2, theta3):

    plt.clf()

    plt.grid(color='gray', linestyle='-', linewidth=1)
    plt.axhline(y=0, color='k')
    plt.xticks(np.arange(-300, 301, 20))
    plt.yticks(np.arange(0, 301, 20))
    plt.xlim(-300, 300)
    plt.ylim(0, 300)

    circle = plt.Circle((0, 0), 300, color='blue', fill=False)
    plt.gca().add_patch(circle)

    A = np.array([0, 0])
    B = np.array([150 * np.cos(theta1), 150 * np.sin(theta1)])
    C = B + np.array([100 * np.cos(theta1 + theta2), 100 * np.sin(theta1 + theta2)])
    D = C + np.array([50 * np.cos(theta1 + theta2 + theta3), 50 * np.sin(theta1 + theta2 + theta3)])

    plt.plot([A[0], B[0], C[0], D[0]], [A[1], B[1], C[1], D[1]], 'go-', linewidth=2)
    plt.pause(0.25)

def on_click(event):
    global theta1, theta2, theta3, clicks
    x, y = event.xdata, event.ydata

    if len(clicks) < 21:
        # Store the clicked 
        clicks.append((x, y))

        line, = plt.plot([100, x], [100, y], 'g-')
        plt.pause(0.25)

        line.remove()
        plt.draw()

        if len(clicks) == 1:
            with table:
                print("Dot# {:<7} B pos {:<10} A-B ∡ {:<4} Δ A-B ∡ {:<3} C pos {:<10.5} B-C ∡ {:<5} Δ B-C ∡ {:<3} D pos {:<10.5} C-D ∡ {:<4.5} Δ C-D ∡ {:<5} Max Δ∡".format("", "", "", "", "", "", "", "", "", "", ""))

        with table:
            if len(clicks) <= 21:
                i = len(clicks)
                click = clicks[-1]
                theta1_i = np.arctan2(click[1], click[0])
                B_pos = (150 * np.cos(theta1_i), 150 * np.sin(theta1_i))
                delta_theta1 = theta1_i - theta1

                C_pos = (B_pos[0] + 100 * np.cos(theta1_i + theta2), B_pos[1] + 100 * np.sin(theta1_i + theta2))
                delta_theta2 = (theta1_i + theta2) - theta1

                D_pos = (C_pos[0] + 50 * np.cos(theta1_i + theta2 + theta3), C_pos[1] + 50 * np.sin(theta1_i + theta2 + theta3))
                delta_theta3 = (theta1_i + theta2 + theta3) - theta1

                max_delta_theta = max(abs(delta_theta1), abs(delta_theta2), abs(delta_theta3))

                print(f"{i:<6}{B_pos[0]:>9.2f},{B_pos[1]:<9.2f}{theta1_i:>9.2f}{delta_theta1:>12.2f}{C_pos[0]:>10.2f},{C_pos[1]:<9.2f}{(theta1_i + theta2):>9.2f}{delta_theta2:>12.2f}{D_pos[0]:>10.2f},{D_pos[1]:<9.2f}{(theta1_i + theta2 + theta3):>9.2f}{delta_theta3:>12.2f}{max_delta_theta:>12.2f}")

theta1 = np.pi / 2
theta2 = np.pi / -2
theta3 = -np.pi / 2

plot_robotic_arm(theta1, theta2, theta3)

plt.gcf().canvas.mpl_connect('button_press_event', on_click)

plt.show()