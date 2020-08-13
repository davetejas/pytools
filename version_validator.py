# Is the version within the spec?
# -------------------------------
#
# At FOSSA, we work closely with build systems. Often, we need to simulate builds in order to analyze their behavior. Today, we're going to re-implement a small portion of a build system: version range resolution.
#
# In this session's exercise, we'll be implementing versionWithinSpec, a function that takes a "version" and a "spec" and tells us whether the version is within the spec.
#
#
# What is a version?
# ------------------
#
# A version is a string that consists of either:
#
# 1. An integer, OR
# 2. An integer followed by a period followed by an integer.
#
# Some example versions:
#
# - "36"
# - "1.35"
# - "2.0"
#
# A version that is a plain integer has an implicit ".0" appended to it. For example, "1" is equivalent to "1.0".
#
#
# What is a spec?
# ---------------
#
# A spec is a string composed of one or more constraints separated by commas.
#
# A constraint is a combination of an operator and a version.
#
# Some example constraints:
#
# - ">1.3"
# - "<=2"
# - ">=2.5"
#
# Some example specs:
#
# - ">1.3,<=2"
# - ">=2.5,<4"
# - ">0,<2 ,<3"
# - ">0, <3, >1.343.232"
# A version is within a spec if it satisfies all constraints of the spec.
# 


# Requirements

# ex : input -> version "1.4", spec ">1.3,<=2"



import json


'''
Solution Summary:

- parser build range for input string 
- helper func:
    - check 2 version return eq/>/< -> 0/1/-1
    - expand range as you parse version
- check given version
'''
    
class Version:
    def __init__(self):
        self.inc = [False,False]    # bools to inc version num or not in valid range
        self.start = None
        self.end = None
        
    # helper checks if new version is > old one
    # 1 -> new ver greater than old
    # 0 -> both equal
    # -1 -> new ver less than old
    def ver_compare(self, old: list, new: list) -> int:
        o = len(old)
        n = len(new)
        
        for i in range(min(o, n)):
            if old[i] == new[i]:
                continue
            if old[i] < new[i]:
                return 1
            if old[i] > new[i]:
                return -1

        
        if n > o:
            return 1
        elif n == o:
            return 0
        elif n < o:
            return -1
        
        
    # helper func to update range
    def update_range(self, curr: list, inc: bool):
        
        # set start version if its None
        if self.start is None:
            self.start = curr
            if inc is True:
                self.inc[0] = True
            return

        # set end version if its none and current is > than start
        # also update start if found lower range
        if self.end is None:  
            if self.ver_compare(self.start, curr) == 1:
                self.end = curr
                if inc is True:
                    self.inc[1] = True
            else:
                self.start = curr
                if inc is True:
                    self.inc[0] = True
            return

        # if start and end both are present check if range needs to expand

        if self.ver_compare(self.start, curr) == -1:
            self.start = curr
            if inc is True:
                self.inc[0] = True
            else:
                self.inc[0] = False
            return

        if self.ver_compare(self.end, curr) == 1:
            self.end = curr
            if inc is True:
                self.inc[1] = True
            else:
                self.inc[1] = False
            return
    
    # Parser parses string to build start-end version
    def parse_spec(self, spec: str):
        curr = None
        p = spec.split(',')
        
        for v in p:
            if v[1] == '=':
                curr = v[2:].split('.')
                self.update_range(curr, True)
                
            else:
                curr = v[1:].split('.')
                self.update_range(curr, False)
                    
        print("Range : {}-{} {}".format(self.start, self.end, self.inc))
        
    # check if given version, is in valid range
    # assumption we already have valid range build prior
    def check_version(self, ver: str) -> bool:
        v = ver.split('.')
        print(self.ver_compare(self.start, v))
        
        # check for <= or >= 
        if self.ver_compare(self.start, v) == 0:
            if self.inc[0] is True:
                return True
            else:
                return False
            
        if self.ver_compare(self.end, v) == 0:
            if self.inc[1] is True:
                return True
            else:
                return False
            
        if self.ver_compare(self.start, v) == -1:
            print("#3")
            return False
        
        if self.ver_compare(self.end, v) == 1:
            print("#4")
            return False
        
        return True




def version_within_spec(version, spec):
    """version_within_spec returns true if version is within the spec."""
    
    result = Version()
    result.parse_spec(spec)
    out = result.check_version(version)
    return out

tests = [
    {"version": "1", "spec": ">1.3,<=2", "expected": False},
    {"version": "3", "spec": ">=2.5,<4", "expected": True},
    {"version": "3", "spec": ">0,<2,<3", "expected": False},
]

for test in tests:
    result = version_within_spec(test["version"], test["spec"])

    if result == test["expected"]:
        print("OK: " + json.dumps(test["version"]) + ", " + json.dumps(test["spec"]))
    else:
        print()
        print("TEST CASE FAILED: " + json.dumps(test["version"]) + ", " + json.dumps(test["spec"]))
        print("Expected: " + json.dumps(test["expected"]))
        print("Actual: " + json.dumps(result))
        print()
