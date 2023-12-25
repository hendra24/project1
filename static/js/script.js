console.log('jQuery script is executing');

$(document).ready(function() {
    // Your jQuery code here
    alert('jQuery is working!');
    setTimeout(function(){
        $('#message').fadeOut('slow');
    }, 4000);
});
