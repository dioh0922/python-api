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

echo "env<br>";
echo getenv("TESSDATA_PREFIX");

echo "<br>which<br>";
$out = [];
exec("which tesseract", $out);

foreach($out as $iter){
	echo $iter;
}

echo "<br>env<br>";
$out = [];
exec("printenv", $out);

foreach($out as $iter){
	echo $iter;
}


echo "<br>-v<br>";
$out = [];
exec("tesseract -v", $out);

foreach($out as $iter){
	echo $iter;
}
var_dump($out);

echo "<br>python<br>";
$out = [];
exec("python call_ocr.py test.jpg", $out);

foreach($out as $iter){
	echo $iter;
}
var_dump($out);

?>
