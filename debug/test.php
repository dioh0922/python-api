<?php

echo "hello world<br>";

exec("python test.py", $out);

foreach($out as $iter){
	echo $iter;
}

?>
