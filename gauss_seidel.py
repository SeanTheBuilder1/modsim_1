%matplotlib inline
import matplotlib.pyplot as plt 
import numpy as np

def main():
    x_old = 0.0
    y_old = 0.0
    acceptable_error = 0.0000001
    
    i = 0
    graph_arr_x = []
    graph_arr_y = []

    while True:
        x_new = (5.0 - y_old) / 2.0
        y_new = (x_new - 6.0) / 3.0;
        x_error = abs((x_new - x_old) / x_new)
        y_error = abs((y_new - y_old) / y_new)
        ave_error = (x_error + y_error) / 2.0
        x_old = x_new
        y_old = y_new
        i = i + 1
        print(
            "Iteration %d\nNew x value: %lf\nNew y value: %lf\nX Error: %lf\nY Error: %lf\nAverage Error:%lf\n\n"
            % (i, x_new, y_new, x_error, y_error, ave_error)
        )
        graph_arr_x.append(i)
        graph_arr_y.append(ave_error)
        if (ave_error < acceptable_error):
            print(
                "Acceptable Error Reached!\nResults\nX=%lf, Y=%lf, Error=%lf" %  
                (x_new, y_old, ave_error)
            )
            break
    plt.plot(graph_arr_x, graph_arr_y)
    plt.show()

main()
