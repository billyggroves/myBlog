$(document).ready(function() {
  $("#login").click(function() {
    var inputs = {
      username : $('input#username').val(),
      password : $('input#password').val(),
    };

    console.log(inputs);

    $.getJSON('admin', inputs)
    .done(function(data, textStatus, jqXHR) {
        console.log(data.result);
        // alert(data.result);
        $('#contactForm').each(function(){
            this.reset();
        });
    })
    .fail(function(jqXHR, textStatus, errorThrown) {

        // log error to browser's console
        console.log(errorThrown.toString());
    });

  });
});
