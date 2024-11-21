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
        y_new = (4.0 - (2 * x_old)-z_old) / 4.0;
        z_new = (3.0 - x_old + y_old) / 3.0;
        x_error = abs((x_new - x_old) / x_new)
        y_error = abs((y_new - y_old) / y_new)
        z_error = abs((z_new - z_old) / z_new)
        ave_error = (x_error + y_error + z_error) / 3.0
        x_old = x_new
        y_old = y_new
        z_old = z_new
        i = i + 1
        print(
            "Iteration %d\nNew x value: %0.16f\nNew y value: %0.16f\nNew z value: %0.16f\nX Error: %0.16f\nY Error: %0.16f\nZ Error: %0.16f\nAverage Error:%0.16f\n\n"
            % (i, x_new, y_new, z_new, x_error, y_error, z_error, ave_error)
        )
        graph_arr_x.append(i)
        graph_arr_y.append(ave_error)
        if (ave_error < acceptable_error):
            print(
                "Acceptable Error Reached!\nResults\nX=%0.16f, Y=%0.16f, Z=%0.16f Error=%0.16f" %  
                (x_new, y_new, z_new, ave_error)
            )
            break
    
    plt.plot(graph_arr_x, graph_arr_y)
    plt.xlabel('Iteration')
    plt.ylabel('Error')
    plt.title('Jacobi Method')
    plt.show()

main()

