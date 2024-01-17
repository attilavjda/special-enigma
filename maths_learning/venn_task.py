import matplotlib.pyplot as plt
from matplotlib.patches import Circle, PathPatch
from matplotlib.text import TextPath
from matplotlib.transforms import Affine2D

# Function to create a funky Venn diagram
def create_funky_venn(ax, A1, A2, A3):
    circle_radius = 1.0
    overlap_radius = 0.6

    # Draw circles
    circle1 = Circle((-1, 0), circle_radius, fc='skyblue', alpha=0.7)
    circle2 = Circle((1, 0), circle_radius, fc='lightgreen', alpha=0.7)
    circle3 = Circle((0, 1.5), circle_radius, fc='lightcoral', alpha=0.7)

    ax.add_patch(circle1)
    ax.add_patch(circle2)
    ax.add_patch(circle3)

    # Draw the funky overlap region for exactly two events
    path = TextPath((-0.5, 1.2), '2', size=2, prop='bold')
    trans = Affine2D().rotate_deg(45).translate(0, 0.1)
    path = path.transformed(trans)
    overlap_patch = PathPatch(path, fc='lightgray', alpha=0.7)
    ax.add_patch(overlap_patch)

    # Draw text labels
    ax.text(-1, 0, 'A1', va='center', ha='center', color='white', weight='bold')
    ax.text(1, 0, 'A2', va='center', ha='center', color='white', weight='bold')
    ax.text(0, 1.5, 'A3', va='center', ha='center', color='white', weight='bold')

    # Set axis properties
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1, 2)

    # Remove axis ticks and labels
    ax.set_xticks([])
    ax.set_yticks([])

# Define the sets
A1 = {1}
A2 = {1}
A3 = {1}

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6))

# Create the funky Venn diagram
create_funky_venn(ax, A1, A2, A3)

# Show the plot
plt.title('Funky Venn Diagram for Exactly Two Events')
plt.show()
