eel.expose(takeall);
function takeall(list){
    listfordoc= document.getElementById('ul');
    list.forEach(element => {
        a=0
        console.log(element)
        var para = document.createElement("tr"); 
        var node = document.createTextNode(element);
        while (a<4) {
            var para2 = document.createElement("td");
            var node = document.createTextNode(element[a]);
            para2.appendChild(node);
            para.appendChild(para2)
            a++
        }
        listfordoc.appendChild(para)
    });
}
function retu(){
    eel.returnall()
}