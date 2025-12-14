#!/usr/bin/env python3
"""
Create a placeholder/demo image for ekstazi_result.png
This simulates what the terminal output would look like
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch

fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Background (terminal-like)
bg = FancyBboxPatch((0, 0), 10, 10, boxstyle="round,pad=0.1", 
                   facecolor='#1e1e1e', edgecolor='#333', linewidth=2)
ax.add_patch(bg)

# Title
ax.text(5, 9.5, 'Ekstazi Regression Test Selection Output', 
        ha='center', va='center', fontsize=14, fontweight='bold', color='#51cf66')

# Terminal output simulation
output_lines = [
    '[INFO] --- ekstazi:5.3.0:select (ekstazi) @ rts-demo ---',
    '[INFO] Ekstazi: Analyzing dependencies...',
    '[INFO] Ekstazi: Detected changes in Calculator.java',
    '[INFO] Ekstazi: Selected 3 tests (out of 10)',
    '',
    '[INFO] --- surefire:3.1.2:test (default-test) @ rts-demo ---',
    '[INFO] Running edu.iastate.coms417.demo.CalculatorTest',
    '[INFO] Tests run: 3, Failures: 0, Errors: 0, Skipped: 0',
    '',
    '[INFO] Results:',
    '[INFO] Tests run: 3, Failures: 0, Errors: 0, Skipped: 0',
    '[INFO] Time elapsed: 1.5 s',
    '',
    '[INFO] BUILD SUCCESS',
    '[INFO] Total time: 2.1 s'
]

y_start = 8.5
line_height = 0.4
colors = {
    'INFO': '#4dabf7',
    'Ekstazi': '#51cf66',
    'BUILD SUCCESS': '#51cf66',
    'default': '#e9ecef'
}

for i, line in enumerate(output_lines):
    y = y_start - i * line_height
    if line.strip() == '':
        continue
    
    # Determine color
    color = colors.get('default', '#e9ecef')
    if 'Ekstazi' in line:
        color = colors['Ekstazi']
    elif 'BUILD SUCCESS' in line:
        color = colors['BUILD SUCCESS']
    elif '[INFO]' in line:
        color = colors['INFO']
    
    ax.text(0.5, y, line, ha='left', va='center', fontsize=10, 
           family='monospace', color=color)

# Comparison box
comp_box = FancyBboxPatch((1, 1), 8, 1.2, boxstyle="round,pad=0.1", 
                         facecolor='#2d3436', edgecolor='#51cf66', linewidth=2)
ax.add_patch(comp_box)

ax.text(5, 1.8, 'Comparison:', ha='center', va='center', 
       fontsize=12, fontweight='bold', color='#51cf66')
ax.text(2.5, 1.4, 'Without Ekstazi:', ha='left', va='center', 
       fontsize=10, color='#ff6b6b')
ax.text(2.5, 1.1, '10 tests, 4.76s', ha='left', va='center', 
       fontsize=10, color='#ff6b6b', family='monospace')

ax.text(7.5, 1.4, 'With Ekstazi:', ha='left', va='center', 
       fontsize=10, color='#51cf66')
ax.text(7.5, 1.1, '3 tests, 1.5s', ha='left', va='center', 
       fontsize=10, color='#51cf66', family='monospace')

ax.text(5, 0.6, 'Time Savings: 68%', ha='center', va='center', 
       fontsize=11, fontweight='bold', color='#ffd43b')

plt.tight_layout()
plt.savefig('ekstazi_result.png', dpi=300, bbox_inches='tight', facecolor='#1e1e1e')
print("✅ Created ekstazi_result.png (placeholder)")
print("   Note: You can replace this with an actual terminal screenshot")

