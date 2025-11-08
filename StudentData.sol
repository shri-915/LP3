// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {
    struct Student {
        string Name;
        uint rollno;
        uint age;
    }
    Student[] public students;

    // Add this to handle direct ETH transfers
    receive() external payable {}

    fallback() external payable {}

    function addStudent(string memory _name, uint _age, uint _rollno) public {
        students.push(Student(_name, _rollno, _age));
    }

    function getStudent(uint index) public view returns (string memory, uint, uint) {
        require(index <= students.length, "Index out of bounds");
        Student memory s = students[index-1];
        return (s.Name, s.age, s.rollno);
    }

    function getTotalStudents() public view returns (uint) {
        return students.length;
    }
}