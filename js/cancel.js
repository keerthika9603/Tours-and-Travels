
function sendEmail(){
    Email.send({
        Host : "smtp.gmail.com",
        Username : "keerthikam.20cse@kongu.edu",
        Password : "keerthi@kongu",
        To : 'keerthikam.20cse@kongu.edu',
        From : "gotrip.com",
        Subject : "tour Booking",
        Body : "Your Booking is cancelled Successfully..."
   }).then(
    message => alert(message));
}