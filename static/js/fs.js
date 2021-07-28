$(document).ready(function () {
    $("#btn").click(function () {
        var a = $(this).attr('class');

        $.ajax({
            url: "http://127.0.0.1:8000/download",
            type: "POST",
            data: {
                id: '134kbps',
                class:a,
                csrfmiddlewaretoken:"99MBQR7OLyvoFEQkiBMVhKDigGz6n7DBw2C4pel0m9qzOgWeIVBIQi1R3ttzhBEo",
            },
            success: function(response){
                console.log(response);
            }
            
        });
        
    });
});