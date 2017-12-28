document.getElementById( "plot_area" ).addEventListener( "click", function( event ) {
    var clickX = event.pageX ;
    var clickY = event.pageY ;

    var clientRect = this.getBoundingClientRect() ;
    var positionX = clientRect.left + window.pageXOffset ;
    var positionY = clientRect.top + window.pageYOffset ;

    var x = clickX - positionX ;
    var y = clickY - positionY ;
} ) ;

var points = 0;

$(this).on("click", function(e){
    $('body').append($("<p><label for='point_" + points + "'><input type='text' name='point_name_" + points + "' /></label></p><div class='color picker'>color picker</div><p><input type='text' name='point_x_" + points + "' value=" + x + " /></p><p><input type='text' name='point_y_" + points + "' value=" + y + " /></p>").css({
            position: 'absolute',
            left: e.pageX,
            top:  e.pageY,
            backgroundColor: "#aaaaaa"
    }));
    var points +=1;
});
