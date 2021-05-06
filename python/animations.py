from matplotlib.animation import FuncAnimation
import numpy as np
from matplotlib import pyplot as plt
import parameters as P
from mpl_toolkits.mplot3d import Axes3D

class gpsAnimation:
    """
    Create the GPS Animation
    """
    def __init__(self):
        self.fig = plt.figure()
        self.ax = fig.gca(projection='3d')
        self.ax.set_xlim3d(-P.orbital_radius, P.orbital_radius)
        self.ax.set_ylim3d(-P.orbital_radius, P.orbital_radius)
        self.ax.set_zlim3d(-P.orbital_radius, P.orbital_radius)
        self.ax.set_aspect('equal')

        self.flag_init = True

    def update(self, satellites, receivers):
        [self.draw_satellite(satellite) for satellite in satellites]

        if self.flag_init:
            self.flag_init = False

    def draw_satellite(self, satellite):
        