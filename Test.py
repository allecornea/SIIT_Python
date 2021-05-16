input = [
{'dept': '001', 'sku': 'foo', 'transId': 'uniqueId1', 'qty': 100},
{'dept': '001', 'sku': 'bar', 'transId': 'uniqueId2', 'qty': 200},
{'dept': '001', 'sku': 'foo', 'transId': 'uniqueId3', 'qty': 300},
{'dept': '002', 'sku': 'baz', 'transId': 'uniqueId4', 'qty': 400},
{'dept': '002', 'sku': 'baz', 'transId': 'uniqueId5', 'qty': 500},
{'dept': '002', 'sku': 'qux', 'transId': 'uniqueId6', 'qty': 600},
{'dept': '003', 'sku': 'foo', 'transId': 'uniqueId7', 'qty': 700}
]

from itertools import groupby
from operator import itemgetter

grouper = itemgetter("dept", "sku")
result = []
for key, grp in groupby(sorted(input, key = grouper), grouper):
    temp_dict = dict(zip(["dept", "sku"], key))
    temp_dict["qty"] = sum(item["qty"] for item in grp)
    result.append(temp_dict)

from pprint import pprint
print(sorted(input, key = grouper))
print('-------------------')
pprint(result)