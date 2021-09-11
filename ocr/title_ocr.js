
var control_result = new Vue({
	el: "#result_area",
	data:{
		text: "ファイルを選んでください"
	}
});

var control_file_select = new Vue({
	el: "#load_img",
	methods:{
		selected: load_local_Image
	}
});

function load_local_Image(e){
	var file = e.target.files[0];
	if(!file.type.match("image.*")){
		alert("画像でない");
		return;
	}

	var blob = window.URL.createObjectURL(file);
	$("#resultImg").empty();
	$("#img_preview").attr("src", blob);
	control_result.text = "判別しています";
	get_img_title()
}

function img_select(e, txt){
	let post = {
		"target" : txt
	};

	$.ajax({
		type: "POST",
		url: "./get_title_api.php",
		cacha:false,
		data: post,
	})
	.done(function(ajax_data){
		control_result.text = ajax_data + "番の画像を抽出します";
	})
	.fail(function(){
		control_result.text = "OCRサーバへの通信が失敗しました。";
	});
}

function img_click(){
		$(document).trigger("img_select", [this.name]);
		$("#resultImg").empty();
}

function get_img_title(){

	var formdata = new FormData($("#img_form").get(0));

	$.ajax({
		type: "POST",
		url: "./get_area_api.php",
		cacha:false,
		contentType: false,
		processData: false,
		data: formdata,
		dataType: "html"
	})
	.done(function(ajax_data){
		control_result.text = ajax_data;
	})
	.fail(function(){
		control_result.text = "OCRサーバへの通信が失敗しました。";
	});

}

//起動時の処理
(window.onload = function(){
	//get_img_class();
});
