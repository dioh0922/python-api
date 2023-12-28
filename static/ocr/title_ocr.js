
let crop_obj = null; //画像切り取り用オブジェクト

let app_controller = new Vue({
	el: "#app",
	data:{
		text: "",
		detect_title: "",
		is_init: false,
		is_selected: false,
        is_detected: false,
		file: {
			type: "",
			bin: "",
		}
	},
	methods:{
		selected(e){
			this.is_selected = true;
			let file = e.target.files[0];
			if(!file.type.match("image.*")){
				alert("画像でない");
				return;
			}else{
				this.file.type = file.type;
			}
		
			if(crop_obj != null){
				crop_obj.destroy();
			}
		
			$("#title_img_view").empty();
		
			this.text = "タイトル部分を選択してください";
				
			//let formdata = new FormData($("#img_form").get(0));
			let src = window.URL.createObjectURL(file);
		
			$("#prev_src").attr("src", src);
			$("#prev_src").ready(function(){
				let el = $("#prev_src").get(0);
				crop_obj = new Cropper(el,{
					cropend(event){
					}
				});
			});
		},
		submit(){
			this.text = "識別しています";
			console.log(crop_obj.getCroppedCanvas().toDataURL(this.file.type));

			this.file.bin = crop_obj.getCroppedCanvas().toDataURL(this.file.type);
			let formdata = new FormData();
			formdata.append("upload_img", this.file.bin);
			$.ajax({
				type: "POST",
				url: "./ocr/get_title_api",
				cacha:false,
				contentType: false,
				processData: false,
				data: formdata,
				dataType: "html"
			})
			.done(function(ajax_data){
				this.detect_title = ajax_data;
				this.text = "「" + this.detect_title + "」でした";
		
				//連続で収集すると保存できないため画像検索にしておく
				this.img_search(ajax_data);
			})
			.fail(function(){
				this.text = "OCRサーバへの通信が失敗しました。";
			});
		},
        img_search(txt){
            // 
            $.ajax({
                type: "POST",
                url: svr + "search_img_crawler.php",
                cacha:false,
                data: {
                    search_word: txt
                },
            })
            .done(function(ajax_data){
                if(ajax_data == 0){
                    this.text = "画像の収集に失敗しました";
                }else{
                    let src_arr = ajax_data.split("<br>");
                    for(let i = 0; i < src_arr.length - 1; i++){
                        $("<img>").attr({
                            src: src_arr[i],
                            style: "margin-left: 10px; margin-bottom: 10px; width:40%; height: 40%; display: inline-block; padding: 10px;"
                        }).appendTo("#title_img_view");
                    }
                    this.text = this.detect_title + "の画像を表示します";
                    //$(window).trigger("crawler_comp");
                }
            })
            .fail(function(){
                this.text = "OCRサーバへの通信が失敗しました。";
            });
        },
        crawler(){
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
                this.text = this.detect_title + "の画像を表示します";
            })
            .fail(function(){
                this.text = "OCRサーバへの通信が失敗しました。";
            });
        }
	},
	mounted(){
		this.is_init = true;
        this.text = "ファイルを選んでください";
	}
});


