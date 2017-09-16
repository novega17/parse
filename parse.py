import csv
ACCEPTED_MSG = """
Hi Customer {}:

On {} the opening price of TSLA was {} and high was {}.

We are thrilled to let you know that your investment goal was acheived.

We look forward to seeing you on 11/1/2017 in our office for the investing seminar.
Thank you,
Workshop Organizers
"""

REJECTED_MSG = """
Hi Cusotmer {}:
On {} TSLA did not meet your requested price.
We are sorry to advise you that the workshop is now full.  
Thank you for your interest.
Workshop Organizers"""

csv_file = open('TSLA.csv')
csv_reader =csv.reader(csv_file, delimiter=',')
next(csv_reader)

for row in csv_reader:
    Cust, Date, Open, High, Low, Close, AdjClose, Volume = row
    msg = ACCEPTED_MSG.format(Cust,Date,Open,High)
    print("E-mail content:")
    print(msg)

csv_file.close()
