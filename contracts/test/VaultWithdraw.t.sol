pragma solidity ^0.8.20;

import "./fixtures/VaultFixture.sol";

contract VaultWithdrawTest is VaultFixture {
    function test_withdraw_reduces_balance_and_totalAssets() public {
        depositAs(user1, 200);

        withdrawAs(user1, 50);

        assertEq(vault.balances(user1), 150);
        assertEq(vault.totalAssets(), 150);
    }

    function test_withdraw_reverts_if_insufficient() public {
        vm.prank(user1);
        vm.expectRevert(bytes("insufficient"));
        vault.withdraw(1);
    }
}
