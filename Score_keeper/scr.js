const P1Display=document.querySelector("#pl1");
const P2Display=document.querySelector("#pl2");
const p1Btn=document.querySelector("#play1");
const p2Btn=document.querySelector("#play2");
const RST=document.querySelector("#rst");
const slc=document.querySelector("#ptsSel");

const sports_quotes = [
    "I've missed more than 9,000 shots in my career. I've lost almost 300 games. 26 times, I've been trusted to take the game-winning shot and missed. I've failed over and over and over again in my life. And that is why I succeed. - Michael Jordan",
    "I am the greatest. I said that even before I knew I was. - Muhammad Ali",
    "I don't count my sit-ups; I only start counting when it starts hurting because they're the only ones that count. - Muhammad Ali",
    "I've never lost a game; I just ran out of time. - Michael Jordan",
    "I've never been afraid to fail. - Michael Jordan",
    "You can't put a limit on anything. The more you dream, the farther you get. - Michael Phelps",
    "I've learned that something constructive comes from every defeat. - Tom Brady",
    "It's not the will to win that matters—everyone has that. It's the will to prepare to win that matters. - Paul Bryant",
    "You miss 100 percent of the shots you don't take. - Wayne Gretzky",
    "If you don't have confidence, you'll always find a way not to win. - Carl Lewis",
    "I've failed over and over and over again in my life. And that is why I succeed. - Michael Jordan",
    "I hated every minute of training, but I said, 'Don't quit. Suffer now and live the rest of your life as a champion.' - Muhammad Ali",
    "Push yourself again and again. Don't give an inch until the final buzzer sounds. - Larry Bird",
    "The more difficult the victory, the greater the happiness in winning. - Pele",
    "Talent is God-given. Be humble. Fame is man-given. Be grateful. Conceit is self-given. Be careful. - John Wooden",
    "You can't let praise or criticism get to you. It's a weakness to get caught up in either one. - John Wooden",
    "You don't win games on predictions; you win them on execution. - Tony Dungy",
    "The only way to prove that you're a good sport is to lose. - Ernie Banks",
    "When you've got something to prove, there's nothing greater than a challenge. - Terry Bradshaw",
    "The difference between the impossible and the possible lies in a person's determination. - Tommy Lasorda",
    "I've never lost a game. I just ran out of time. - Kobe Bryant",
    "To uncover your true potential, you must first find your own limits, and then you have to have the courage to blow past them. - Picabo Street",
    "The more difficult the victory, the greater the happiness in winning. - Pele",
    "It's hard to beat a person who never gives up. - Babe Ruth",
    "The harder the battle, the sweeter the victory. - Les Brown",
    "Champions keep playing until they get it right. - Billie Jean King",
    "I've failed over and over and over again in my life. And that is why I succeed. - Michael Jordan",
    "Success is no accident. It is hard work, perseverance, learning, studying, sacrifice, and most of all, love of what you are doing or learning to do. - Pele",
    "I've missed more than 9000 shots in my career. I've lost almost 300 games. 26 times, I've been trusted to take the game-winning shot and missed. I've failed over and over and over again in my life. And that is why I succeed. - Michael Jordan",
    "I've never been afraid to fail. - Michael Jordan",
    "It's not the size of the dog in the fight, but the size of the fight in the dog. - Archie Griffin",
    "When you've got something to prove, there's nothing greater than a challenge. - Terry Bradshaw",
    "To give any less than your best is to sacrifice a gift. - Steve Prefontaine",
    "Success is no accident. It is hard work, perseverance, learning, studying, sacrifice, and most of all, love of what you are doing or learning to do. - Pele",
    "I’ve failed over and over and over again in my life. And that is why I succeed. - Michael Jordan",
    "It's not whether you get knocked down, it's whether you get up. - Vince Lombardi",
    "You miss 100% of the shots you don't take. - Wayne Gretzky",
    "Winning isn't everything, it's the only thing. - Vince Lombardi",
    "I hated every minute of training, but I said, 'Don't quit. Suffer now and live the rest of your life as a champion.' - Muhammad Ali",
    "The more difficult the victory, the greater the happiness in winning. - Pele",
    "The only way to prove that you're a good sport is to lose. - Ernie Banks",
    "When you've got something to prove, there's nothing greater than a challenge. - Terry Bradshaw",
    "The difference between the impossible and the possible lies in a person's determination. - Tommy Lasorda",
    "I've never lost a game. I just ran out of time. - Kobe Bryant",
    "To uncover your true potential, you must first find your own limits, and then you have to have the courage to blow past them. - Picabo Street",
    "The more difficult the victory, the greater the happiness in winning. - Pele",
    "It's hard to beat a person who never gives up. - Babe Ruth",
    "The harder the battle, the sweeter the victory. - Les Brown",
    "Champions keep playing until they get it right. - Billie Jean King",
    "I've failed over and over and over again in my life. And that is why I succeed. - Michael Jordan",
    "Success is no accident. It is hard work, perseverance, learning, studying, sacrifice, and most of all, love of what you are doing or learning to do. - Pele",
    "I've missed more than 9000 shots in my career. I've lost almost 300 games. 26 times, I've been trusted to take the game-winning shot and missed. I've failed over and over and over again in my life. And that is why I succeed. - Michael Jordan",
    "I've never been afraid to fail. - Michael Jordan",
    "It's not the size of the dog in the fight, but the size of the fight in the dog. - Archie Griffin",
    "When you've got something to prove, there's nothing greater than a challenge. - Terry Bradshaw",
    "To give any less than your best is to sacrifice a gift. - Steve Prefontaine",
    "Success is no accident. It is hard work, perseverance, learning, studying, sacrifice, and most of all, love of what you are doing or learning to do. - Pele",
    "I’ve failed over and over and over again in my life. And that is why I succeed. - Michael Jordan",
    "It's not whether you get knocked down, it's whether you get up. - Vince Lombardi",
    "You miss 100% of the shots you don't take. - Wayne Gretzky",
    "Winning isn't everything, it's the only thing. - Vince Lombardi",
    "I hated every minute of training, but I said, 'Don't quit. Suffer now and live the rest of your life as a champion.' - Muhammad Ali",
    "The more difficult the victory, the greater the happiness in winning. - Pele",
    "The only way to prove that you're a good sport is to lose. - Ernie Banks",
    "When you've got something to prove, there's nothing greater than a challenge. - Terry Bradshaw",
    "The difference between the impossible and the possible lies in a person's determination. - Tommy Lasorda",
    "I've never lost a game. I just ran out of time. - Kobe Bryant",
    "To uncover your true potential, you must first find your own limits, and then you have to have the courage to blow past them. - Picabo Street",
    "The more difficult the victory, the greater the happiness in winning. - Pele",
    "It's hard to beat a person who never gives up. - Babe Ruth",
    "The harder the battle, the sweeter the victory. - Les Brown",
    "Champions keep playing until they get it right. - Billie Jean King",
    "I've failed over and over and over again in my life. And that is why I succeed. - Michael Jordan",
    "Success is no accident. It is hard work, perseverance, learning, studying, sacrifice, and most of all, love of what you are doing or learning to do. - Pele",
    "I've missed more than 9000 shots in my career. I've lost almost 300 games. 26 times, I've been trusted to take the game-winning shot and missed. I've failed over and over and over again in my life. And that is why I succeed. - Michael Jordan",
    "I've never been afraid to fail. - Michael Jordan",
    "It's not the size of the dog in the fight, but the size of the fight in the dog. - Archie Griffin",
    "When you've got something to prove, there's nothing greater than a challenge. - Terry Bradshaw",
    "To give any less than your best is to sacrifice a gift. - Steve Prefontaine",
    "Success is no accident. It is hard work, perseverance, learning, studying, sacrifice, and most of all, love of what you are doing or learning to do. - Pele",
    "I’ve failed over and over and over again in my life. And that is why I succeed. - Michael Jordan",
    "It's not whether you get knocked down, it's whether you get up. - Vince Lombardi",
    "You miss 100% of the shots you don't take. - Wayne Gretzky",
    "Winning isn't everything, it's the only thing. - Vince Lombardi",
    "I hated every minute of training, but I said, 'Don't quit. Suffer now and live the rest of your life as a champion.' - Muhammad Ali",
    "The more difficult the victory, the greater the happiness in winning. - Pele",
    "The only way to prove that you're a good sport is to lose. - Ernie Banks",
    "When you've got something to prove, there's nothing greater than a challenge. - Terry Bradshaw",
    "The difference between the impossible and the possible lies in a person's determination. - Tommy Lasorda",
    "I've never lost a game. I just ran out of time. - Kobe Bryant",
    "To uncover your true potential, you must first find your own limits, and then you have to have the courage to blow past them. - Picabo Street",
    "The more difficult the victory, the greater the happiness in winning. - Pele",
    "It's hard to beat a person who never gives up. - Babe Ruth",
    "The harder the battle, the sweeter the victory. - Les Brown",
    "Champions keep playing until they get it right. - Billie Jean King",
    "I've failed over and over and over again in my life. And that is why I succeed. - Michael Jordan",
    "Success is no accident. It is hard work, perseverance, learning, studying, sacrifice, and most of all, love of what you are doing or learning to do. - Pele",
    "I've missed more than 9000 shots in my career. I've lost almost 300 games. 26 times, I've been trusted to take the game-winning shot and missed. I've failed over and over and over again in my life. And that is why I succeed. - Michael Jordan",
    "I've never been afraid to fail. - Michael Jordan",
    "It's not the size of the dog in the fight, but the size of the fight in the dog. - Archie Griffin",
    "When you've got something to prove, there's nothing greater than a challenge. - Terry Bradshaw",
    "To give any less than your best is to sacrifice a gift. - Steve Prefontaine",
    "Success is no accident. It is hard work, perseverance, learning, studying, sacrifice, and most of all, love of what you are doing or learning to do. - Pele",
    "I’ve failed over and over and over again in my life. And that is why I succeed. - Michael Jordan"
]



let p1Score=0;
let p2Score=0;
let winscr=3
let isGameOver=false;

function newQuote(){
    var randomNum=Math.floor(Math.random()*(sports_quotes.length))
    document.getElementById('Qot').innerHTML=sports_quotes[randomNum];
}


p1Btn.addEventListener('click',function(){
    if (!isGameOver){
        p1Score+=1;
        P1Display.textContent=p1Score;
        if(p1Score===winscr){
            isGameOver=true;
            P1Display.classList.add('winner')
            P2Display.classList.add('loser')
        }
        
    }
    
})

p2Btn.addEventListener('click',function(){
    if (!isGameOver){
        p2Score+=1;
    
        if(p2Score===winscr){
            isGameOver=true;
            P2Display.classList.add('winner')
            P1Display.classList.add('loser')
        }
        P2Display.textContent=p2Score;
    }
    
})

RST.addEventListener('click',function(){
    isGameOver=false
    p1Score=0;
    p2Score=0;
    P1Display.textContent=p1Score;
    P2Display.textContent=p2Score;
    P1Display.classList.remove('winner','loser');
    P2Display.classList.remove('winner','loser');
    
    
})

slc.addEventListener('change',function(){
    winscr=parseInt(this.value);
    isGameOver=false
    p1Score=0;
    p2Score=0;
    P1Display.textContent=p1Score
    P2Display.textContent=p2Score
    P1Display.classList.remove('winner','loser');
    P2Display.classList.remove('winner','loser');
})


