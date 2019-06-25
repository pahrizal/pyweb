var to;
$(function(){
    $('a[ajax]').click(function(ev){
        ev.preventDefault();
        href = $(this).attr('href');
        loadpage(href);
    })
    loadpage('/dashboard')
})
function logout(){
    swal({
        title: 'Are you sure want to logout?',
        buttons: ['No, maybe later', 'Yes, please']
    }).then((yes) => {
        console.log(yes)
        if(yes){
            $.ajax({
                url: '/auth',
                method: 'DELETE',
                headers: {'jwt': localStorage.jwt},
                success: function(r){
                    if(r.state){
                        localStorage.clear();
                        window.location=r.redir
                    }
                }
            })
        }
    })
}
function loadpage(href,cb, onbackpressed){
    clearTimeout(to)
    $('#dimscreen').show();
    $.ajax({url: href, method: 'GET', headers: {jwt: localStorage.jwt}, success: function(ret){
        $('#dimscreen').hide();
        $('#content').html(ret);
        if(typeof cb == 'string'){
            eval(cb);
        }else if(typeof cb == 'function'){
            cb();
        }
    }});
    if(typeof onbackpressed == 'string'){
        $(document).on('keyup', function(e){
            if(e.which==27) loadpage(onbackpressed);
        })
    }else{
        $(document).unbind('keyup')
    }
}

function ajax(url, method, data, cb){
    $.ajax({
        url: url,
        method: method,
        headers:{'jwt': localStorage.jwt},
        data: data,
        success: cb

    });
}