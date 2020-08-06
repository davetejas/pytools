# implement

# add_chunk() -> adds data in chunks
# remove_bytes -> rm n bytes from qeueu


                
class Solution:
    def __init__(self):
        self.q = bytearray()
        
    def dump_q(self):
        print("Current Size {} : Queue{}".format(len(self.q),self.q))
        
    def add_chunk(self, buf: list):
        # Each chunk of list keeps expanding the bytearray
        self.q += bytearray(buf)
        self.dump_q()
        
    def remove_q(self, num: int):
        print(len(self.q))
        
        result = []
        e = self.q.pop(0)
        result.append(e)
        
        #iterative solution
        while len(self.q) > 0:
            e = self.q.pop(0)
            result.append(e)
            if len(result) == num:
                break
        
        self.dump_q()
        return result
    

    
# Test case:

r = Solution() # init queue

# T1 : add following chunk
c1 = [1,2,3,4]
r.add_chunk(c1)

# T2: append to chunk
c2 = [9,99]
r.add_chunk(c2)

# T3: remove elements
r.remove_q(2)

# T4: overflow empty queue pop > sz of queue
r.remove_q(6)


# output 

# Finished in 52 ms
# Current Size 4 : Queuebytearray(b'\x01\x02\x03\x04')
# Current Size 6 : Queuebytearray(b'\x01\x02\x03\x04\tc')
# 6
# Current Size 4 : Queuebytearray(b'\x03\x04\tc')
# 4
# Current Size 0 : Queuebytearray(b'')





