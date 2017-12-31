

from linq import Flow

def test_Sum():
    Flow([(1, 2), (2, 3), (3, 2)]).Sum(lambda x, y: x + y)
test_Sum()

def test_Enum():
    Flow([(1, 2), (2, 3), (3, 2)]).Enum()
test_Enum()

def test_Map():
    Flow([(1, 2), (2, 3), (3, 2)]).Map(lambda x, y: x + y).ToTuple()
test_Map()

def test_Then():
    Flow([(1, 2), (2, 3)]).Then(lambda x: x); Flow([(1, 2), (2, 3)]).Then(lambda x, y: x + y)
test_Then()

def test_Scan():
    Flow([2, 3, 5]).Scan(lambda last, now: last + now, 0).ToList()
test_Scan()

def test_Filter():
    Flow([(1, 2), (2, 3), (3, 2)]).Filter(lambda x, y: x + y);Flow([(1, 1), (2, 2), (3, 2)]).Filter(lambda x, y: x is y).Filter().Filter(lambda x: x!=(3, 2)).All()
test_Filter()

def test_Each():
    Flow([(1, 2), (2, 3), (3, 2)]).Each(lambda x, y: x + y)
test_Each()

def test_Aggregate():
    Flow([1, 2, 3, 4, 5]).Aggregate(max, min, sum).ToTuple()
test_Aggregate()

def test_Zip():
    Flow([(1, 2), (2, 3), (3, 2)]).Zip( [(1, 2), (2, 2), (3, 3)] )
test_Zip()

def test_Sorted():
    Flow([(1, 2), (2, 3), (3, 2)]).Sorted(lambda x, y: x + y);Flow([1, 2, 3]).Sorted().Sorted(by=lambda x: -x)
test_Sorted()

def test_ArgSorted():
    Flow([(1, 2), (2, 3), (3, 2)]).ArgSorted(lambda x, y: x + y);Flow([3, 2, 1]).ArgSorted(); Flow([(1,1),(2, 2), (3, 1)]).ArgSorted(by=lambda a, b: a*b).ToList()
test_ArgSorted()

def test_Group():
    Flow([(1, 2), (2, 3), (3, 2)]).Group(lambda x, y: x + y).ToTuple();Flow([1, 1,  2, 3, 3]).Group().Map(lambda _ : (len(_), len(_))).Group(lambda a, b: a*b).ToTuple()
test_Group()

def test_GroupBy():
    Flow([(1, 2), (2, 3), (3, 2)]).GroupBy(lambda x, y: x + y).ToTuple();Flow([1, 1, 1]).GroupBy().ToList()
test_GroupBy()

def test_Take():
    Flow([(1, 2), (2, 3), (3, 2)]).Take(1).ToTuple()
test_Take()

def test_TakeIf():
    Flow([(1, 2), (2, 3), (3, 2)]).TakeIf(lambda x, y: x + y).ToTuple();Flow([1,2,3]).TakeIf(lambda x: x%2).ToTuple()
test_TakeIf()

def test_TakeWhile():
    Flow([(1, 2), (2, 3), (3, 2)]).TakeWhile(lambda x, y: x + y).ToTuple();Flow([1, 2, 3, 4, 5, 6]).TakeWhile(lambda x: x<3).ToTuple()
test_TakeWhile()

def test_Drop():
    Flow([(1, 2), (2, 3), (3, 2)]).Drop(1)
test_Drop()

def test_Skip():
    Flow([(1, 2), (2, 3), (3, 2)]).Skip(1)
test_Skip()

def test_Concat():
    Flow([(1, 2), (2, 3), (3, 2)]).Concat( [(1, 2), (2, 2), (3, 3)] ).ToTuple()
test_Concat()

def test_ToList():
    Flow([(1, 2), (2, 3), (3, 2)]).ToList()
test_ToList()

def test_ToTuple():
    Flow([(1, 2), (2, 3), (3, 2)]).ToTuple()
test_ToTuple()

def test_ToDict():
    Flow([(1, 1), (2, 2), (3, 3)]).ToDict()
test_ToDict()

def test_ToSet():
    Flow([(1, 2), (2, 3), (3, 2)]).ToSet()
test_ToSet()

def test_All():
    Flow([(1, 2), (2, 3), (3, 2)]).All(lambda x, y: x + y);Flow([1, 1, 1]).All()
test_All()

def test_Any():
    Flow([(1, 2), (2, 3), (3, 2)]).Any(lambda x, y: x + y);Flow([1, 1, 1]).Any()
test_Any()

def test_Next():
    Flow((i for i in range(3))).Next()
test_Next()

def test_Extended():
    Flow([(1, 2), (2, 2), (3, 3)]).Extended( [(1, 2), (2, 2), (3, 3)] )
test_Extended()

def test_Extend():
    Flow([(1, 2), (2, 2), (3, 3)]).Extend( [(1, 2), (2, 2), (3, 3)] )
test_Extend()

def test_Sort():
    Flow([(1, 2), (2, 2), (3, 3)]).Sort(lambda x, y: x + y)
test_Sort()

def test_Reverse():
    Flow([(1, 2), (2, 2), (3, 3)]).Reverse()
test_Reverse()

def test_Reversed():
    Flow([(1, 2), (2, 2), (3, 3)]).Reversed()
test_Reversed()

def test_Intersects():
    Flow({(1, 1), (2, 2), (3, 3)}).Intersects( [(1, 2), (2, 2), (3, 3)] )
test_Intersects()

def test_Union():
    Flow({(1, 1), (2, 2), (3, 3)}).Union( [(1, 2), (2, 2), (3, 3)] )
test_Union()
