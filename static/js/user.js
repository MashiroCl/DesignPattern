var tttext0="请输入手机号码";
var tttext1="";
var data={};
    function ccclick(){
    document.getElementById("phone").value = tttext1;
    }
    function cclick_again(){

        var postData =  JSON.stringify(data);

        $.ajax({
            url: 'http://127.0.0.1:8000/commit/',
            type: 'GET',
            data: {'data':postData,
            },
            traditional:true,//用传统方式序列化数据
            success:function(flag){
                alert(flag)
            }
        })//通过设置traditional属性为true直接传递数组 */
        alert("再来一单成功！");
    }
    //删除ObjData相关
    function cclick(){

        var div0 = document.getElementById("button_again");
        div0.style.display = "block";
        var key="milk";
        obj=document.getElementsByName(key);



        var value=0;
        if(obj[1].checked){
            value=2;
        }
        else if(obj[0].checked){
            value=1;
        }
        else{
            value=0;
        }

        data[key]=value;

        key="beef_pizza";
        obj=document.getElementsByName(key);
        value=0;
        if(obj[1].checked){
            value=2;
        }
        else if(obj[0].checked){
            value=1;
        }
        else{
            value=0;
        }

        data[key]=value;


        key="coke";
        obj=document.getElementsByName(key);
        value=0;
        if(obj[1].checked){
            value=2;
        }
        else if(obj[0].checked){
            value=1;
        }
        else{
            value=0;
        }

        data[key]=value;

        key="chip";
        obj=document.getElementsByName(key);
        value=0;
        if(obj[0].checked){
            value=1;
        }
        else{
            value=0;
        }



        data[key]=value;



        key="chick_pizza";
        obj=document.getElementsByName(key);
        value=0;
        if(obj[0].checked){
            value=1;
        }
        else{
            value=0;
        }


        data[key]=value;

        key="chick_wing";
        obj=document.getElementsByName(key);
        value=0;
        if(obj[0].checked){
            value=1;
        }
        else{
            value=0;
        }


        data[key]=value;



        obj=document.getElementById("phone").value;
        key="phone";
        data[key]=obj;


       var postData =  JSON.stringify(data);

        $.ajax({
            url: 'http://127.0.0.1:8000/commit/',
            type: 'GET',
            data: {'data':postData,
                    },
            traditional:true,//用传统方式序列化数据
            success:function(flag){
                alert(flag)
            }
        })//通过设置traditional属性为true直接传递数组 */




    }
