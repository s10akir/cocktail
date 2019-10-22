function initialize(dom) {
	// 変数
    let fontSize = 15;
	let inSetting = false;

	// 一番外の枠
	let div = defaultFrame();

	// テキスト編集
	let textEditor = document.createElement('textarea');
	textEditor.style.cssText =
	  'position: absolute; top: 0px; left: 0px; border: 0; width: 100%; height: 100%; resize: none;  overflow: hidden; display: none; font-size: ' + fontSize + 'px';
	textEditor.setAttribute("placeholder", "文字を入力してください");
	div.appendChild(textEditor);

	// 設定ボタン
	let setting = document.createElement('input');
	setting.setAttribute('type', 'button');
	setting.setAttribute('value', '設定');
	setting.style.cssText = 'position: absolute; right: 0; width: 50px; height: 30px; border-radius: 5px; display: none; z-index: 1';
	div.appendChild(setting);

	// 保存ボタン
	let save = document.createElement('input');
	save.setAttribute('type', 'button');
	save.setAttribute('value', '保存');
	save.style.cssText = 'position: absolute; bottom: 0; left: 0; width: 50px; height: 25px; border-radius: 5px; display: none; z-index: 1';
	div.appendChild(save);

	// フォントサイズ +1
	let fontSizeUp = document.createElement('input');
	fontSizeUp.setAttribute('type', 'button');
	fontSizeUp.setAttribute('value', '+5');
	fontSizeUp.style.cssText = 'position: absolute; bottom: 30px; left: 0px; width: 25px; height: 25px; border-radius: 5px; display: none; z-index: 1';
	div.appendChild(fontSizeUp);

	// フォントサイズ -1
	let fontSizeDown = document.createElement('input');
	fontSizeDown.setAttribute('type', 'button');
	fontSizeDown.setAttribute('value', '-5');
	fontSizeDown.style.cssText = 'position: absolute; bottom: 30px; left: 30px; width: 25px; height: 25px; border-radius: 5px; display: none; z-index: 1';
	div.appendChild(fontSizeDown);

	// テキスト表示部分
	let textBox = document.createElement('div');
	textBox.setAttribute('class', 'data');
	textBox.style.cssText = 'width: 100%; height: 100%; word-wrap: break-word; font-size: ' + fontSize + 'px';
	textBox.innerHTML = '設定ボタンから編集できます';
	div.appendChild(textBox);

	// マウスオーバー時に設定ボタンの表示
	div.onmouseover = function() {
        if (!inSetting)
            setting.style.display = 'block';
	}

	// マウスアウト時に設定ボタンの非表示
	div.onmouseout = function() {
        setting.style.display = 'none';
	}

	// 設定ボタンが押された
	setting.onclick = function() {
        inSetting = true;

        //非表示要素を表示
        textEditor.style.display = 'block';
        save.style.display = 'block';
        fontSizeUp.style.display = 'block';
        fontSizeDown.style.display = 'block';
	}

	// 保存ボタンが押された
	save.onclick = function() {
        textBox.innerHTML = textEditor.value.replace(/\n/g, '<br>');  // 改行を<br>に

        textBox.style.fontSize = fontSize;   // フォントサイズの反映

        textEditor.style.display = 'none';
        save.style.display = 'none';
        fontSizeUp.style.display = 'none';
        fontSizeDown.style.display = 'none';
        inSetting = false;
	}

	// フォントサイズアップ
	fontSizeUp.onclick = function() {
        fontSize += 5;
        textEditor.style.fontSize = fontSize;
	}

	// フォントサイズダウン
	fontSizeDown.onclick = function() {
        fontSize -= 5;
        textEditor.style.fontSize = fontSize;
	}

	dom.appendChild(div);
}

  // 枠作成
function defaultFrame() {
    let div = document.createElement('div');
    div.classList.add('module');
    div.setAttribute('data-id', 'text');
    div.style.cssText = 'position: relative; border: solid; width: 100%; height: 100%; box-sizing: border-box;';
    return div;
}

function save(dom) {
    let element = dom.getElementsByClassName('data');

    let data = '';
    data += element[0].innerHTML;
    data += ',' + element[0].style.fontSize;
    // console.log(element);
    return data;
}

export default {
	initialize, save
}
