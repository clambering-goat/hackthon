import matplotlib.pyplot as plt
import numpy as np


def generate_pie_chart(label, value, output_path):
    y = np.array(value)
    explode = [0.01, 0]
    plt.figure().clear()
    plt.pie(y, labels=label, explode=explode)
    plt.savefig(output_path)
    # plt.show()
