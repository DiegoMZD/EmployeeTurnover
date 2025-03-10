import seaborn as sns
import matplotlib.pyplot as plt

def plt_hist(df, col, bins = 10):
    sns.histplot(data=df, x=col, bins = bins, )
    plt.show()

def plt_count_x(df, col, order=None):
    ax = sns.countplot(data=df, x=col, order=order)
    abs_values = df[col].value_counts().values
    ax.bar_label(container=ax.containers[0], labels=abs_values)
    plt.show()

def plt_count_y(df, col, order=None):
    ax = sns.countplot(data=df, y=col, order=order)
    abs_values = df[col].value_counts().values
    ax.bar_label(container=ax.containers[0], labels=abs_values)
    plt.show()