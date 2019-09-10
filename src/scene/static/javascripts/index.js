let modules = [];

let moduleNo = 0;

let addModule = function(moduleId, dom) {
    import('/scene/api/' + moduleId)
    .then((module) => {
        module.default.initialize(dom);
        modules.push(module.initialize);
    });
}


$(function() {

    let deleteMode = false;
    // var zoomScale = 1;

    $('.module').draggable({
        // grid: [30, 30],
        helper: 'clone',
        start: function(){
            // console.log("drag");
            $(this).addClass('drag');
        },
        stop: function(){
            $('.drag').removeClass('drag');
        }
    })

    $('#scene').droppable({
        accept: '.module',
        drop: function(event, ui){

            let clone = $('.drag').clone();
            clone.addClass('inDropArea');
            clone.attr('id', 'moduleid');


            // カーソルの位置にモジュール配置
            // console.log($("#scene").offset().top);
            // console.log(ui.position.top);
            let mouseTop = ui.position.top;         // カーソルの位置
            let sceneTop = $("#scene").offset().top;    // #sceneの上の座標
            let mouseLeft = ui.position.left;           // カーソルの位置
            let sceneLeft = $("#scene").offset().left;  // #sceneの上の座標
            let top = mouseTop - sceneTop - ((mouseTop - sceneTop) % 50);
            let left = mouseLeft - sceneLeft - ((mouseLeft - sceneLeft) % 50);


            // clone.css({position: 'absolute', top: top, left: left});
            // $(this).append(clone);

            moduleNo++;
            let frame = $('<div></div>', {
                id: moduleNo,
                css: {
                    position: 'absolute',
                    top: top,
                    left: left,
                    width: 100,
                    height: 100,
                },
            });

            $("#scene").append(frame)

            let moduleId = $('.drag').attr('data-id');
            addModule(moduleId, $('#' + moduleNo)[0]);

            // ドロップ後の要素にdraggableを付ける
            $('#' + moduleNo)
            .draggable({
                handle: 'div',
                containment: '#scene',
                grid: [50, 50],

                // 拡大率が変わってもマウスがずれないように
                // drag: function(e, ui) {
                //     ui.position.left = ui.position.left / zoomScale;
                //     ui.position.top  = ui.position.top / zoomScale;
                // }
            })
            .resizable({
                grid: [50, 50],
                // drag: function(e, ui) {
                //     ui.position.left = ui.position.left / zoomScale;
                //     ui.position.top  = ui.position.top / zoomScale;
                // }
            })
            .click(function() {
                if(deleteMode){
                    if(window.confirm('モジュールを削除します'))
                        $(this).remove();
                }
            })
        }
    });

    $('#delete').click(function() {
        if(deleteMode) {
            $(this).html('モジュール<br>削除');
            deleteMode = false;
            $(this).css('background-color', '');
        }
        else {
            $(this).html('削除モード');
            deleteMode = true;
            $(this).css('background-color', '#FF7575');
        }
    })

    // $("#scaleUp").click(function() {
    //     zoomScale += 0.1;
    //     $('#scene').css({transform: 'scale(' + zoomScale + ')'});
    // })
    // $("#scaleDown").click(function() {
    //     zoomScale -= 0.1;
    //     $('#scene').css({transform: 'scale(' + zoomScale + ')'});
    // })
    // $("#scaleReset").click(function() {
    //     zoomScale = 1;
    //     $('#scene').css({transform: 'scale(' + zoomScale + ')'});
    // })
})
