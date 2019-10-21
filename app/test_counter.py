import counter
import coverage


counter.Counter.connect()
instance = counter.Counter()


def testGet():
    instance.setCount(65535)
    assert instance.getCount() == 65535


def testIncrement():
    instance.setCount(655)
    instance.increment()
    assert instance.getCount() == 656


def testSet():
    instance.setCount(3333333)
    assert instance.getCount() == 3333333


def testNegativeDecrement():
    instance.setCount(0)
    assert instance.decrement() == False


def testComplex():
    instance.setCount(65535)
    instance.increment()
    instance.decrement()
    assert instance.getCount() == 65535


def testNegativeSet():
    assert instance.setCount(-3) == False
