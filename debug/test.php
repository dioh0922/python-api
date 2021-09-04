<?php

echo "hello world<br>";
print(date("Y-m-d H:i"));
exec("python test.py", $out);

foreach($out as $iter){
	echo $iter;
}

?>
