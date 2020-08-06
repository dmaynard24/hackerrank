<?php

function forwardReferences($test_s) {  
  return preg_match('/^(\2tic|(tac))+$/', $test_s, $output_array) ? "true" : "false";
}

?>
