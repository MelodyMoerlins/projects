const profile = document.getElementById('profile');
const cart = document.getElementById('cart');
const search = document.getElementById('search');
const calendar = document.getElementById('calendar');
const help = document.getElementById('help');
const right = document.getElementById('right');
let hidden1 = document.getElementById('hidden');

function clicked(){
    document.getElementById('pictures').innerHTML = Image
}

function clickedFilters(){
    if(document.getElementById('hidden').style.display == "block"){
        document.getElementById('hidden').style.display = "none";
    } else{
        document.getElementById('hidden').style.display = "block";
        //document.getElementById('a').style.color = "e6ffff";
}}

function unPopular(){

}

function dblClicked(){
    document.getElementById('hidden').style.display = "none"
}


var books = ["EDUCATED", "THE GREAT GATSBY", "JAMES AND THE GIANT PEACH", "SOUL", "WALK INTO THE SHADOW", "HARRY POTTER AND THE DEATHY HALLOWS",];

var bookNames= ["Educated", "The Great Gatsby", "James and the Giant Peach", "SOUL", "Walk into the Shadow", "Harry Potter and the Deathy Hallows",]

function displayBooks(){
    let book1 = document.getElementById("searchbar").value

    let book = book1.toUpperCase()

    for (i=0; i<books.length; i++){
        if (books[i].includes(book)) {
            event.preventDefault()
           document.getElementById("answers").innerHTML+="<br>" + bookNames[i];} 

           else if(document.getElementById("answers").value==undefined){
            document.getElementById("answers").innerHTML= "This book is not in our database. Check your spelling and try again, or special order the book through your profile."
           }
     }
}
