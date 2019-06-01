
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Column 2 from data table
A_input_chars = [1, 2, 3, 4]
B_input_chars = [1, 2, 3, 4, 5, 6, 7, 8]

# Column 3 and 4 from data table
# Replace list elements with your times
A_time = [0.00366687774658, 0.0219659805298, 0.177834033966, 1.78593206406,]
B_time = [0.00699019432068,0.00859713554382,0.0117418766022,0.0218880176544,0.0561180114746,0.178546905518,0.547641038895,1.65290808678]

fig, ax = plt.subplots(1,1)
# plot(x_list, y_list, "color and style")
ax.plot(A_input_chars, A_time, 'ro-', label='Algo. A') # red dots
ax.plot(B_input_chars, B_time, 'bo-', label='Algo. B') # blue dots

# Label and show
ax.set_xlabel ("Length of input in characters")
ax.set_ylabel("Execution time")
ax.set_title("Execution time vs. input length")
ax.legend(loc='center left') # Show and place the legend fig.set_facecolor('white')
fig.savefig('graph_data_1')