let modules = [];

let moduleNo = 0;

let addModule = function(moduleId, dom) {
    import('/scene/api/' + moduleId)
    .then((module) => {
        module.default.initialize(dom);
        modules.push(module);
    });
}


$(function() {

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
            let frame = $('<div></div', {
                id: moduleNo,
                class: 'use-module',
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
                    $(this).remove()
            }
    })
        }
    });

    let deleteMode = false;
    $('#delete').click(function() {
        if (deleteMode) {
            $(this).html("モジュール<br>削除");
            deleteMode = false;
            $(this).css('background-color', '')
        }
        else {
            $(this).html("削除モード");
            deleteMode = true;
            $(this).css('background-color', '#FF7575')
        }
    });

    $('#output').click(function() {
        // 各モジュールのデータ保管用の2次元配列の初期化
        let length = $('#scene').find('.use-module').length;
        let dataAry = new Array(length);
        for(let i = 0; i < length; i++){
            dataAry[i] = new Array(0);
        }

        // モジュールの外枠のデータ(親側で作ったほう)
        $('#scene').find('.use-module').each(function(index, element) {
            dataAry[index].push(element.style.top);
            // console.log('top : ' + element.style.top);

            dataAry[index].push(element.style.left);
            // console.log('left : ' + element.style.left);

            dataAry[index].push(element.style.height);
            // console.log('height : ' + element.style.height);

            dataAry[index].push(element.style.width);
            // console.log('width : ' + element.style.width);
        })

        // モジュール内部
        $('#scene').find('.module').each(function(index, element) {
            let moduleId = element.getAttribute('data-id');
            dataAry[index].push(moduleId)

            // console.log('module名 : ' + element.getAttribute('data-id'));

            import('/scene/api/' + moduleId)
            .then((module) => {
                let data = module.default.save(element);
                // console.log(data);
                dataAry[index].push(data);
            })
            .then(() => {
                if(index === length - 1){       // 最後のモジュールが終わったら
                    // alert(dataAry);
                    console.log(dataAry);
                }
            })
        })
    });



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

    // $("#preview").click(function() {
    //     console.log($('#scene').html());
    // })

    // $('#inputModule').click(function() {
    //     console.log($('#moduleText').val())
    //     $('#scene').append($('#moduleText').val());
    //     $('.ui-draggable').draggable({
    //         handle: 'div',
    //         containment: '#scene',
    //         grid: [50, 50],

    //         // 拡大率が変わってもマウスがずれないように
    //         // drag: function(e, ui) {
    //         //     ui.position.left = ui.position.left / zoomScale;
    //         //     ui.position.top  = ui.position.top / zoomScale;
    //         // }
    //     })
    //     $('.ui-resizable').resizable({
    //         grid: [50, 50],
    //         // drag: function(e, ui) {
    //         //     ui.position.left = ui.position.left / zoomScale;
    //         //     ui.position.top  = ui.position.top / zoomScale;
    //         // }
    //     });

    // })
})
