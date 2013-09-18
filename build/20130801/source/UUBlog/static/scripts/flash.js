function flash(obj) {
    
	var timer;
	$(obj+" .mask img").click(
	function(){
		var index = $(obj+" .mask img").index($(this));	
		changeImg(index);
	}).eq(0).click();
		
	$(obj).find(".mask").animate({
		"bottom":"0"	
	}, 1500);
    
	$(obj).hover(
	function(){
		clearInterval(timer);	
	},
	function(){
		timer = setInterval(function(){
			var show = $(obj+" .mask img.show").index();
			if (show >= $(obj+" .mask img").length-1)
				show = 0;
			else
				show ++;
			changeImg(show);
		},3000);
	});
    
	function changeImg (index)
	{
		var currentMaskImg=$(obj+" .mask img").eq(index);
			
		$(obj+" .mask img").removeClass("show").eq(index).addClass("show");
		$(obj+" .mask .title").html(currentMaskImg.attr("alt"));
			
		$(obj+" .bigImg").parents("a").attr("href",currentMaskImg.attr("link"));
		$(obj+" .bigImg").hide().attr("src",currentMaskImg.attr("uri")).fadeIn("slow");
	}
	timer = setInterval(function(){
		var show = $(obj+" .mask img.show").index();
		if (show >= $(obj+" .mask img").length-1)
			show = 0;
		else
			show ++;
		changeImg(show);
	},3000);
}