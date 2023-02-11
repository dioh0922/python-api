let result_obj = new Vue({
	el: "#text_area",
	data: {
		text: ""
	}
});

let loading_txt = new Vue({
	el: "#loading",
	data: {
		text: ""
	}
});

function generate_sentence(lang){
	loading_txt.text = "生成しています";
	result_obj.text = "";

	$.ajax({
		type: "POST",
		url: "./generate_sentence_api.php",
		data: {
			lang: lang
		}
	}).done(function(response){
		loading_txt.text = "";
		result_obj.text = response;
	}).fail(function(){
		alert("サーバとの通信に失敗しました");
	});
}
