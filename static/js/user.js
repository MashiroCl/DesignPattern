

    function ObjData(key,value){
        this.Key=key;
        this.Value=value;
    }



    function cclick(){

        var array=[];
        var data={};
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
        var s=new ObjData(key,value); //创建键值对象
        array.push(s); //把对象放入对象数组中

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
        s=new ObjData(key,value); //创建键值对象
        array.push(s); //把对象放入对象数组中

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
        s=new ObjData(key,value); //创建键值对象
        array.push(s); //把对象放入对象数组中

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
        s=new ObjData(key,value); //创建键值对象
        array.push(s); //把对象放入对象数组中

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
        s=new ObjData(key,value); //创建键值对象
        array.push(s); //把对象放入对象数组中

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
        s=new ObjData(key,value); //创建键值对象
        array.push(s); //把对象放入对象数组中

        data[key]=value;



        // alert(array);
        // for(var i=0;i<array.length;i++){
        //     alert(array[i].Key+array[i].Value);
        // }
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
