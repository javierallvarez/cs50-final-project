document.addEventListener('DOMContentLoaded', function() {

    const onList = document.querySelectorAll('.on-list');
    onList.forEach(element => {
        element.addEventListener('click', () => {
            deleteFromReadlistPage(element);
        })
    })
})


// Delete items from the Readlist:
function deleteFromReadlistPage(element) {
    let id = element.getAttribute("data-id");
    let rdlCard = document.querySelector(`#readlist-card-${id}`)
    const form = new FormData();
    form.append("id", id);
    fetch("/add_to_readlist/", {
        method: 'POST',
        body: form
    })
    .then(res => res.json())
    .then(res => {      
    rdlCard.classList.add('none');  
    })
}  
  