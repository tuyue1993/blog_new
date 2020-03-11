$(function () {
    $('#create_article').click(function(){
        window.open('/addblog/',target='_self');
    })

    $('#article_index').click(function(){
        window.open('/blogindex/',target='_self');
    })

    $('#squirrel_article').click(function(){
        window.open('/squirrelindex/',target='_self');
    })


    // 随机数没办法从views里面生成传过来，html也不知道又什么办法可以
    // $('#random_article').click(function(){
    //     // var random_num = $(this).attr('random_num');
    //     $.getJSON('/random/',function (data) {
    //
    //         window.open('/articledetail/'+ data['random_num'],target='_self');
    //     })
    // })

    
    $('.title').click(function(){
        var $title = $(this);
        var article_id = $title.attr('article_id');
        window.open('/articledetail/'+ article_id,target='_self');
    })
})