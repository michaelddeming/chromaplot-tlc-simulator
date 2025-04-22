# matplotlib Objects
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Custom Objects
from classes.compound import Compound 

def main():

    # TEMP Compound Objects
    COMPOUNDS_LIST = []
    for i in range(6):
        if i == 0:
            COMPOUNDS_LIST.append(Compound(name= f"solvent", x_cord=i, y_cord=0, ret_fact= 1.0))
        else:
            rand_num = np.random.random()
            print(rand_num)
            COMPOUNDS_LIST.append(Compound(name= f"comp{i}", x_cord=i, y_cord=0, ret_fact= rand_num))

    # COMPOUNDS --> "name": [x, y, rf]
    COMPOUNDS = {compound.name : compound.get_data() for compound in COMPOUNDS_LIST}
    print(COMPOUNDS)
    

    x_data_dict = {}
    y_data_dict = {}

    FRAME_COUNT = 150
    for key in COMPOUNDS:
        x_data_dict[key], y_data_dict[key] = generate_data(COMPOUNDS[key], FRAME_COUNT)

    fig, ax = plt.subplots()

    # Create two separate plot elements for comp1 and comp2
    colors = ["k", "b", "g", "y", "m", "r"]

    plot_objs = []
    for i, key in enumerate(COMPOUNDS):
        color = colors[i % len(colors)]
        plot_objs.append(ax.plot([], [], f"{color}o")[0])

    # Set axis limits
    ax.set_xlim(0, len(x_data_dict) + (len(x_data_dict) * 0.1))
    ax.set_ylim(0, FRAME_COUNT + (FRAME_COUNT * 0.1))

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
        fig, update, frames=range(1, FRAME_COUNT + 1), init_func=init, blit=True
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
