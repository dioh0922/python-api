<?php

echo "hello world<br>";
print(date("Y-m-d H:i"));
exec("pip freeze", $out);

foreach($out as $iter){
	echo $iter;
}

/*
$out = [];
exec("python test.py", $out);

foreach($out as $iter){
	echo $iter;
}
*/

?>
