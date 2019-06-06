
    var flag0 = false;
    var flag1 = false;
    var flag2 = false;
    var phone_number0=1234;
    var phone_number1=5678;
    var phone_number2=78910;


    function cclick() {
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

    };


    function cclick_btn00() {
        alert(111);
        var data = {};
        data["phone_number"] = document.getElementById("div0phone").innerHTML;

        var postData = JSON.stringify(data);

        $.ajax({
            url: 'http://127.0.0.1:8000/inform_takefood/',
            type: 'get',
            data: {
                'data': postData,
            },
            traditional: true,//用传统方式序列化数据
            success: function (flag) {
                alert(flag)
            }
        })//通过设置traditional属性为true直接传递数组 */
    };
    function cclick_btn01() {
        var data = {};
        data["phone_number"] = document.getElementById("div0phone").innerHTML;

        var postData = JSON.stringify(data);

        $.ajax({
            url: 'http://127.0.0.1:8000/inform_text/',
            type: 'get',
            data: {
                'data': postData,
            },
            traditional: true,//用传统方式序列化数据
            success: function (flag) {
                alert(flag)
            }
        })//通过设置traditional属性为true直接传递数组 */
    }
    function cclick_btn02() {
        var data = {};
        data["phone_number"] = document.getElementById("div0phone").innerHTML;

        var postData = JSON.stringify(data);

        $.ajax({
            url: 'http://127.0.0.1:8000/inform_phone/',
            type: 'get',
            data: {
                'data': postData,
            },
            traditional: true,//用传统方式序列化数据
            success: function (flag) {
                alert(flag)
            }
        })//通过设置traditional属性为true直接传递数组 */
    }
    function cclick_btn03() {
        var data = {};
        data["phone_number"] = document.getElementById("div0phone").innerHTML;

        var postData = JSON.stringify(data);

        $.ajax({
            url: 'http://127.0.0.1:8000/inform_kitchen/',
            type: 'get',
            data: {
                'data': postData,
            },
            traditional: true,//用传统方式序列化数据
            success: function (flag) {
                alert(flag)
            }
        })//通过设置traditional属性为true直接传递数组 */
    }

    function cclick_btn10() {
        alert(777);
        var data = {};
        data["phone_number"] = document.getElementById("div1phone").innerHTML;

        var postData = JSON.stringify(data);

        $.ajax({
            url: 'http://127.0.0.1:8000/inform_takefood/',
            type: 'get',
            data: {
                'data': postData,
            },
            traditional: true,//用传统方式序列化数据
            success: function (flag) {
                alert(flag)
            }
        })//通过设置traditional属性为true直接传递数组 */
    }
    function cclick_btn11() {
        var data = {};
        data["phone_number"] = document.getElementById("div1phone").innerHTML;

        var postData = JSON.stringify(data);

        $.ajax({
            url: 'http://127.0.0.1:8000/inform_text/',
            type: 'get',
            data: {
                'data': postData,
            },
            traditional: true,//用传统方式序列化数据
            success: function (flag) {
                alert(flag)
            }
        })//通过设置traditional属性为true直接传递数组 */
    }
    function cclick_btn12() {
        var data = {};
        data["phone_number"] = document.getElementById("div1phone").innerHTML;

        var postData = JSON.stringify(data);

        $.ajax({
            url: 'http://127.0.0.1:8000/inform_phone/',
            type: 'get',
            data: {
                'data': postData,
            },
            traditional: true,//用传统方式序列化数据
            success: function (flag) {
                alert(flag)
            }
        })//通过设置traditional属性为true直接传递数组 */
    }
    function cclick_btn13() {
        var data = {};
        data["phone_number"] = document.getElementById("div1phone").innerHTML;

        var postData = JSON.stringify(data);

        $.ajax({
            url: 'http://127.0.0.1:8000/inform_kitchen/',
            type: 'get',
            data: {
                'data': postData,
            },
            traditional: true,//用传统方式序列化数据
            success: function (flag) {
                alert(flag)
            }
        })//通过设置traditional属性为true直接传递数组 */
    };

    function cclick_btn20() {
        var data = {};
        data["phone_number"] = document.getElementById("div2phone").innerHTML;

        var postData = JSON.stringify(data);
        alert("before");

         $.ajax({
            url: 'http://127.0.0.1:8000/inform_takefood/',
           type: 'GET',
            data: {'data':postData,
                    },
            traditional:true,//用传统方式序列化数据
            success:function(flag){
                alert(flag)
            }
        });
        alert("lalallaalala");
    };
    function cclick_btn21() {
        var data = {};
        data["phone_number"] = document.getElementById("div2phone").innerHTML;

        var postData = JSON.stringify(data);

        $.ajax({
            url: 'http://127.0.0.1:8000/inform_text/',
            type: 'get',
            data: {
                'data': postData,
            },
            traditional: true,//用传统方式序列化数据
            success: function (flag) {
                alert(flag)
            }
        })//通过设置traditional属性为true直接传递数组 */
    }
    function cclick_btn22() {
        var data = {};
        data["phone_number"] = document.getElementById("div2phone").innerHTML;

        var postData = JSON.stringify(data);

        $.ajax({
            url: 'http://127.0.0.1:8000/inform_phone/',
            type: 'get',
            data: {
                'data': postData,
            },
            traditional: true,//用传统方式序列化数据
            success: function (flag) {
                alert(flag)
            }
        })//通过设置traditional属性为true直接传递数组 */
    }
    function cclick_btn23() {
        var data = {};
        data["phone_number"] = document.getElementById("div2phone").innerHTML;

        var postData = JSON.stringify(data);

        $.ajax({
            url: 'http://127.0.0.1:8000/inform_kitchen/',
            type: 'get',
            data: {
                'data': postData,
            },
            traditional: true,//用传统方式序列化数据
            success: function (flag) {
                alert(flag)
            }
        })//通过设置traditional属性为true直接传递数组 */
    }
