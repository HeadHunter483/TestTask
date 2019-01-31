$(document).ready(function(){
    $("#send").click(function(){
        var elemid = $(this).attr('id').substring(5)

        $.ajax({
        method: 'POST',
        url: '/post_new/'+elemid,
        data: {item: $("#item").val(), completed: $("#exampleFormControlSelect1 option:selected").val()}

    });

    });
});