#!/usr/bin/env python

def mean(numlist):
    """Calculate the mean of the values in numlist

    Input
    =====
    `numlist` (`list` or `tuple`) - List of values whose mean will be calculated. Example input, x = [1,5,3].

    Output
    ======
    (`float`) - Mean of the values in numlist
    
    """
    if type(numlist) == list and len(numlist) >= 1:

        flnumlist = []
        for i in numlist:
            try:
                n = float(i)
                flnumlist.append(n)
            except:
                CalcMean=0
                raise ValueError("numlist contains a non-numeric charcter"),str(n)
                break

        total = sum(flnumlist)
        length = len(flnumlist)

        return total/length
    else:
        print "Input is not a list or its an empty list"

##mean([])

if __name__ =="__main__":
##    import sys
##    if len(sys.argv) > 1:
##        numlist = []
##        for arg in sys.argv[1:]:
##            numlist.append(float(arg))
##   else:
     mean([1,2,2,4,5])
##    print mean(numlist)
