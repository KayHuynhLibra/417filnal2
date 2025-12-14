#!/usr/bin/env python3
"""
Script to create RTS workflow diagram for the report
Requires: matplotlib, pillow
Install: pip install matplotlib pillow
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Create figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Colors
color_retest = '#ff6b6b'
color_rts = '#51cf66'
color_code = '#4dabf7'
color_test = '#ffd43b'

# ========== LEFT: Retest All Strategy ==========
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.axis('off')
ax1.set_title('Retest All Strategy', fontsize=14, fontweight='bold', pad=20)

# Code change
code_box = FancyBboxPatch((3, 8), 4, 1, boxstyle="round,pad=0.1", 
                          facecolor=color_code, edgecolor='black', linewidth=2)
ax1.add_patch(code_box)
ax1.text(5, 8.5, 'Code Change', ha='center', va='center', fontsize=11, fontweight='bold')

# Arrow down
arrow1 = FancyArrowPatch((5, 8), (5, 6.5), arrowstyle='->', 
                        mutation_scale=20, linewidth=2, color='black')
ax1.add_patch(arrow1)
ax1.text(5.5, 7.2, 'Execute', ha='left', va='center', fontsize=10)

# All tests
test_boxes = []
y_positions = [5.5, 4.5, 3.5, 2.5, 1.5]
for i, y in enumerate(y_positions):
    box = FancyBboxPatch((2, y), 6, 0.8, boxstyle="round,pad=0.05", 
                        facecolor=color_retest, edgecolor='black', linewidth=1.5)
    ax1.add_patch(box)
    ax1.text(5, y+0.4, f'Test {i+1}', ha='center', va='center', fontsize=9)

ax1.text(5, 0.5, '... (All Tests)', ha='center', va='center', fontsize=10, style='italic')
ax1.text(5, 6.5, 'Time: 45s', ha='center', va='center', fontsize=10, 
         bbox=dict(boxstyle='round', facecolor='white', edgecolor='black'))

# ========== RIGHT: RTS Strategy ==========
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.axis('off')
ax2.set_title('Regression Test Selection (RTS)', fontsize=14, fontweight='bold', pad=20)

# Code change
code_box2 = FancyBboxPatch((3, 8), 4, 1, boxstyle="round,pad=0.1", 
                           facecolor=color_code, edgecolor='black', linewidth=2)
ax2.add_patch(code_box2)
ax2.text(5, 8.5, 'Code Change', ha='center', va='center', fontsize=11, fontweight='bold')

# Dependency analysis
analysis_box = FancyBboxPatch((2.5, 6.5), 5, 1, boxstyle="round,pad=0.1", 
                             facecolor='#ffa94d', edgecolor='black', linewidth=2)
ax2.add_patch(analysis_box)
ax2.text(5, 7, 'Dependency Analysis', ha='center', va='center', fontsize=10, fontweight='bold')

# Arrow down
arrow2 = FancyArrowPatch((5, 6.5), (5, 5.5), arrowstyle='->', 
                        mutation_scale=20, linewidth=2, color='black')
ax2.add_patch(arrow2)
ax2.text(5.5, 6, 'Select', ha='left', va='center', fontsize=10)

# Selected tests only
selected_box = FancyBboxPatch((3, 4.5), 4, 0.8, boxstyle="round,pad=0.05", 
                              facecolor=color_rts, edgecolor='black', linewidth=2)
ax2.add_patch(selected_box)
ax2.text(5, 4.9, 'Test 3 (Selected)', ha='center', va='center', fontsize=9, fontweight='bold')

# Skipped tests (grayed out)
skipped_boxes = [(2, 3.5), (2, 2.5), (2, 1.5)]
for x, y in skipped_boxes:
    box = FancyBboxPatch((x, y), 6, 0.8, boxstyle="round,pad=0.05", 
                        facecolor='#e9ecef', edgecolor='gray', linewidth=1, linestyle='--')
    ax2.add_patch(box)

ax2.text(5, 3.9, 'Test 1 (Skipped)', ha='center', va='center', fontsize=8, style='italic', color='gray')
ax2.text(5, 2.9, 'Test 2 (Skipped)', ha='center', va='center', fontsize=8, style='italic', color='gray')
ax2.text(5, 1.9, 'Test 4+ (Skipped)', ha='center', va='center', fontsize=8, style='italic', color='gray')

ax2.text(5, 0.5, 'Time: 8s (82% faster)', ha='center', va='center', fontsize=10, 
         bbox=dict(boxstyle='round', facecolor='white', edgecolor='green', linewidth=2))

plt.tight_layout()
plt.savefig('rts_diagram.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✅ Created rts_diagram.png")
print("   Saved to: images/rts_diagram.png")

