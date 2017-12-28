var points = 0;

document.getElementById('plot_area').innerHTML = '_';

$(this).on("click", function(event){
    points ++;

    var clickX = event.pageX ;
    var clickY = event.pageY ;

    var clientRect = this.getBoundingClientRect() ;
    var positionX = clientRect.left + window.pageXOffset ;
    var positionY = clientRect.top + window.pageYOffset ;

    var x = clickX - positionX ;
    var y = clickY - positionY ;

    // $('plot_area').append($("<div class='point_form'><p><label for='point_" + points + "'><input type='text' name='point_name_" + points + "' /></label></p><div class='color picker'>color picker</div><p><input type='text' name='point_x_" + points + "' value=" + x + " /></p><p><input type='text' name='point_y_" + points + "' value=" + y + " /></p></div>").css({
    $('plot_area').append($("<p>add point here!</p>").css({
        position: 'absolute',
        left: clickX,
        top:  clickY,
        backgroundColor: "#aaaaaa"
    }));

    return points;
});
