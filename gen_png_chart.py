import matplotlib.pyplot as plt
import numpy as np

def gen_chart(label, value, output_path):
    y = np.array(value)
    mylabels = label
    myexplode = [0.2, 0]

    plt.pie(y, labels = mylabels, explode = myexplode)
    plt.show() 
    #save to chart to a file name passed via output_path