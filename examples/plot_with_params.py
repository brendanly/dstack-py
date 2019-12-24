import matplotlib.pyplot as plt
import numpy as np
from dstack.stack import create_frame
from dstack.matplotlib import MatplotlibHandler

if __name__ == '__main__':
    frame = create_frame(stack='plots/simple_plot',
                         token='token',
                         handler=MatplotlibHandler())

    p = np.arange(0.0, 1.0, 0.1)
    for phase in p:
        t = np.arange(0.0, 2.0, 0.01)
        s = 1 + np.sin(2 * np.pi * t + phase)

        fig, ax = plt.subplots()
        ax.plot(t, s)

        ax.set(xlabel='t', ylabel='x',
               title='My first plot')
        ax.grid()
        frame.commit(fig, 'My first plot', {'phase': phase})
        plt.close(fig)

    frame.push()
