//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MyContract {
    string private myStr;
    string[] private strArray;
    uint private counter = 0;

    function getCounter () public view returns (uint) {
        return counter;
    }

}