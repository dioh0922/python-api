let result_obj = new Vue({
    el: "#app",
    data: {
        text: "",
        generate_str: ""
    },
    methods:{
        generate(e){
            this.text = "生成しています";
            this.generate_str = "";
            $.ajax({
                type: "POST",
                url: "./markovify/generate_sentence_api",
                data: {
                    lang: e
                }
            }).done(function(response){
                result_obj.text = "";
                result_obj.generate_str = response;
            }).fail(function(){
                let str = "サーバとの通信に失敗しました";
                result_obj.text = str;
                alert(str);
            });
        }
    }
});

