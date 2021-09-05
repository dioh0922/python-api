<?php
ini_set( 'display_errors', 1 );
	header('Content-Type: text/html; charset=UTF-8');
	try{
		$full = "";
		if(isset($_POST["lang"])){
			if($_POST["lang"] != ""){
				if($_POST["lang"] == "jpn"){
					$full = "python generate_sentence.py jpn";
				}else if($_POST["lang"] == "chn"){
					$full = "python generate_sentence.py chn";
				}
				exec($full, $out);

				foreach($out as $iter){
					echo $iter;
				}
			}
		}
	}catch(Exception $e){
		echo $e->getMessage();
	}
?>
