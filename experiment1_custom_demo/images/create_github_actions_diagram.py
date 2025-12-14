#!/usr/bin/env python3
"""
Create a simple GitHub Actions workflow diagram
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')
ax.set_title('GitHub Actions CI/CD Pipeline with Ekstazi', fontsize=14, fontweight='bold', pad=20)

# Colors
color_step = '#0366d6'
color_success = '#28a745'
color_cache = '#ffa500'

y_positions = [9, 7.5, 6, 4.5, 3, 1.5]
steps = [
    ('1. Checkout Code', 'actions/checkout@v3'),
    ('2. Setup JDK 17', 'Setup Java environment'),
    ('3. Cache Ekstazi', 'Restore .ekstazi directory'),
    ('4. Run Tests', 'mvn test (with RTS)'),
    ('5. Save Cache', 'Save .ekstazi directory'),
    ('✅ Build Success', 'Tests passed')
]

for i, (title, desc) in enumerate(steps):
    y = y_positions[i]
    
    # Box
    if i == len(steps) - 1:
        color = color_success
    elif 'Cache' in title:
        color = color_cache
    else:
        color = color_step
    
    box = FancyBboxPatch((1, y-0.4), 8, 0.8, boxstyle="round,pad=0.1", 
                         facecolor=color, edgecolor='black', linewidth=2, alpha=0.8)
    ax.add_patch(box)
    
    # Text
    ax.text(5, y, title, ha='center', va='center', fontsize=11, fontweight='bold', color='white')
    ax.text(5, y-0.2, desc, ha='center', va='center', fontsize=9, style='italic', color='white')
    
    # Arrow (except last)
    if i < len(steps) - 1:
        arrow = FancyArrowPatch((5, y-0.4), (5, y_positions[i+1]+0.4), 
                                arrowstyle='->', mutation_scale=20, 
                                linewidth=2, color='black')
        ax.add_patch(arrow)

# Add info box
info_box = FancyBboxPatch((0.5, 0.2), 9, 0.8, boxstyle="round,pad=0.1", 
                         facecolor='#f6f8fa', edgecolor='black', linewidth=1)
ax.add_patch(info_box)
ax.text(5, 0.6, 'Workflow automatically runs on every push/PR', 
        ha='center', va='center', fontsize=10)

plt.tight_layout()
plt.savefig('github_actions.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✅ Created github_actions.png")

