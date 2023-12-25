
const svr = "http://localhost/ocr_relay_svr/";

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

var crop_obj = null;
var detected_title = "";

function load_local_Image(e){
	let file = e.target.files[0];
	if(!file.type.match("image.*")){
		alert("画像でない");
		return;
	}

	if(crop_obj != null){
		crop_obj.destroy();
	}

	$("#img_preview").empty();
	$("#title_img_view").empty();

	control_result.text = "タイトル部分を選択してください";

	$("<img>").attr({
		src: "",
		id: "prev_src",
		alt: "",
	}).appendTo("#img_preview");


	$("<input>").attr({
		type: "button",
		id: "send_crop_btn",
		value: "選択完了",
		class: "btn btn-success",
		style: "margin-top: 10px;",
	}).appendTo("#img_preview");


	let formdata = new FormData($("#img_form").get(0));
	let src = window.URL.createObjectURL(file);

	$("#prev_src").attr("src", src);
	$("#prev_src").ready(function(){
		let el = $("#prev_src").get(0);
		crop_obj = new Cropper(el,{
			cropend(event){
			}
		});
	});
}

function send_crop_img_to_api(){
	control_result.text = "識別しています";

	crop_obj.getCroppedCanvas().toBlob((blob) => {
		let formdata = new FormData();
		formdata.append("upload_img", blob);
		$.ajax({
			type: "POST",
			url: svr + "get_title_api.php",
			cacha:false,
			contentType: false,
			processData: false,
			data: formdata,
			dataType: "html"
		})
		.done(function(ajax_data){
			detected_title = ajax_data;
			control_result.text = "「" + detected_title + "」でした";
			//location.href = "http://google.co.jp/search?tbm=isch&q=" + detected_title;

			//連続で収集すると保存できないため画像検索にしておく
			get_img_result_word(ajax_data);
		})
		.fail(function(){
			control_result.text = "OCRサーバへの通信が失敗しました。";
		});
	}, "image/jpeg"); //jpeg形式にする(toBlob()そのままだとpngになる)
}

function get_img_result_word(txt){
	let post_data = {
	};

	post_data["search_word"] = txt;

	$.ajax({
		type: "POST",
		url: svr + "search_img_crawler.php",
		cacha:false,
		data: post_data,
	})
	.done(function(ajax_data){
		if(ajax_data == 0){
			control_result.text = "画像の収集に失敗しました";
		}else{
			let src_arr = ajax_data.split("<br>");
			for(let i = 0; i < src_arr.length - 1; i++){
				$("<img>").attr({
					src: src_arr[i],
					style: "margin-left: 10px; margin-bottom: 10px; width:40%; height: 40%; display: inline-block; padding: 10px;"
				}).appendTo("#title_img_view");
			}
			control_result.text = detected_title + "の画像を表示します";
			//$(window).trigger("crawler_comp");
		}
	})
	.fail(function(){
		control_result.text = "OCRサーバへの通信が失敗しました。";
	});

}

function get_img_src(){
	$.ajax({
		type: "GET",
		url: svr + "get_img_src_api.php",
		cacha:false,
	})
	.done(function(ajax_data){
		let src_arr = ajax_data.split("\n");
		for(let i = 0; i < src_arr.length - 1; i++){
			$("<img>").attr({
				src: src_arr[i],
				style: "margin-left: 10px; margin-bottom: 10px; width:40%; height: 40%; display: inline-block; padding: 10px;"
			}).appendTo("#title_img_view");
		}
		control_result.text = detected_title + "の画像を表示します";
	})
	.fail(function(){
		control_result.text = "OCRサーバへの通信が失敗しました。";
	});
}

//起動時の処理
(window.onload = function(){
	$(document).on("click", "#send_crop_btn", send_crop_img_to_api);
	$(window).on("crawler_comp", get_img_src);
});
