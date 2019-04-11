'''Question 2'''    
import json

# Enter your code here. Read input from STDIN. Print output to STDOUT
report_df = []

def a(ls):
    return ls[3]
def b(ls):
    return ls[2]
def c(ls):
    return ls[1]
def d(ls):
    return ls[0]

lines = []
while True:
    try:
        line = input()
        #print(line)
        if line:
            lines.append(line)
        else:
            break
    except:
        break

JSON_report = '\n'.join(lines)
#print(JSON_report)
JSON_report = json.loads(JSON_report)
#print(JSON_report)
for record in JSON_report["report"]:
    for sub in record["subject"]:
        report_df.append([sub["code"],sub["grade"],record["enrollment"], record["name"]])

report_df = sorted(report_df, key = a)
report_df = sorted(report_df, key = b)
report_df = sorted(report_df, key = c)
report_df = sorted(report_df, key = d)

for rec in report_df:
    print(' '.join(rec))

# COM B rit2011020 Samantha
# {
#     "report":[
#         {
#             "enrollment": "rit2011001",
#             "name": "Julia",
#             "subject":[
#                 {
#                     "code": "DSA",
#                     "grade": "A"
#                 }
#             ]
#         },
