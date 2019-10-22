function initialize(dom) {
    // 一番外の枠
    let div = defaultFrame();

    // 時計の呼び出し
    let clock = document.createElement('iframe');
    clock.style.cssText =
        'position: absolute; top: 0px; left: 0px; border: 0; width: 100%; height: 100%; overflow: hidden; pointer-events: none;';
    clock.src = "https://script.google.com/macros/s/AKfycbx0tpIk34RkEfOAMysYzZdkuHnyv3xI2lDoYYlaEfRgt4RN1w/exec?data=clock";
    div.appendChild(clock);

    dom.appendChild(div);
}
  
  // 枠作成
function defaultFrame() {
    let div = document.createElement('div');
    div.classList.add('module');
    div.setAttribute('data-id', 'clock');
    div.style.cssText = 'position: relative; border: solid; width: 100%; height: 100%; box-sizing: border-box;';
    return div;
}

function save(dom){
    return null;
}

export default {
    initialize, save
}
