from gps_animation import GPSAnimation
import parameters as P
import numpy as np
from matplotlib import pyplot as plt

if __name__ == '__main__':
    animation = GPSAnimation()

    t = P.t_start

    while t < P.t_end:
        receiver = np.array([0,0])
        satellites = np.array([
            [P.orbital_radius, P.orbital_radius]
            ])

        animation.update(receiver, satellites)

        t += P.dt
        plt.pause(0.1)

    print('Press key to close')
    plt.waitforbuttonpress()
    plt.close()