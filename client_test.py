import unittest
from client3 import getDataPoint

class Client Test (unittest. TestCase): 
def test_getDataPoint_calculatePrice(self):
quotes [
{'top_ask': {'price': 121.2, 'size': 36},
'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}
id': 0.109974697771', 'stock': 'ABC' },
{'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
'top_bid': {'price': 117.87, 'size': 81}, 'id': 0.109974697771', 'stock': 'DEF'}

for i in quotes:
self.assertEqual (getDataPoint (i), (i
["stock"],i['bid_price'], i['ask_price'], (i ["bid_price']+i['ask_price'])/2))

def
test_getDataPoint_calculatePriceBidGreaterThan Ask(self):
quotes =[
 {'top_ask': {'price': 119.2, 'size': 36},
  'timestamp': '2019-02-11 22:06:30.572453', 
  'top_bid': {'price': 120.48, 'size': 109} , 
  'id': '0.109974697771', 'stock': 'ABC' },
  {'top_ask': {'price': 121.68, 'size': 4},
    'timestamp': '2019-02-11 22:06:30.572453',
    'top_bid': {'price': 117.87, 'size': 81},
    'id': '0.109974697771', 'stock': 'DEF'}
  }
  for i in quotes:
  self.assertEqual (getDataPoint(i),
   (i ['stock'], i['bid price'], 
    i['ask_price'], 
   (i ['bid_price']+il ask_price'])/2))
    
    if__name__='__main__':
      unittest.main()
                                                                                  
                                                                                  
