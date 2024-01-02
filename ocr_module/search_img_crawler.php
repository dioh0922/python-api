<?php
	header('Content-Type: text/html; charset=UTF-8');

	$target = $_POST["search_word"];

	//$full = "python crawler.cgi ".$target;
	$full = "python get_sample_img_src.py ".$target;
	exec($full, $out);

/*
	$dir = "get_result/";
	$f_list = glob($dir."*");
	foreach ($f_list as $iter) {
		$dist_name = mb_substr($iter, -5);
		$trim_target = mb_substr($target, 0, 5);
		rename($iter, $dir.$trim_target.$dist_name);
	}

	if(count($f_list) <= 0){
		echo 0;
	}else{
		echo 1;
	}
*/

	foreach($out as $val){
		echo($val);
	}
?>
