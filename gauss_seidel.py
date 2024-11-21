%matplotlib inline
import matplotlib.pyplot as plt 

def main():
    x_old = 0.0
    y_old = 0.0
    z_old = 0.0
    acceptable_error = 0.0000001
    
    i = 0
    graph_arr_x = []
    graph_arr_y = []

    while True:
        x_new = (7.0 - y_old + z_old) / 3.0
        y_new = (4.0 - (2 * x_new)-z_old) / 4.0;
        z_new = (3.0 - x_new + y_new) / 3.0;
        x_error = abs((x_new - x_old) / x_new)
        y_error = abs((y_new - y_old) / y_new)
        z_error = abs((z_new - z_old) / z_new)
        ave_error = (x_error + y_error + z_error) / 3.0
        x_old = x_new
        y_old = y_new
        z_old = z_new
        i = i + 1
        print(
            "Iteration %d\nNew x value: %lf\nNew y value: %lf\nNew z value: %lf\nX Error: %lf\nY Error: %lf\nZ Error: %lf\nAverage Error:%lf\n\n"
            % (i, x_new, y_new, z_new, x_error, y_error, z_error, ave_error)
        )
        graph_arr_x.append(i)
        graph_arr_y.append(ave_error)
        if (ave_error < acceptable_error):
            print(
                "Acceptable Error Reached!\nResults\nX=%lf, Y=%lf, Z=%lf Error=%lf" %  
                (x_new, y_new, z_new, ave_error)
            )
            break
    plt.plot(graph_arr_x, graph_arr_y)
    plt.xlabel('Iteration')
    plt.ylabel('Error')
    plt.title('Gauss-Seidel Method')
    plt.show()

main()

