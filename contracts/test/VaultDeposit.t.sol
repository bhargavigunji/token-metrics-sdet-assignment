pragma solidity ^0.8.20;

import "./fixtures/VaultFixture.sol";

contract VaultDepositTest is VaultFixture {
    function test_deposit_updates_balance_and_totalAssets() public {
        depositAs(user1, 100);

        assertEq(vault.balances(user1), 100);
        assertEq(vault.totalAssets(), 100);
    }

    function test_deposit_reverts_on_zero() public {
        vm.prank(user1);
        vm.expectRevert(bytes("amount zero"));
        vault.deposit(0);
    }


    function testFuzz_deposit_never_sets_wrong_total(uint96 amt) public {
    uint256 amount = uint256(amt) % 1_000_000;
    if (amount == 0) return;

    depositAs(user1, amount);
    assertEq(vault.totalAssets(), amount);
}

}
