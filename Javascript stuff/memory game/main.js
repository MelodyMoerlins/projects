let clickedCard = null;
let preventClick = false;
let combosFound = 0;

const colors= [
    'pink', 'yellow', 'red', 'cyan', 'blue', 'teal', 'orange', 'green',
]

const cards = [...document.querySelectorAll('.card')];
for (let color of colors){
    const cardAIndex = parseInt(Math.random() * cards.length);
    const cardA = cards['CardAIndex'];
    cards.splice(cardAIndex, 1);    
    cardA.className += `${color}`
    cardA.setAttribute('data-color', color);

    const cardBIndex = parseInt(Math.random() * cards.length);
    const cardB = cards['CardBIndex']
    cards.splice(cardAIndex, 1);
    cardB.className+= `${color}`
    cardB.setAttribute('data-color', color);
}
function onCardClicked(e){
    const target = e.currentTarget;
    if (target === clickedCard || target.className.includes('done')) {

    }
    target.className = target.className.replace('color-hidden', '')
    target.className += 'done';

    if (!clickedCard) {
        clickedCard = target;
    } else if (clickedCard) {
        if (clickedCard.getAttribute("data-color") === target.getAttribute("data-color")
        ){
            combosFound++;
            if (combosFound === 8){alert("YOU WIN")}
            console.log('cards are equal');
            clickedCard=null
        } else {
            console.log('cards aren\'t equal');
            preventClick = true;
            setTimeout(() =>{
                preventClick = true;
                clickedCard.className=clickedCard.className.replace('done', '').trim() + ' color-hidden';
                target.className=
                    target.className.replace('done', '').trim()  + ' color-hidden';
                    clickedCard=null;
            }, 500);
        }
    }

};
//24:00