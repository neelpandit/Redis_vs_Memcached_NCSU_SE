# This script generates a list of closed issues along with the time it took 
# to close it in days. 
# It also computes the average resolutiont time and classifies the number of 
# issues in to groups with resolution time :
# 0 - 10
# 10- 50
# 50 - 100
# 100 - 500
# > 500
# 
# To run the file, run 'python issues.py <project name>' where <project name> 
# can take values redis or memcached. 


import requests
import dateutil.parser
import sys

headers = {"Authorization": "Bearer <API KEY>"}

project = sys.argv[1]
if project == "redis":
  owner = "antirez"
  repo = "redis"
elif project == "memcached":
  owner = "memcached"
  repo = "memcached"

f = open("%s.txt" % (repo), "w")

def run_query(query):
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

        
# The GraphQL query 
countQuery = """
{
  repository(owner: \"%s\", name: \"%s\") {
    issues(states: CLOSED, first: 1) {
      totalCount
      pageInfo {
        startCursor
        hasNextPage
      }
    }
  }
}
""" % (owner,repo)

result = run_query(countQuery)
repository = result["data"]["repository"]
pageInfo = repository["issues"]["pageInfo"]
totalCount = repository["issues"]["totalCount"]
startCursor1 = pageInfo["startCursor"]

hasNext = True
totalDays = 0
ten = 0
fifty = 0
hundred = 0
fiveHundred = 0
thousand = 0

while hasNext:

  issueDataQuery = """
  {
    repository(owner: \"%s\", name: \"%s\") {
      issues(states: CLOSED, after: \"%s\", first: 100) {
        nodes{
          number
          createdAt
          closedAt
        }
        pageInfo{
          endCursor
          hasNextPage
        }
      }
    }
  }
  """ % (owner,repo,startCursor1)

  result = run_query(issueDataQuery)
  repository = result["data"]["repository"]
  pageInfo = repository["issues"]["pageInfo"]
  hasNext = pageInfo["hasNextPage"]
  startCursor1 = pageInfo["endCursor"]

  for i in repository["issues"]["nodes"]:
    created = dateutil.parser.parse(i["createdAt"])
    closed = dateutil.parser.parse(i["closedAt"])
    days = (closed - created).days

    if days <= 10:
      ten += 1
    elif days <= 50:
      fifty += 1
    elif days <= 100:
      hundred += 1
    elif days <= 500:
      fiveHundred += 1
    else:
      thousand += 1

    f.write("%s - %d" % (i["number"],days))
    f.write("\r\n")
    totalDays += (closed - created).days

f.write("\r\n") 
f.write("Avg = %d days/issue" % (totalDays/totalCount))
f.write("\r\n") 
f.write("%d %d %d %d %d" %(ten,fifty,hundred,fiveHundred,thousand))