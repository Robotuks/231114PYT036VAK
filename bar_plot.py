import matplotlib.pyplot as plt


def plot_bar(fruits, counts, labels, bar_colors):

    fig, ax = plt.subplots()

    

    ax.bar(fruits, counts, label=labels, color=bar_colors)

    ax.set_ylabel('fruit supply')
    ax.set_title('Fruit supply by kind and color')
    ax.legend(title='Fruit color')

    plt.show()


fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [40, 100, 30, 55]
bar_labels = ['red', 'blue', 'red', 'orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

plot_bar( fruits, counts, bar_labels, bar_colors )