let app_controller = new Vue({
    el: "#app",
    data:{
        text: "ファイルを選んでください",
        prev_img:{
            is_loaded:false,
            bin: "",
            type: "",
        }
    },
    methods:{
        file_reader(e){
            this.prev_img.bin = e.currentTarget.result;
            this.prev_img.is_loaded = true;
            this.img_identify();
        },
        selected(e){
            let target = e.target.files[0];
            if(!target.type.match("image.*")){
                alert("画像ではありません");
                this.prev_img.is_loaded = false;
                return ;
            }

            const reader = new FileReader();
            reader.onload = this.file_reader;
            reader.readAsDataURL(target);

            this.text = "識別しています";
        },
        img_identify(){

            let formdata = new FormData();
            formdata.append("upload_img", this.prev_img.bin);
            $.ajax({
                type: "POST",
                url: "/chainer/identify_api",
                cacha:false,
                contentType: false,
                processData: false,
                data: formdata
            })
            .done(function(ajax_data){
                app_controller.text = ajax_data;
            })
            .fail(function(){
                app_controller.text = "APIへの通信が失敗しました。";
            });
        }
    }
})
