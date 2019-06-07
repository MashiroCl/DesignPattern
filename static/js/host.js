
    var flag0 = false;
    var flag1 = false;
    var flag2 = false;
    var phone_number0=1234;
    var phone_number1=5678;
    var phone_number2=78910;





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
