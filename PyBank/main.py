def __main__():
    import csv
    import os
    import numpy as np

    budget_csv = os.path.join("../PyBank", "budget_data.csv")

    # read budget csv into a list
    with open(budget_csv, 'r') as csvfile:
        data = list(csv.reader(csvfile, delimiter=','))

    # get rid of header line
    ### data = np.array(data[1:])
    data = data[1:]

    # find month column
    ### total_months = len(data[:,0])
    total_months = len(data)

    # find profit column, read as integer instead of string
    ### profits_per_month = data[:,1]
    ### profits_per_month = profits_per_month.astype('int64')

    ### total_profit = np.sum(profits_per_month)  # add profits column
    total_profit = 0
    total_change = 0
    differences_per_month = []
    greatest_profit = 0
    greatest_loss = 0
    for i in range(total_months):
        total_profit += int(data[i][1])
        if i != (total_months - 1):
            change = int(data[i+1][1]) - int(data[i][1])
            total_change += change
            if change > greatest_profit:
                greatest_profit = change
                profit_index = i + 1
            if change < greatest_loss:
                greatest_loss = change
                loss_index = i + 1
            differences_per_month.append(change)

    average_change = round((total_change/(total_months-1)),2)
    greatest_month = data[profit_index][0]
    worst_month = data[loss_index][0]


    # # find differences between each profits row
    ### differences_per_month = np.diff(profits_per_month)
    # greatest_profit = max(differences_per_month) # look for largest profit change,
    ### profit_index = np.where(differences_per_month == greatest_profit) # collect index
    # greatest_loss = min(differences_per_month) # look for largest loss change,
    ### loss_index = np.where(differences_per_month == greatest_loss) # collect index
    #
    # # average change is the total differences / how many changes
    ### total_differences = np.sum(differences_per_month)
    # average_change = total_differences/(total_months-1)
    # average_change = round(average_change, 2)
    #
    # # index slicing for the largest profit | largest loss month
    ### greatest_month = data[profit_index[0] + 1][0][0]
    ### worst_month = data[loss_index[0] + 1][0][0]
    #
    #


    # print findings
    def show__analysis():
        message = (('Fianancial Analysis\n' +
             '--------------------------\n' +
             'Total Months: {}\n' +
             'Total: ${}\n' +
             'Average Change: ${}\n' +
             'Greatest Increase in Profits: {} (${})\n' +
             'Greatest Decrease in Profits: {} (${})\n')
             .format(total_months,total_profit,average_change,greatest_month,greatest_profit,worst_month,greatest_loss))

        return message

    print(show__analysis())

    f = open("financial_analysis.txt","w+")
    f.write(show__analysis())
    f.close()


if __name__ == '__main__':
    __main__()
