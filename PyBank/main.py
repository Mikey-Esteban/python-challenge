def __main__():
    import pandas as pd
    import csv
    import numpy as np


    #df = pd.read_csv('budget_data.csv')
    #print(df)
    #total_rows = df.count()
    #print(total_rows)

    with open("budget_data.csv", 'r') as file:
        data = list(csv.reader(file, delimiter=','))
    data = np.array(data[1:])
    #months = np.genfromtxt("budget_data.csv", delimiter = ',', skip_header=1)
    months = len(data)


    total = data[:,1]
    total = total.astype('int64')
    #print(total)
    total_profit = np.sum(total)

    differences = np.diff(total)

    greatest_profit = max(differences)
    #print('greatest profit TYPE issssssss ', type(greatest_profit))
    profit_index = np.where(differences == greatest_profit)

    greatest_loss = min(differences)
    loss_index = np.where(differences == greatest_loss)



    total_differences = np.sum(differences)
    average_change = total_differences/(months-1)

    #print('type of total', type(total))
    #print('sliced array', total)
    print('Total Months:', months)
    print('Total: $' + str(total_profit))
    print('Average Change: $' + str(round(average_change, 2)))
    #print('greatest profit: ', max(differences))
    #print('greatest loss: ', min(differences))
    #print('profit index: ', profit_index)
    # print('loss index: ', loss_index)
    greatest_month = data[profit_index[0] + 1][0][0]
    #print('loss index: ', loss_index)
    worst_month = data[loss_index[0] + 1][0][0]
    print('Greatest Increase in Profits: ' + greatest_month + ' ($' + str(greatest_profit) + ')')
    print('Greatest Decrease in Profits: '+ worst_month + ' ($' + str(greatest_loss) + ')')



if __name__ == '__main__':
    __main__()
