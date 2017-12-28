// jsファイルに書くこと

// plot範囲内のクリックされた相対位置を取得
// 取得した位置にPointを追加するフォームを表示
// 入力が完了したデータを仮に表示しておく（編集可）←？


// <div id="target">...</div>などの要素にクリックイベントを設定
document.getElementById( "plot_area" ).addEventListener( "click", function( event ) {
    var clickX = event.pageX ;
    var clickY = event.pageY ;

    // 要素の位置を取得
    var clientRect = this.getBoundingClientRect() ;
    var positionX = clientRect.left + window.pageXOffset ;
    var positionY = clientRect.top + window.pageYOffset ;

    // 要素内におけるクリック位置を計算
    var x = clickX - positionX ;
    var y = clickY - positionY ;
} ) ;

var points = 0;

$(this).on("click", function(e){
    $('body').append($("
        <p><label for='point_" + points + "'><input type='text' name='point_name_" + points + "' /></label></p>
        <div class='color picker'>color picker</div>
        <p><input type='text' name='point_x_" + points + "' value=" + x + " /></p>
        <p><input type='text' name='point_y_" + points + "' value=" + y + " /></p>
        ").css({
            position: 'absolute',
            left: e.pageX,
            top:  e.pageY,
            backgroundColor: "#aaaaaa"
    }));
    var points +=1;
});
