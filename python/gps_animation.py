from matplotlib import pyplot as plt
import numpy as np
from matplotlib import patches as mpatches
import parameters as P

class GPSAnimation:
    """
        Create GPS Receiver Animation
    """
    def __init__(self):
        self.flag_init = True
        self.fig, self.ax = plt.subplots()
        self.receiver = None
        self.satellites = []

        plt.axis([-2*P.orbital_radius, 2*P.orbital_radius, -2*P.orbital_radius, 2*P.orbital_radius])
        self.ax.set_aspect('equal')
    def update(self, receiver, satellites):
        """
        Updates the animation

        Parameters:
            receiver ((2, ) ndarray): xy coordinates
            satellites ((2, n) ndarray): xy coordinates for n satellites
        """
        self.draw_receiver(receiver)
        self.draw_satellites(satellites)
        self.flag_init = False

    def draw_satellites(self, satellites):
        """
        Updates the animation

        Parameters:
            satellites ((n,2) ndarray): xy coordinates for n satellites
        """

        satellites_xy = satellites - P.receiver_width/2.0

        if self.flag_init:
            for n in np.size(satellites_xy,0):
                my_sat = mpatches.Rectangle(
                    satellites_xy[n], P.receiver_width, P.receiver_width,
                    fc='red', ec='black'
                )
                self.satellites.append(my_sat)
                self.ax.add_patch(my_sat)

        else:
            for 

    def draw_receiver(self, receiver):
        """
        Updates receiver

        Parameters:
            receiver ((2, ) ndarray): xy coordinates
        """
        xy = receiver - P.receiver_width/2.0

        if self.flag_init:
            self.receiver = mpatches.Rectangle(
                xy, P.receiver_width, P.receiver_width,
                fc='blue', ec='black'
            )
            self.ax.add_patch(self.receiver)
        else:
            self.receiver.set_xy(xy)
