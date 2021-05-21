function quit(){
    window.close()
    eel.quitprogram()
}
function input(){
    const title = document.getElementById('title').value;
    const content = document.getElementById('content').value;
    const price = document.getElementById('price').value;
    console.log(title, content, price);
    eel.input1(title, content, price);
}
function delt(){
    const id = document.getElementById('inputfordelete').value
    eel.delete(id)
}
