class Solver:
    def __init__(self):
        self.s=0
        
    def solve(self,*args):
        self.s+=sum(args)
        def recurse(*kwargs):
            self.s+=sum(kwargs)
            return self.solve
        return recurse

o=Solver()
o.solve(2,3,2)(10,3)(3,3)(2,10)(10,4)
print(o.s)
