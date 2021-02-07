
function getCookie(cname) {
     var name = cname + "=";
     var ca = document.cookie.split(';');
     for(var i=0; i<ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1);
        if(c.indexOf(name) == 0)
           return c.substring(name.length,c.length);
     }
     return "";
}

 $(".delete-icon").click(function(e){
    e.preventDefault();
    if (confirm("Are you sure you want to delete user?")){
    var req_url = $(this).data("url")
        $.ajax({
            type: "POST",
            url: req_url,
            beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
            }
        })
    }
 });

 $("#add_user").click(function(e){
    e.preventDefault();
    window.location.href = $(this).data("url");
 });

 $(document).ajaxStop(function(){
    window.location.reload();
 });

 $(document).ready(function(){

 $("#flexCheckDefault").click(function(e){
        if(this.checked){
            $('input[type=checkbox]').each(function() { this.checked = true; });
        } else {
            $('input[type=checkbox]').each(function() { this.checked = false; });
        }
    });

});
