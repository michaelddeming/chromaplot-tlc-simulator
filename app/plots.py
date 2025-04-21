import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def main():
    # COMPOUNDS --> "name": [x, y, rf]
    COMPOUNDS = {
                "comp1": [1, 0, 0.5],
                "comp2": [2, 0, 0.9],
                "comp3": [3, 0, 0.33],
                "comp4": [4, 0, 0.2],
                "comp5": [5, 0, 0.87],
                }

    x_data_dict = {}
    y_data_dict = {}

    for key in COMPOUNDS:
        x_data_dict[key], y_data_dict[key] = generate_data(COMPOUNDS[key], 10)


    fig, ax = plt.subplots()
    
    # Create two separate plot elements for comp1 and comp2
    colors = ["r", "b", "g", "y", "m"]
    
    plot_objs = []
    for i, key in enumerate(COMPOUNDS):
        color = colors[i % len(colors)]
        plot_objs.append(ax.plot([], [], f"{color}o")[0])
    

    # Set axis limits
    ax.set_xlim(0, len(x_data_dict) + 1)
    ax.set_ylim(0, 10)

    def init():
        for obj in plot_objs:
            obj.set_data([], [])
        
        return plot_objs

    def update(frame):
        # Update both compounds at the same time
        for i, key in enumerate(COMPOUNDS):
            plot_objs[i].set_data(x_data_dict[key][:frame], y_data_dict[key][:frame])
        return plot_objs

    ani = FuncAnimation(
        fig,
        update,
        frames=range(1, 11),
        init_func=init,
        blit=True
    )

    plt.title("Thin Layer Chromatography Simulation")
    plt.xlabel("Compounds")
    plt.ylabel("Distance (cm)")
    plt.show()

def generate_data(compound: list, data_quantity: int):
    if compound:
        x_data = []
        y_data = []
        for _ in range(data_quantity):
            x_data.append(compound[0])
            y_data.append(compound[1])
            compound = [compound[0], compound[1] + compound[2], compound[2]]
        return x_data, y_data
    raise ValueError("No Compound")

if __name__ == "__main__":
    main()