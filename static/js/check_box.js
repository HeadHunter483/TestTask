$(document).ready(function(){
    $(".task-checkbox").click(function(){
        var id = $(this).attr('id').substring(5)
        if ($(this).prop("checked")) {
            $.ajax({
                method: "GET",
                url: "/check/"+id,
                data: {list_id: id},
                success: function(data){
                let itemid = 'class_'+id;
                $('#'+itemid).addClass('striker secondary');
                }
            });
        }
        else {
            $.ajax({
                method: "GET",
                url: "/check/"+id,
                data: {list_id: id},
                success: function(data){
                let itemid = 'class_'+id;
                $('#'+itemid).removeClass('striker secondary');
                }
            });
        }
});
});