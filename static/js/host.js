(function($)
{
    var flag0 = false;
    var flag1 = false;
    var flag2 = false;
    var phone_number0;
    var phone_number1;
    var phone_number2;
    $.getJSON("http://127.0.0.1:8000/host/",
        function (data) {
            //alert("ID:" + data.id + "\nName:" + data.name);
            alert(111);
            for (var key in data) {
                var ttext = key;
                var phone_number = data[key];
                if (flag0 == false) {
                    phone_number0 = phone_number;
                    var div0 = document.getElementById("div0");
                    div0.style.display = "block";

                    var div0p = document.getElementById("div0p");

                    div0p.innerHTML = ttext;
                    flag0 = true;

                } else if (flag1 == false) {
                    phone_number1 = phone_number;

                    var div1 = document.getElementById("div1");
                    div1.style.display = "block";

                    var div1p = document.getElementById("div1p");

                    div1p.innerHTML = ttext;
                    flag1 = true;

                } else {
                    phone_number2 = phone_number;

                    var div2 = document.getElementById("div2");
                    div2.style.display = "block";

                    var div2p = document.getElementById("div2p");

                    div2p.innerHTML = ttext;
                    flag2 = true;

                }
            }

        });

    function cclick() {
        alert(123);
        $.getJSON("http://127.0.0.1:8000/host/",
            function (data) {
                //alert("ID:" + data.id + "\nName:" + data.name);
                alert(111);
                for (var key in data) {
                    var ttext = key;
                    var phone_number = data[key];
                    if (flag0 == false) {
                        phone_number0 = phone_number;
                        var div0 = document.getElementById("div0");
                        div0.style.display = "block";

                        var div0p = document.getElementById("div0p");

                        div0p.innerHTML = ttext;
                        flag0 = true;

                    } else if (flag1 == false) {
                        phone_number1 = phone_number;

                        var div1 = document.getElementById("div1");
                        div1.style.display = "block";

                        var div1p = document.getElementById("div1p");

                        div1p.innerHTML = ttext;
                        flag1 = true;

                    } else {
                        phone_number2 = phone_number;

                        var div2 = document.getElementById("div2");
                        div2.style.display = "block";

                        var div2p = document.getElementById("div2p");

                        div2p.innerHTML = ttext;
                        flag2 = true;

                    }
                }

            });

        // if(flag0==false){
        //     var ttext="牛肉披萨<br/>牛奶加咖啡";
        //
        //     var div0=document.getElementById("div0");
        //     div0.style.display="block";
        //
        //     var div0p=document.getElementById("div0p");
        //
        //     div0p.innerHTML=ttext;
        //     flag0=true;
        // }
        // else if(flag1==false){
        //     var ttext="鸡肉披萨<br/>可乐加冰";
        //
        //     var div1=document.getElementById("div1");
        //     div1.style.display="block";
        //
        //     var div1p=document.getElementById("div1p");
        //
        //     div1p.innerHTML=ttext;
        //     flag1=true;
        //
        // }
        // else{
        //     var ttext="薯条";
        //
        //     var div2=document.getElementById("div2");
        //     div2.style.display="block";
        //
        //     var div2p=document.getElementById("div2p");
        //
        //     div2p.innerHTML=ttext;
        //     flag2=true;
        //
        // }

    }


    function cclick_btn0() {
        var data = {};
        data["phone_number"] = phone_number0;

        var postData = JSON.stringify(data);

        $.ajax({
            url: 'http://127.0.0.1:8000/commit',
            type: 'get',
            data: {
                'data': postData,
                'test': "Hello"
            },
            traditional: true,//用传统方式序列化数据
            success: function (flag) {
                alert(flag)
            }
        })//通过设置traditional属性为true直接传递数组 */
    }

    function cclick_btn1() {
        var data = {};
        data["phone_number"] = phone_number1;

        var postData = JSON.stringify(data);

        $.ajax({
            url: 'http://127.0.0.1:8000/commit',
            type: 'get',
            data: {
                'data': postData,
                'test': "Hello"
            },
            traditional: true,//用传统方式序列化数据
            success: function (flag) {
                alert(flag)
            }
        })//通过设置traditional属性为true直接传递数组 */
    }

    function cclick_btn2() {
        var data = {};
        data["phone_number"] = phone_number2;

        var postData = JSON.stringify(data);

        $.ajax({
            url: 'http://127.0.0.1:8000/commit',
            type: 'get',
            data: {
                'data': postData,
                'test': "Hello"
            },
            traditional: true,//用传统方式序列化数据
            success: function (flag) {
                alert(flag)
            }
        })//通过设置traditional属性为true直接传递数组 */
    }

})(jQuery);