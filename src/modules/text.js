export default {
    initialize: (dom)=> {
        let div = document.createElement('div');
        div.style.cssText = "border: solid; width: 100%; height: 100%";
        div.innerHTML = 'AAA';
        dom.appendChild(div);
    }
}  
  