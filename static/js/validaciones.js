function Teclas(e, accept){
    var ascii = e.which|e.keyCode;
    var ret = false;
    vari1=ascii>=48 && ascii<=57
    vari2=ascii>=65 && ascii<=90 || ascii>=97 && ascii<=122 || ascii==241 || ascii==209 || ascii==32
    if (accept==1){
        if(vari1 || ascii==46 || ascii==44){
        ret=true;
        }
    }else if (accept==2){
        if (vari2){
        ret=true;
        }
    }else if (accept==3){
        if (vari1 || vari2 || ascii==45 || ascii==95 || ascii==64 || ascii==46){
        ret = true;
        }
    } 
    console.log(ascii);
    return ret;
}