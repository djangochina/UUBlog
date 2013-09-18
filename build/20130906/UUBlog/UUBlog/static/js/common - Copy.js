$(document).ready(function() {
    selectPosition(null);
        
    {% if navInfo %}
    $("#parentId").val({{ navInfo.parent_id}});
    {% endif %}
});
        
function PadLeft(str,length,chars){
    var oldLength=str.length;
    var newLength=length-oldLength;
    if(newLength<1){
        return str;
                
    }
    for(var i=0;i<newLength;i++){
        str=chars+str;
    }
    return str;
                
}    
function buildTree(index,level)
    {
        var options="";
            
        {{navTree|safe}}
        //var data=Array();data[0]=[[4,'新闻']];data[4]=[[3,'国际']];data[3]=[[18,'222']];
            
        var navArray= data[index];
            
        /*undefined*/
        if (navArray==undefined){
            return options;
        }
        level+=1;
        for(var i=0;i<navArray.length;i++){
            
            options+="<option value='"+navArray[i][0]+"'>"+PadLeft(navArray[i][1],level,"-")+"</option>";
            options+=buildTree(navArray[i][0],level);
        }
            
        return options;
    }
            
function selectPosition(obj) {
    var options=buildTree(0);
    //alert(options);
    //options="<option>aaaa</option>"  
    $("#parentId").html(options);
                
    alert(PadLeft("q",5,"a"));
}
