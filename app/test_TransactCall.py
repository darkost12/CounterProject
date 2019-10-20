import TransactCall
import coverage


TransactCall.Counter.connect()
instance = TransactCall.Counter()


def testGet():
    #TransactCall.Counter.setCount(instance, 65535)
    #assert TransactCall.Counter.getCount(instance) == 65535
    instance.setCount(65535)
    assert instance.getCount() == 65535


def testIncrement():
    #TransactCall.Counter.setCount(instance, 655)
    #TransactCall.Counter.increment(instance)
    #assert TransactCall.Counter.getCount(instance) == 656
    instance.setCount(655)
    instance.increment()
    assert instance.getCount() == 656


def testSet():
    #TransactCall.Counter.setCount(instance, 3333333)
    #assert TransactCall.Counter.getCount(instance) == 3333333
    instance.setCount(3333333)
    assert instance.getCount() == 3333333

def testNegativeDecrement():
    #TransactCall.Counter.setCount(instance, 0)
    #assert TransactCall.Counter.decrement(instance) == False
    instance.setCount(0)
    assert instance.decrement() == False


def testComplex():
    #TransactCall.Counter.setCount(instance, 65535)
    #TransactCall.Counter.increment(instance)
    #TransactCall.Counter.decrement(instance)
    #assert TransactCall.Counter.getCount(instance) == 65535
    instance.setCount(65535)
    instance.increment()
    instance.decrement()
    assert instance.getCount() == 65535


def testNegativeSet():
    #assert TransactCall.Counter.setCount(instance, -3) == False
    assert instance.setCount(-3) == False
