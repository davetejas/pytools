# Write a function that takes as its input a rational number a / b and returns its string representation.
# Examples:
# 5 / 4: 5, 4 => 1.25
# 1 / 3: 1, 3 => 0.(3)
# 1 / 6: 1, 6 => 0.1(6)
# 1 / 22: 1, 22 => 0.0(45) = 0.045454545454545456
# 45454545454545456 / 100 = 0.045454545454545456

# 4/2 = 2 
# 5/2 = 2.5 -> out = 2 r = 1 , r * 10 r -> 10  5 

# 1/3 -> 10/3 -> r = 1, out = 3/10

# psedocode

# chk num > deno

       # if rem < deno
       #      multi * 10 till its greater than deno
       #      div (recur) if patern continues add braces
            
#else
#      cal reminder

       # if rem < deno
       #      multi * 10 till its greater than deno
       #      div (recur) if patern continues add braces
            
        
# print(int(5/2))
# print(int(5%2))

# 1/3 = 0.33333333...
# 33/10 = 0.33
# 333/1000 = 0.333
# 3333/10000 = 0.3333
#print(3333333333333 / 1000000000000000)
# .33 .456

# 1.(33) 33 33 33

class Solve:
    def __init__(self):
        self.pattern = ""          # repeat pattern
        self.precision = ""        # Numbers on left of decimal 
        self.scale = ""            # Numbers on right on decimal MAX - 20 
        self.verbose = True
        

    # Helper func to build scale in a div output
    def helper(self,reminder, deno):

        # Halting condition
        # Max number after decimale is 20 char
        if len(self.scale) > 20:
            return
        
        count = 0
        while reminder <= deno:
            reminder = reminder * 10
            count += 1

        out = (int(reminder / deno))
        r = (reminder % deno)

        temp = "{}".format(out)
                
        # find repeat pattern to infinity
        if len(self.pattern) == 0:
            self.pattern = temp
        elif self.pattern != temp:
            self.pattern = temp
        
        if len(temp) < count:
            while len(temp) == count:
                count -= 1
                self.scale += "0"    
        else:
            self.scale += temp

        if self.verbose is True:
            print("S-{} R-{}".format(self.scale, r))

        if r == 0:
            return
        else:
            self.helper(r, deno)
    
    # get Division 
    def get_div(self, num: int, deno: int):

        if num >= deno:
            out = (int(num/deno))
            r = (num % deno)

            # Finding precision in the number i.e X in X.Y
            self.precision += "{}".format(out)    
            
            if self.verbose is True:
                print("Precision -> {}".format(self.precision))

            # Build scale in number i.e Y in X.Y
            if r != 0:
                self.helper(r, deno)
        else:
            self.helper(num, deno)
            
        self.build_result()
        
    # updates string if repeat to infinity pattern is found
    def parser(self):
        if self.verbose is True:
            print("--PARSER--")
        
        count = 0   
        temp = self.scale
        
        # following scans for pattern from the end. Any repeat pattern has to go till infinity
        # for every count of match we remove that of string and loop
        
        while len(temp) > 0:
            if self.verbose is True:
                print(temp)
            if temp[-(len(self.pattern)):] == self.pattern:
                count += 1
                temp = temp[:-(len(self.pattern))]
            else:
                break
        
        # overwrite scale if repeat found
        if count > 1:
            self.scale = temp + "(" + self.pattern + ")"
        
    # Assemble final result for output
    def build_result(self):
        
        #print ("Res - {}.{} - Pattern{}".format(self.precision, self.scale, self.pattern))

        if len(self.precision) == 0:
            self.precision = "0"
            
        if len(self.scale) == 0:
            self.scale = "0"
        
        # check if pattern - substring is repeating to infinity
        if len(self.scale) >= 20:
            self.parser()
            
        result = self.precision + "." + self.scale
            
        print ("output = {}".format(result))
        return result 
            
            
        
            
x = Solve()

# Test case normal div
#x.get_div(4,2)

# Test case num < deno
#x.get_div(1,2)

# Test case num == deno
#x.get_div(5,5)

# Test case repeat pattern
# 1 / 3: 1, 3 => 0.(3)
x.get_div(1,3)

# Test case other request
# 5 / 4: 5, 4 => 1.25
#x.get_div(5,4)

# 1 / 6: 1, 6 => 0.1(6)
#x.get_div(1,6)

# 1 / 22: 1, 22 # failing
#x.get_div(1,22)

    
    
