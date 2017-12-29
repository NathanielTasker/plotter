var point_num = 0;

document.getElementById( "plot_area" ).addEventListener( "dblclick", function( event ) {
    point_num ++;

    var clickX = event.pageX ;
    var clickY = event.pageY ;

    var clientRect = this.getBoundingClientRect() ;
    var positionX = clientRect.left + window.pageXOffset ;
    var positionY = clientRect.top + window.pageYOffset ;

    var x = clickX - positionX ;
    var y = clickY - positionY ;

    $('#plot_area').append($("<div class='point_form' id='point_form_" + point_num + "'><p><label for='point_" + point_num + "'><input type='text' name='point_name_" + point_num + "' id='point_name_" + point_num + "' /><span class='del_point' id='del_point_" + point_num + "'>&ensp;x</span></label></p><input type='hidden' name='point_x_" + point_num + "' value=" + x + " /><input type='hidden' name='point_y_" + point_num + "' value=" + y + " /></div>").css({
        position: 'absolute',
        left: clickX,
        top:  clickY,
    }));

    var focusElm = document.getElementById("point_name_" + point_num);
    focusElm.focus();

    console.log(point_num); //just for test
    return point_num;
});

// document.getElementById( "del_point_    //point_num    " ).addEventListener( "click", function( event ) {
//     $('#point_form_    //point_num    ').remove()
// }
