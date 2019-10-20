pragma solidity >=0.5.0;


contract TransactCall {

    uint private count;

    event FailedSet(int indexed _count);
    event FailedDecrement();
    event SuccessSet(uint indexed _count);

    function setCount(int _count) public payable {
        if (_count >= 0) {
            count = uint(_count);
            emit SuccessSet(count);
        } else {
            emit FailedSet(_count);
        }
    }

    function increment() public {
        count += 1;
    }

    function decrement() public {
        if (count > 0)
            count -= 1;
        else {
            emit FailedDecrement();
        }
    }

    function getCount() public view returns (uint) {
        return count;
    }
}
