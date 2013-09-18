function FollowBlog(obj) {
    blog_id = $(obj).attr("id");
    dot = blog_id.indexOf("_");
    blogid = blog_id.substring(dot + 1);
    ajaxurl = "{% url 'blogajaxfollowblog' %}";
    postData = { "blogid": blogid };

    $.ajax({
        type: "GET",
        data: postData,
        url: ajaxurl,
        cache: false,
        dataType: "json",
        success: function (data, textStatus) {
            var follows = parseInt($("#follow_" + blogid).html());
            follows += 1;
            $("#follow_" + blogid).html(follows);

            $(obj).attr("value", "已关注");
            $(obj).attr("disabled", "disabled");
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {

        }
    });

    return false;
}
function SuggestBlog(obj) {
    blog_id = $(obj).attr("id");
    dot = blog_id.indexOf("_");
    blogid = blog_id.substring(dot + 1);
    ajaxurl = "{% url 'blogajaxsuggestblog' %}";
    postData = { "blogid": blogid };

    $.ajax({
        type: "GET",
        data: postData,
        url: ajaxurl,
        cache: false,
        dataType: "json",
        success: function (data, textStatus) {
            var suggestes = parseInt($("#suggest_" + blogid).html());
            suggestes += 1;
            $("#suggest_" + blogid).html(suggestes);
            $(obj).attr("value", "已推荐");
            $(obj).attr("disabled", "disabled");
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {

        }
    });

    return false;
}