var arr = [];


arr[0]= new Image();
arr[0].src = "{% static 'images/sgpot(7).jpg' %}";

arr[1]= new Image();
arr[1].src = "{% static 'images/sgpot(2).jpg' %}";

arr[2]= new Image();
arr[2].src = "{% static 'images/sgpot(3).jpg' %}";

arr[3]= new Image();
arr[3].src = "{% static 'images/sgpot(4).jpg' %}";

arr[4]= new Image();
arr[4].src = "{% static 'images/sgpot(11).jpg' %}";

arr[5]= new Image();
arr[5].src = "{% static 'images/sgpot(5).jpg' %}";

arr[6]= new Image();
arr[6].src = "{% static 'images/sgpot(6).jpg' %}";

arr[7]= new Image();
arr[7].src = "{% static 'images/sgpot(7).jpg' %}";

arr[8]= new Image();
arr[8].src = "{% static 'images/sgpot(8).jpg' %}";

arr[9]= new Image();
arr[9].src = "{% static 'images/sgpot(9).jpg' %}";

arr[10]= new Image();
arr[10].src = "{% static 'images/sgpot(10).jpg' %}";

arr[11]= new Image();
arr[11].src = "{% static 'images/sgpot(11).jpg' %}";

arr[12]= new Image();
arr[12].src = "{% static 'images/sgpot(12).jpg' %}";

arr[13]= new Image();
arr[13].src = "{% static 'images/sgpot(13).jpg' %}";

arr[14]= new Image();
arr[14].src = "{% static 'images/sgpot(14).jpg' %}";

arr[15]= new Image();
arr[15].src = "{% static 'images/sgpot(15).jpg' %}";

arr[16]= new Image();
arr[16].src = "{% static 'images/sgpot(16).jpg' %}";

arr[17]= new Image();
arr[17].src = "{% static 'images/sgpot(17).jpg' %}";

arr[18]= new Image();
arr[18].src = "{% static 'images/sgpot(18).jpg' %}";

arr[19]= new Image();
arr[19].src = "{% static 'images/sgpot(19).jpg' %}";

arr[20]= new Image();
arr[20].src = "{% static 'images/sgpot(20).jpg' %}";

var i=0;
function fn1()
{
    document.getElementById("id1").src=arr[i].src;
    i++;
    if(i==10)
    {
        i=0;
    }
}
var j=20;
function fn3()
{
    document.getElementById("id2").src=arr[j].src;
    j--;
    if(j==10)
    {
        j=20;
    }
}
function fn2()
{                
    setInterval(function(){fn1()},1500)
    setInterval(function(){fn3()},1500)
}