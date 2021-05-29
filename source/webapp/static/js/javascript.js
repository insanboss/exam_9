


async function makeRequest(url, method='GET') {
        let response = await fetch(url, {method});
            if (response.ok) {  // нормальный ответ
                let resp = await response.json();
            return resp
            }
            else {            // ошибка
            let error = new Error(response.statusText);
            error.response = response;
            throw error;
            }
        }

        addPhoto = async (event)=>{
            event.preventDefault()
            let currentTarget = event.currentTarget
            let current_url = currentTarget.href
            try{
                 let result = await makeRequest(current_url)
                currentTarget.innerHTML = '<i class="fas fa-heart"></i>'
                currentTarget.setAttribute('href', current_url.replace('add_photo', "remove_photo"))
                currentTarget.onclick = removePhoto
                let id = currentTarget.dataset.counter
                let counter = document.getElementById(id)
                counter.innerText = result
            }
            catch (error){
                console.log(error);
            }
        }

        removePhoto = async (event) => {
            event.preventDefault()
            let currentTarget = event.currentTarget
            let current_url = currentTarget.href
            try {
                let result = await makeRequest(current_url)
                currentTarget.innerHTML = '<i class="far fa-heart"></i>'
                currentTarget.setAttribute('href', current_url.replace('remove_photo', 'add_photo'))
                currentTarget.onclick = addPhoto
                let id = currentTarget.dataset.counter
                let counter = document.getElementById(id)
                counter.innerText = result
            }
            catch (error) {
                console.log(error);
            }
        }