$(function () {

    $('#create_article').click(function(){
        window.open('/addblog/',target='_self');
    })

    $('#article_index').click(function(){
        window.open('/blogindex/',target='_self');
    })

    $('.title').click(function(){
        var $title = $(this);
        var article_id = $title.attr('article_id');
        window.open('/squirrelarticledetail/'+ article_id,target='_self');
    })
})