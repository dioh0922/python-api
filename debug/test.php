<?php

echo "hello world<br>";
echo date("Y-m-d H:i");
echo "<br>";

/*
exec("pip freeze", $out);

foreach($out as $iter){
	echo $iter;
}
*/

$out = [];
exec("python test.py", $out);

foreach($out as $iter){
	echo $iter;
}


?>
