function httpGet(theUrl,callback)
{
    var xmlHttp = null;
    xmlHttp = new XMLHttpRequest();
	xmlHttp.open( "GET", theUrl, true );
    xmlHttp.send();
    xmlHttp.onload = callback;
    return xmlHttp.responseText;
}