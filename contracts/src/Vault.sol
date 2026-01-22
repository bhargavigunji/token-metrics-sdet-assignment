
pragma solidity ^0.8.20;

contract Vault {
    mapping(address => uint256) public balances;
    uint256 public totalAssets;

    function deposit(uint256 amount) external {
        require(amount > 0, "amount zero");
        balances[msg.sender] += amount;
        totalAssets += amount;
    }

    function withdraw(uint256 amount) external {
        require(balances[msg.sender] >= amount, "insufficient");
        balances[msg.sender] -= amount;
        totalAssets -= amount;
    }
}
