import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Set clean style
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 12
plt.rcParams['axes.linewidth'] = 1.5
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False

# Colors
BLUE = '#3b82f6'
RED = '#ef4444'
GRAY = '#6b7280'
BLACK = '#111827'

# 1. Two Clusters
def create_two_clusters():
    np.random.seed(42)

    # Generate clusters
    blue_x = np.random.randn(15) * 0.8 + 3
    blue_y = np.random.randn(15) * 0.8 + 3
    red_x = np.random.randn(15) * 0.8 - 1
    red_y = np.random.randn(15) * 0.8 - 1

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(blue_x, blue_y, c=BLUE, s=80, label='Class +1', zorder=3)
    ax.scatter(red_x, red_y, c=RED, s=80, label='Class -1', zorder=3)

    # Add separating line
    x_line = np.linspace(-3, 5, 100)
    y_line = -x_line + 2  # Simple diagonal
    ax.plot(x_line, y_line, '--', color=GRAY, linewidth=2, label='Decision boundary')

    ax.set_xlim(-3, 5)
    ax.set_ylim(-3, 5)
    ax.set_xlabel('Feature $x_1$')
    ax.set_ylabel('Feature $x_2$')
    ax.legend(loc='upper left')
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('../assets/images/two-clusters.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Created two-clusters.png")

# 2. Decision boundary animation (4 panels)
def create_decision_boundary_animation():
    np.random.seed(42)

    # Simple linearly separable data
    X = np.array([
        [2, 3], [3, 3], [3, 2], [4, 3],  # Class +1
        [-1, -1], [0, -1], [-1, 0], [0, 0]  # Class -1
    ])
    y = np.array([1, 1, 1, 1, -1, -1, -1, -1])

    # Simulate training - store weight history
    weights_history = [
        (np.array([0.0, 0.0]), 0.0),      # Initial
        (np.array([0.2, 0.3]), 0.1),      # After few updates
        (np.array([0.5, 0.4]), 0.2),      # Getting better
        (np.array([0.8, 0.7]), 0.3),      # Converged
    ]

    titles = ['Initial (random)', 'After 2 updates', 'After 5 updates', 'Converged']

    fig, axes = plt.subplots(1, 4, figsize=(16, 4))

    for idx, (ax, (w, b), title) in enumerate(zip(axes, weights_history, titles)):
        # Plot points
        pos = y == 1
        neg = y == -1
        ax.scatter(X[pos, 0], X[pos, 1], c=BLUE, s=100, zorder=3)
        ax.scatter(X[neg, 0], X[neg, 1], c=RED, s=100, zorder=3)

        # Plot decision boundary: w·x + b = 0 => x2 = (-w1*x1 - b) / w2
        if abs(w[1]) > 0.01:  # Avoid division by zero
            x1_range = np.linspace(-3, 6, 100)
            x2_boundary = (-w[0] * x1_range - b) / w[1]
            ax.plot(x1_range, x2_boundary, '--', color=GRAY, linewidth=2)
        elif abs(w[0]) > 0.01:
            ax.axvline(-b / w[0], linestyle='--', color=GRAY, linewidth=2)

        ax.set_xlim(-2, 5)
        ax.set_ylim(-2, 5)
        ax.set_title(title)
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.3)

        if idx == 0:
            ax.set_ylabel('$x_2$')
        ax.set_xlabel('$x_1$')

    plt.tight_layout()
    plt.savefig('../assets/images/decision-boundary-steps.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Created decision-boundary-steps.png")

# 3. XOR problem
def create_xor_problem():
    fig, ax = plt.subplots(figsize=(6, 6))

    # XOR points
    X = np.array([[1, 1], [1, -1], [-1, 1], [-1, -1]])
    y = np.array([1, -1, -1, 1])  # XOR pattern

    pos = y == 1
    neg = y == -1
    ax.scatter(X[pos, 0], X[pos, 1], c=BLUE, s=200, zorder=3, label='Class +1')
    ax.scatter(X[neg, 0], X[neg, 1], c=RED, s=200, zorder=3, label='Class -1')

    # Show some failed line attempts
    x_line = np.linspace(-2, 2, 100)

    # Attempt 1: horizontal
    ax.plot(x_line, np.zeros_like(x_line), ':', color='#9ca3af', linewidth=2, alpha=0.7)
    # Attempt 2: vertical
    ax.axvline(0, linestyle=':', color='#9ca3af', linewidth=2, alpha=0.7)
    # Attempt 3: diagonal
    ax.plot(x_line, x_line, ':', color='#9ca3af', linewidth=2, alpha=0.7)

    # Add labels to points
    labels = ['(1,1)\n+1', '(1,-1)\n-1', '(-1,1)\n-1', '(-1,-1)\n+1']
    offsets = [(0.15, 0.15), (0.15, -0.3), (-0.5, 0.15), (-0.5, -0.3)]
    for (x, yc), label, offset in zip(X, labels, offsets):
        ax.annotate(label, (x + offset[0], yc + offset[1]), fontsize=10)

    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_xlabel('$x_1$')
    ax.set_ylabel('$x_2$')
    ax.set_title('XOR: No single line can separate these')
    ax.legend(loc='upper left')
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)

    plt.tight_layout()
    plt.savefig('../assets/images/xor-problem.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Created xor-problem.png")

if __name__ == '__main__':
    create_two_clusters()
    create_decision_boundary_animation()
    create_xor_problem()
    print("All diagrams created!")
