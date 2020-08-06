<?php

require_once("branch_reset_groups.php");

// I was too lazy to set up PHPUnit.. LOl
print(branchResetGroups("12-34-56-78")); // true
print("\n"); // true
print(branchResetGroups("---12---34---56---78")); // false

?>