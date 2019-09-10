function initialize(dom) {
    // 一番外の枠
    let div = defaultFrame();

    // 時計の呼び出し
    let clock = document.createElement('iframe');
    clock.style.cssText =
        'position: absolute; top: 0px; left: 0px; border: 0; width: 100%; height: 100%; overflow: hidden;';
    clock.src = "http://tatikaze.com";
    div.appendChild(clock);

    dom.appendChild(div);
  }
  
  // 枠作成
  function defaultFrame() {
    let div = document.createElement('div');
    div.style.cssText = 'position: relative; border: solid; width: 100%; height: 100%; box-sizing: border-box;';
    return div;
  }
  
  export default {
    initialize
  }