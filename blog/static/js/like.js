function clickLike(pk, csrf){
    console.log(
        "HELLo"
    )
    fetch(
        `/blog/${pk}/like/`,
        {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                "X-CSRFToken": csrf
            },
            method: "POST"
        }
    )
    .then(res => res.json())
    .then(res => {
        if(res.success === true){
            document.getElementById('like-count').innerHTML = parseInt(document.getElementById('like-count').innerHTML) +res['change']
            if(res.change === 1) {
                document.getElementById('like-btn').innerHTML = '<i class="zmdi zmdi-thumb-down"></i> Unlike'
            } else if (res.change === -1) {
                document.getElementById('like-btn').innerHTML = '<i class="zmdi zmdi-thumb-up"></i> Like'
            }
        }
    })
    .catch(err => console.log(err))
}