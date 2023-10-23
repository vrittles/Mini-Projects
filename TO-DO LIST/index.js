const input=document.getElementById("input");
const addbtn=document.getElementById("addbtn")
const lists=document.getElementById("lists")
const warning=document.querySelector(".warning")
function addtask(){
    if (input.value ==='') {
        warning.innerHTML="Please Enter Any Task";
        // alert("please enter any task")
    }
    else{
let li=document.createElement("LI");
li.innerHTML=input.value;
lists.appendChild(li)
let span=document.createElement("span")
span.innerHTML="\u00d7";
li.appendChild(span)
warning.innerHTML="";

    }
    input.value="";
    saveData();
}
lists.addEventListener("click",function (e) {
    if(e.target.tagName==="LI"){
        e.target.classList.toggle("checked");
        saveData();
    }
    else if(e.target.tagName==="SPAN"){
        e.target.parentElement.remove();
saveData();
    }
},false);
function saveData() {
    localStorage.setItem("data",lists.innerHTML)
}
function showTask(){
    lists.innerHTML=localStorage.getItem("data")
}
showTask();
addbtn.addEventListener("click",addtask);
