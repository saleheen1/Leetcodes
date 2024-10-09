class TimeMap:

    def __init__(self):
        self.hashData = {}
        

    def set(self, key, value, timestamp):
            if key not in self.hashData:
                 self.hashData[key] = []
            
            self.hashData[key].append([value,timestamp])

        

    def get(self, key, timestamp):
        res = ""
        values = self.hashData.get(key,[])
        left = 0
        right = len(values) -1

        while left <= right:
             mid = (left+right) // 2 
             if values[mid][1] <= timestamp:
                  res = values[mid][0]
                  left = mid+1
             else:
                  right = mid -1

        return res
             
