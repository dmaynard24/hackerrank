<?php

require_once("forward_references.php");

// I was too lazy to set up PHPUnit.. LOl
print(forwardReferences("tactactic")); // true
print("\n"); // true
print(forwardReferences("tactactictactictictac")); // false

?>