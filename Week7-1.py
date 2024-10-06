# really confusing due to the conversion from c# to python, not because python is confusing. well, maybe a little.
def DisplayResults(candidates):
    # i kept having problems, and I went over and over before it was fixed, and now it works somehow. I don't know what I changed, but it works.
    if candidates["Candidate 1"] > 0 :
        print("Candidate 1 received", candidates["Candidate 1"], "votes.")
    if candidates["Candidate 2"] > 0:
        print("Candidate 2 received", candidates["Candidate 2"], "votes.")
    if candidates["Candidate 3"] > 0:
        print("Candidate 3 received", candidates["Candidate 3"], "votes.")
    if candidates["Candidate 4"] > 0:
        print("Candidate 4 received", candidates["Candidate 4"], "votes.")
    
# This makes more sense, CastVote here, then in C#
def CastVote(candidateName, candidates):
    candidates[candidateName] += 1     
        
def ResetVotes(candidates):
    candidates["Candidate 1"] = 0
    candidates["Candidate 2"] = 0
    candidates["Candidate 3"] = 0
    candidates["Candidate 4"] = 0

# initialized outside so it exists out of the loop
candidates = {
    "Candidate 1": 0,
    "Candidate 2": 0,
    "Candidate 3": 0,
    "Candidate 4": 0,
}

# honestly, this entire assignment was: finding basic conversions in w3school, then finding some other answers online, then trial and erroring my issues until they worked out.
# I think the issue was the parentheses from the c#. that was the last thing I changed before they started working
resetString = "Y"

while resetString != "N":
    print("Voting System")

    while True:
        print("Vote for a candidate by entering their number (1-4): ")
        
        vote = int(input())

        if vote == 0:
            break

        # I looked up if switch worked, which I don;t think it does. I did find something called match case, which we might;ve covered in class.
        # however, I have my own personal projects, so I have python 3.9.2, and match case is 3.10. So, i'll deal without it on MY computer, because I need 3.9.2.
        if vote == 1:
            CastVote("Candidate 1", candidates)
        elif vote == 2:
            CastVote("Candidate 2", candidates)
        elif vote == 3:
            CastVote("Candidate 3", candidates)
        elif vote == 4:
            CastVote("Candidate 4", candidates)
        else:
            print("What.")

# also I had DisplayResults on the furthest back line, which may also have been an issue.
    DisplayResults(candidates)

    while True:
        print("Do you want to reset the votes? Y/N")
        resetString = input()
        if resetString == "Y":
            ResetVotes(candidates)
            break
        elif resetString == "N":
            print("Exiting...")
            break
        else:
            print("Put Y or N")