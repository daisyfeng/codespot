var  api= window.api|| {
	key:'',
	init:function(){
		var 
		img=document.createElement("img");
		img.setAttribute('style','height:0px; width:0px;');
		img.setAttribute('src','http://fetchbot-api.appspot.com/tj?key='+api.key+'&url='+document.location+'&refer='+document.referrer);		
		document.body.appendChild(img);
	}
}