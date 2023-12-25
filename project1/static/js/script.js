$(document).ready(function() {
    // Your jQuery code here
    console.log('jQuery script is executing');

    alert('jQuery is working!');
    setTimeout(function(){
        $('#message').fadeOut('slow');
    }, 4000);
});
