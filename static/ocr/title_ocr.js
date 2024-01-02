
let crop_obj = null; //画像切り取り用オブジェクト

let app_controller = new Vue({
    el: "#app",
    data:{
        text: "",
        detect_title: "",
        is_init: false,
        is_selected: false,
        file: {
            type: "",
            bin: "",
        },
        img_list: []
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
                app_controller.detect_title = ajax_data;
                app_controller.text = "「" + app_controller.detect_title + "」でした";
        
                //連続で収集すると保存できないため画像検索にしておく
                app_controller.img_search(ajax_data);
            })
            .fail(function(){
                app_controller.text = "OCRサーバへの通信が失敗しました。";
            });
        },
        img_search(txt){
            $.ajax({
                type: "POST",
                url: "./ocr/get_image_api",
                cacha:false,
                data: {
                    search_word: txt
                },
            })
            .done(function(ajax_data){
                if(ajax_data == 0){
                    app_controller.text = "画像の収集に失敗しました";
                }else{
                    app_controller.img_list = ajax_data.split("<br>");
                    app_controller.img_list = app_controller.img_list.filter(el => el != "");
                    app_controller.text = app_controller.detect_title + "の画像を表示します";
                }
            })
            .fail(function(){
                app_controller.text = "OCRサーバへの通信が失敗しました。";
            });
        }
    },
    mounted(){
        this.is_init = true;
        this.text = "ファイルを選んでください";
    }
});


