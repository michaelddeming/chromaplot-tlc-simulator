# matplotlib Objects
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import tempfile
import numpy as np
from matplotlib.animation import FuncAnimation
from io import BytesIO

# Custom Objects
from classes.compound import Compound 

class ChromaPlot:

    def __init__(self, compounds: list, ):
        self.compounds = compounds
        self.compounds_formatted = {}
        self.x_data_dict = {}
        self.y_data_dict = {}
        self.FRAME_COUNT = 200

    
    def format_compounds_list(self):
        if self.compounds:
            self.compounds_formatted = {compound.name : compound.get_data() for compound in self.compounds}

    def generate_frames(self):
    
        x_data_dict = {}
        y_data_dict = {}

        
        for key in self.compounds_formatted:
            if key != "solvent":
                x_data_dict[key], y_data_dict[key] = self.generate_data(self.compounds_formatted[key], self.FRAME_COUNT)
            else:
                x_data_dict[key], y_data_dict[key] = self.generate_data(self.compounds_formatted[key], self.FRAME_COUNT, solvent=True)

        self.x_data_dict = x_data_dict
        self.y_data_dict = y_data_dict
    
    def generate_chromaplot(self):
        self.format_compounds_list()
        self.generate_frames()

        fig, ax = plt.subplots()

        # Create two separate plot elements for comp1 and comp2
        colors = ["k", "b", "g", "y", "m", "r"]

        plot_objs = []
        for i, key in enumerate(self.compounds_formatted):
            color = colors[i % len(colors)]
            plot_objs.append(ax.plot([], [], f"{color}o")[0])

        # Set axis limits
        ax.set_xlim(0, len(self.x_data_dict) -  1 + (len(self.x_data_dict) * 0.1))
        ax.set_ylim(0, self.FRAME_COUNT + (self.FRAME_COUNT * 0.1))

        def init():
            for obj in plot_objs:
                obj.set_data([], [])

            return plot_objs

        def update(frame):
            # Update both compounds at the same time
            for i, key in enumerate(self.compounds_formatted):
                plot_objs[i].set_data(self.x_data_dict[key][:frame], self.y_data_dict[key][:frame])
            return plot_objs

        ani = FuncAnimation(
            fig, update, frames=range(1, self.FRAME_COUNT + 1), init_func=init, blit=True
        )

        plt.title("Thin Layer Chromatography Simulation")
        plt.xlabel("Compounds")
        plt.ylabel("Distance (cm)")

        with tempfile.NamedTemporaryFile(suffix=".gif", delete=False) as tmpfile:
            ani.save(tmpfile.name, writer="pillow")
            
            with open(tmpfile.name, "rb") as f:
                buf = BytesIO(f.read())
        buf.seek(0)
        plt.close(fig)

        return buf





    def generate_data(self, compound: list, data_quantity: int, solvent=False):
        if compound:
            x_data = []
            y_data = []
            for _ in range(data_quantity):
                
                if not solvent:
                    # x buffer element
                    buffer_factor = 0.05 / np.sqrt(compound[0] + 1e-5) # within 10% of original x_data
                    x_buffer_low = compound[0] - (compound[0] * (buffer_factor))
                    x_buffer_high = compound[0] + (compound[0] * (buffer_factor))
                    x_buffer = np.random.uniform(low=x_buffer_low, high=x_buffer_high)
                    x_data.append(x_buffer)
                else:
                    x_data.append(compound[0])
                y_data.append(compound[1])

                compound = [compound[0], compound[1] + compound[2], compound[2]]
            return x_data, y_data
        raise ValueError("No Compound")
            
