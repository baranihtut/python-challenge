import csv

load = "election_data.csv"
output_export = "election_analysis.txt"

total = 0

candidateOptions = []
candidateVotes = {}

winning_candidate = ""
winning_counter = 0

with open(load) as data:
    reader = csv.reader(data)

    for row in reader:
        total = total + 1

        candidateName = row[2]

        if candidateName not in candidateOptions:

            candidateOptions.append(candidateName)

            candidateVotes[candidateName] = 0

        candidateVotes[candidateName] = candidateVotes[candidateName] + 1

with open(output_export, "w") as txt_file:

    results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total}\n"
        f"-------------------------\n"
    )
    print(results)


    txt_file.write(results)

    for candidate in candidateVotes:

        votes = candidateVotes.get(candidate)
        votePercent = float(votes) / float(total) * 100

        if (votes > winning_counter):
            winning_counter = votes
            winning_candidate = candidate

        voterOutput = f"{candidate}: {votePercent:.3f}% ({votes})\n"
        print(voterOutput)

        txt_file.write(voterOutput)

    summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n"
    )
    print(summary)

    txt_file.write(summary)
