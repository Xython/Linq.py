

from linq import Flow
import linq.standard

def test_Unboxed():
    Flow([(1, 2), (2, 3), (3, 2)]).Unboxed()


def test_Sum():
    Flow([(1, 2), (2, 3), (3, 2)]).Sum(lambda x, y: x + y)


def test_Enum():
    Flow([(1, 2), (2, 3), (3, 2)]).Enum()


def test_Map():
    Flow([(1, 2), (2, 3), (3, 2)]).Map(lambda x, y: x + y).ToTuple()

Flow([(1, 2), (2, 3)]).Then(lambda x: x); Flow([(1, 2), (2, 3)]).Then(lambda x, y: x + y)

def test_Filter():
    Flow([(1, 2), (2, 3), (3, 2)]).Filter(lambda x, y: x + y)
Flow([(1, 1), (2, 2), (3, 2)]).Filter(lambda x, y: x is y).Filter().Filter(lambda x: x!=(3, 2)).All()


def test_Each():
    Flow([(1, 2), (2, 3), (3, 2)]).Each(lambda x, y: x + y)

Flow([1, 2, 3, 4, 5]).Aggregate(max, min, sum).ToTuple()

def test_Zip():
    Flow([(1, 2), (2, 3), (3, 2)]).Zip( [(1, 2), (2, 2), (3, 3)] )


def test_Sorted():
    Flow([(1, 2), (2, 3), (3, 2)]).Sorted(lambda x, y: x + y)
Flow([1, 2, 3]).Sorted().Sorted(by=lambda x: -x)


def test_ArgSorted():
    Flow([(1, 2), (2, 3), (3, 2)]).ArgSorted(lambda x, y: x + y)
Flow([3, 2, 1]).ArgSorted(); Flow([(1,1),(2, 2), (3, 1)]).ArgSorted(by=lambda a, b: a*b).ToList()


def test_Group():
    Flow([(1, 2), (2, 3), (3, 2)]).Group(lambda x, y: x + y).ToTuple()
Flow([1, 1,  2, 3, 3]).Group().Map(lambda _ : (len(_), len(_))).Group(lambda a, b: a*b).ToTuple()


def test_GroupBy():
    Flow([(1, 2), (2, 3), (3, 2)]).GroupBy(lambda x, y: x + y).ToTuple()
Flow([1, 1, 1]).GroupBy().ToList()


def test_Take():
    Flow([(1, 2), (2, 3), (3, 2)]).Take(1).ToTuple()


def test_TakeIf():
    Flow([(1, 2), (2, 3), (3, 2)]).TakeIf(lambda x, y: x + y).ToTuple()
Flow([1,2,3]).TakeIf(lambda x: x%2).ToTuple()


def test_TakeWhile():
    Flow([(1, 2), (2, 3), (3, 2)]).TakeWhile(lambda x, y: x + y).ToTuple()
Flow([1, 2, 3, 4, 5, 6]).TakeWhile(lambda x: x<3).ToTuple()


def test_Drop():
    Flow([(1, 2), (2, 3), (3, 2)]).Drop(1)


def test_Skip():
    Flow([(1, 2), (2, 3), (3, 2)]).Skip(1)


def test_Concat():
    Flow([(1, 2), (2, 3), (3, 2)]).Concat( [(1, 2), (2, 2), (3, 3)] ).ToTuple()


def test_ToList():
    Flow([(1, 2), (2, 3), (3, 2)]).ToList()


def test_ToTuple():
    Flow([(1, 2), (2, 3), (3, 2)]).ToTuple()

Flow([(1, 1), (2, 2), (3, 3)]).ToDict()

def test_ToSet():
    Flow([(1, 2), (2, 3), (3, 2)]).ToSet()


def test_All():
    Flow([(1, 2), (2, 3), (3, 2)]).All(lambda x, y: x + y)
Flow([1, 1, 1]).All()


def test_Any():
    Flow([(1, 2), (2, 3), (3, 2)]).Any(lambda x, y: x + y)
Flow([1, 1, 1]).Any()


def test_Next():
    Flow((i for i in range(3))).Next()


def test_Extended():
    Flow([(1, 2), (2, 2), (3, 3)]).Extended( [(1, 2), (2, 2), (3, 3)] )


def test_Extend():
    Flow([(1, 2), (2, 2), (3, 3)]).Extend( [(1, 2), (2, 2), (3, 3)] )


def test_Sort():
    Flow([(1, 2), (2, 2), (3, 3)]).Sort(lambda x, y: x + y)


def test_Reverse():
    Flow([(1, 2), (2, 2), (3, 3)]).Reverse()


def test_Reversed():
    Flow([(1, 2), (2, 2), (3, 3)]).Reversed()


def test_Intersects():
    Flow({(1, 1), (2, 2), (3, 3)}).Intersects( [(1, 2), (2, 2), (3, 3)] )


def test_Union():
    Flow({(1, 1), (2, 2), (3, 3)}).Union( [(1, 2), (2, 2), (3, 3)] )

