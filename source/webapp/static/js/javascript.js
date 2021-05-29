const BASE_URL = 'http://localhost:8003'
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

let url = BASE_URL+'/photos/'
let button = document.getElementsByName('favorite_button')
async function makeRequest(url, method='GET', body) {
    let headers={
        'X-CSRFToken': getCookie('csrftoken')
    }
    let response;
    if(method === 'GET'){
        response = await fetch(url, {method})
    }
    else{
        response = await fetch(url, {method, headers:headers, body:body});
    }

    if (response.ok) {  // нормальный ответ
        return await response.json();
    } else {            // ошибка
        let error = new Error(response.statusText);
        error.response = response;
        throw error;
    }
}
button[0].onclick = async () =>{
    let res = await makeRequest(url)
    console.log(res)


}

