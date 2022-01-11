sample = {
  "data": {
    "findByPortIds": [
      {
        "fundPortId": "0538",
        "parentPortId": "A172",
        "identifiers": [
          {
            "altId": "BlackRock",
            "altIdValue": "TIB2"
          },
          {
            "altId": "CUSIP",
            "altIdValue": "92211J209"
          },
          {
            "altId": "ISIN",
            "altIdValue": "US92211J2096"
          }
        ],
        "returnObjective": None,
        "peerFundAssociation": [],
        "targetMarketClientObjectivesReturnProfilePreservation": None,
        "fundCurrency": "United States of America, US Dollar",
        "marketRegistrations": [],
        "fundLeis": [],
        "orgInfo": [
          {
              "organizationRole": "Auditor",
              "attributeName": "Auditor Name",
              "attributeValue": "PricewaterhouseCoopers LLP"
          },
          {
              "organizationRole": "Auditor",
              "attributeName": "Organization ID",
              "attributeValue": "0000001061"
          }
        ],
        "benchmarkRelationships": [
          {
              "benchmarkAssociation": "Risk Free Rate",
              "benchmarkId": "0000000040",
              "benchmarkLongName": "FTSE Three-Month U.S. Treasury Bill Index"
          },
          {
              "benchmarkAssociation": "Primary Benchmark Characteristic",
              "benchmarkId": "0000022553",
              "benchmarkLongName": "Bloomberg Global Aggregate ex-USD Float Adjusted RIC Capped Index Hedged"
          }
        ],
        "distributionGroups": [
          {
              "distributionGroupCode": "G010",
              "distributionGroupName": "U.S. 40-ACT MUTUAL FUND"
          }
        ],
        "fundSplits": [],
        "fundMergers": []
      }
    ]
  }
}

print(sample['data']['findByPortIds'][0]['benchmarkRelationships'][0]['benchmarkAssociation'])
print(sample['data']['findByPortIds'][0]['distributionGroups'][0]['distributionGroupCode'])
print(sample['data']['findByPortIds'][0]['identifiers'][2]['altId'])

sample['data']['findByPortIds'][0]['marketRegistrations'].append({'name': 'Gazal', 'age': 32})
sample['data']['findByPortIds'][0]['marketRegistrations'].append({'name': 'Pritam', 'age': 32})
print(sample['data']['findByPortIds'][0]['marketRegistrations'])



# print G010
# print Risk Free Rate
# print ISIN

# add a new dictionary to marketRegistrations
# {'name': 'Gazal', 'age': 32}