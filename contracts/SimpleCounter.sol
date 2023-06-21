
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleCounter {
    uint private counter = 0;
    function increment() public {
        counter += 1;
    }

    function decrement() public {
        require(counter > 0, "Counter Value can not be decremented.");
        counter -= 1;
    }

    function getCounter() public view returns (uint)  {
        return counter;
    }
}
