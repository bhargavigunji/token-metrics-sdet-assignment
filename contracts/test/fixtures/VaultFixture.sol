pragma solidity ^0.8.20;

import "forge-std/Test.sol";
import "../../src/Vault.sol";

contract VaultFixture is Test {
    Vault internal vault;
    address internal user1;
    address internal user2;

    function setUp() public virtual {
        vault = new Vault();
        user1 = makeAddr("user1");
        user2 = makeAddr("user2");
    }

    function depositAs(address user, uint256 amount) internal {
        vm.prank(user);
        vault.deposit(amount);
    }

    function withdrawAs(address user, uint256 amount) internal {
        vm.prank(user);
        vault.withdraw(amount);
    }
}
