<?php

echo "hello world<br>";
echo date("Y-m-d H:i");
echo "<br>";

echo "<br>python<br>";
$out = [];
exec("python test.py test.jpg", $out, $ret);

var_dump($out);
var_dump($ret);
?>
