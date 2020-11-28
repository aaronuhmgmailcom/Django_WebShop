function createxhr(){
        if(window.XMLHttpRequest){
            return new XMLHttpRequest();
        }else{
            return new ActiveXObject('Microsoft.XMLHTTP');
        }
    }