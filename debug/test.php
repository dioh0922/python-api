<?php

echo "hello world<br>";
echo date("Y-m-d H:i");
echo "<br>";

echo "<br>python<br>";
$out = [];
exec("python test.py test.jpg", $out, $ret);

foreach($out as $iter){
	echo $iter;
}
var_dump($ret);
?>
