// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BankAccount {
    address public owner;
    uint public balance;

constructor() {
    owner = msg.sender;
}

function deposit() public payable {
    balance += msg.value;
}

function withdraw(uint amount) public {
    require(msg.sender == owner, "Only owner can withdraw");
    require(amount <= balance, "Insufficient Balance");
    balance -= amount;
    payable(owner).transfer(amount);
} 

function showBalance() public view returns (uint) {
    return balance;
} 
}