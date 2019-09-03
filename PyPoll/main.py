def __main__():
    import os
    import csv

    # Path to collect data from the python-challenge folder
    poll_csv = os.path.join("../PyPoll", "election_data.csv")

    # Read in the CSV file
    with open(poll_csv, 'r') as csvfile:

        # Split the csv into a data list
        poll_data = list(csv.reader(csvfile, delimiter=','))

    # hold candidate votes in a dict
    candidate_votes = {}
    total_votes = len(poll_data) - 1
    winner = ''
    # Loop through the data
    for row in poll_data[1:]:
        # check to see if name in candidate_votes
        if row[2] in candidate_votes.keys():
            # index into the votes list, 2nd value is num of votes
            candidate_votes[row[2]][0][1] += 1
        # add a list of votes and 1
        else:
            candidate_votes[row[2]] = [['votes',1]]

    # add in percent, percentage to candidate votes dictionary
    for k,v in candidate_votes.items():
        # index into the votes num
        vote_percent = round((v[0][1]/total_votes)*100,2)
        candidate_votes[k] += [['percent', vote_percent]]
        if winner == '':
            winner = k
        else:
            if vote_percent > candidate_votes[winner][1][1]:
                winner = k


    # print findings
    def show_analysis():
        message = (('Election Results\n' +
            '--------------------------\n' +
            'Total Votes: {}\n' +
            '--------------------------\n' +
            'Khan: {}% ({})\n' +
            'Correy: {}% ({})\n' +
            'Li: {}% ({}))\n' +
            'O\'Tooley: {}% ({})\n' +
            '--------------------------\n' +
            'Winner: {}\n' +
            '--------------------------')
            .format(total_votes, candidate_votes['Khan'][1][1], candidate_votes['Khan'][0][1],
            candidate_votes['Correy'][1][1],candidate_votes['Correy'][0][1],
            candidate_votes['Li'][1][1],candidate_votes['Li'][0][1],
            candidate_votes['O\'Tooley'][1][1],candidate_votes['O\'Tooley'][0][1],
            winner))

        return message

    print(show_analysis())

    f = open("poll_analysis.txt","w+")
    f.write(show_analysis())
    f.close()


if __name__ == '__main__':
    __main__()
