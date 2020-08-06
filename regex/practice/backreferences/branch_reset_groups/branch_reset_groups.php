<?php

function branchResetGroups($test_s) {  
  return preg_match('/^\d\d(?|(-)|(:)|(---)|(\.))\d\d\1\d\d\1\d\d$/', $test_s, $output_array) ? "true" : "false";
}

?>
