from matplotlib import pyplot as mpl


def pretty_print(list):
    for item in range(list):
        print(f"{item}\n")


def print_pie_chart(dictionary):

    labels = list(dictionary.keys())
    values = list(dictionary.values())

    mpl.pie(values, labels=labels, autopct='%1.1f%%')
    mpl.axis('equal')

    mpl.show()


def print_pie_chart_from_lists(list_of_labels, list_of_values):
    labels = list(list_of_labels)
    values = list(list_of_values)

    mpl.pie(values, labels=labels, autopct='%1.1f%%')
    mpl.axis('equal')

    mpl.show()