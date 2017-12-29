var points = 0;

document.getElementById( "plot_area" ).addEventListener( "click", function( event ) {
    points ++;

    var clickX = event.pageX ;
    var clickY = event.pageY ;

    var clientRect = this.getBoundingClientRect() ;
    var positionX = clientRect.left + window.pageXOffset ;
    var positionY = clientRect.top + window.pageYOffset ;

    var x = clickX - positionX ;
    var y = clickY - positionY ;

    $('#plot_area').append($("<div class='point_form'><p><label for='point_" + points + "'><input type='text' name='point_name_" + points + "' id='point_name_" + points + "' /></label></p><input type='text' name='point_x_" + points + "' value=" + x + " class='display_none' /><input type='text' name='point_y_" + points + "' value=" + y + " class='display_none' /></div>").css({
        position: 'absolute',
        left: clickX,
        top:  clickY,
    }));

    var focusElm = document.getElementById("point_name_" + points);
    focusElm.focus();

    console.log(points); //just for test
    return points;
});
