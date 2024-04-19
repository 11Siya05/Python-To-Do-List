function updateclock(){
    const now = new Date();
    const year = now.getFullYear();
    const month = (now.getMonth()+1).toString().padStart(2,0);
    const day = now.getDate();
    const hours = now.getHours().toString().padStart(2,0);
    const minutes = now.getMinutes().toString().padStart(2,0);
    const seconds = now.getSeconds().toString().padStart(2,0);
    const dateString = `${year}-${month}-${day}`;
    const timeString = `${hours}-${minutes}-${seconds}`;
    document.getElementById("date").textContent=dateString;
    document.getElementById("time").textContent=timeString;


}

updateclock();
setInterval(updateclock,1000);