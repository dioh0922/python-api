<?php
	header('Content-Type: text/html; charset=UTF-8');

	//POSTしてきた画像でOCRするように変更する

	//ファイル名は引数で入力するように変更する

	$file_name = $_FILES["upload_img"]["tmp_name"];

	if(!is_uploaded_file($file_name)){
		print("画像ファイルが以上です");
		exit();
	}

	move_uploaded_file($file_name, $file_name);

	$full = "python call_ocr.py ".$file_name;
	exec($full, $out);

	foreach($out as $iter){
		echo $iter;
		echo ",";
	}

	unlink("./".$file_name);

?>
