pragma solidity >=0.5.0;


/// @title TransactCall
/// @dev Contract of simple counter
contract Counter {
    /// Current value of the counter
    uint private count;

    /// Events where check of input takes place
    event FailedSet(int indexed value);
    event FailedDecrement();
    event SuccessSet(uint indexed value);

    /// @dev Function that saves new value in the state variable `count`
    /// @param value Value to assign
    function setCount(int value) public {
        if (value >= 0) {
            count = uint(value);
            emit SuccessSet(count);
        } else
            emit FailedSet(value);
    }

    /// @dev Function that increments the state variable `count`
    function increment() public {
        count += 1;
    }

    ///@dev Function that decrements the state variable `count`
    function decrement() public {
        if (count > 0)
            count -= 1;
        else
            emit FailedDecrement();
    }

    /// @dev Function that gets the current value of the counter
    /// @return uint that represents the current state of `count`
    function getCount() public view returns (uint) {
        return count;
    }
}
