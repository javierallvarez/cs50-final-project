document.addEventListener('DOMContentLoaded', function() {
  const deleteComm = document.querySelectorAll('.delete')
  deleteComm.forEach(element => {
      element.addEventListener('click', () => {
        deleteComment(element);
      })
  });

  const edit = document.querySelectorAll('.edit');
    edit.forEach(element => {
        element.addEventListener('click', () => {
            editView(element);
        });
    });
  
  const form = document.getElementById('submit');
    form.addEventListener('click', (e) => {
      // Don't reload the page:
      e.preventDefault(); 
      // Execute this function instead:
      postComment();
    });  
});


// Get the date of posting of new comments and adapt it to the Django format: 
function newDate(){
  let months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
  let time = new Date();
  let day = time.getDate();
  let month = time.getMonth();
  let year = time.getFullYear();
  //let date = time.toDateString().substring(3,15);
  let hour = time.toLocaleTimeString().substring(0,5)
  let ampm = hour >= 12 ? 'p.m.' : 'a.m.'
  return date = months[month] + ' ' + day + ', ' + year + ', ' + hour + ' ' + ampm
}


  
function postComment() {
  //const form = document.getElementById('comm-form');
  let input = document.getElementById('comment-id').value;
  let user = document.getElementById('input-comment').getAttribute('data-user')
  let first_name = document.getElementById('input-comment').getAttribute('data-first_name')
  let last_name = document.getElementById('input-comment').getAttribute('data-last_name')
  let avatar = document.getElementById('input-comment').getAttribute('data-avatar')
  //let time = document.getElementById('input-comment').getAttribute('data-time')

  let date = newDate();

  let comments = document.querySelector('.comments');
  let div = document.createElement('div');
  let newsId = document.getElementById('input-comment').getAttribute('data-newsId');
  div.classList.add('comment-box');
  let data = new FormData();
  // data.append("id", id);
  data.append("comment", input);
  data.append("user",user);
  data.append("id",newsId)
  fetch("/post_comment/", {
    method: "POST",
    body: data
  })
  .then(res => res.json())
  .then((item) => {
      console.log(item)
    div.style.display = 'flex';
    div.innerHTML = 
            `
            <div class="little-avatar">
              <img src="${avatar}" alt=""> 
            </div>
            <div class="user-comment">
              <h4>${first_name} ${last_name}</h4>
              <small class="turq">@${user}</small>
              <div id="commentView-${item.comment_id}" class="comment-body">
                <p class="comment-text">${input}</p>
              </div> 
              <small class="gray">${date}</small>  
            <div> 
        
            <a class="edit" id="editComment-${item.comment_id}" data-id="${item.comment_id}" title="Edit Comment" style="cursor: pointer;">
                <i class="fa-solid fa-pen-to-square turq"></i>
            </a>
            <a class="delete" id="deleteComment-${item.comment_id}" data-id="${item.comment_id}" title="Delete Comment" style="cursor: pointer;">
                <i class="fa-solid fa-trash-can turq"></i>
            </a>
     
            </div>  
            `
    comments.insertAdjacentElement("afterbegin", div); 
    document.getElementById('comment-id').value = ''   
  });
}  



// Hide the alert message, set to 2000 miliseconds above.
function alertMsg(){
    let alert_message = document.querySelector('#alert_message');
    alert_message.style.display = 'none';
  }


function deleteComment(element) {
const id = element.getAttribute("data-id");
const comment = document.querySelector(`#comment-box-${id}`);
let alert_message = document.querySelector('#alert_message');
const form = new FormData();
form.append("id", id);
let alert = confirm("Are you sure to delete this?");
if (alert == true) {
    fetch("/delete/", {
        method: 'POST',
        body: form
    })
.then(res => res.json())
.then(res => {
        comment.style.display = 'none';
        alert_message.style.display = 'block';
        alert_message.innerHTML = 
                `<div class="alert-msg" role="alert">
                    Comment deleted succesfully. 
                </div>`;
                setTimeout('alertMsg()', 3000);
    });
  }
} 


// Create the form where the post will be edited:
function editComment(id, comment) {
  let editedComment = new FormData()
  editedComment.append("id", id);
  editedComment.append("comment", comment);
  fetch("/edit/", {
      method: "POST",
      body: editedComment
  })
  .then((res) => {
      console.log(res.status)
      document.querySelector(`#commentView-${id}`).textContent = comment;
      document.querySelector(`#commentView-${id}`).style.display = "block";
      document.querySelector(`#editView-${id}`).style.display = "none";
      document.querySelector(`#editView-${id}`).value = comment;
  });
}


function editView(element) {
  // Get the id of the selected element:
  let id = element.getAttribute("data-id");
  let editView = document.querySelector(`#editView-${id}`); 
  let commentView = document.querySelector(`#commentView-${id}`);
  // Hide the real post and show the edit view:
  editView.style.display = 'flex'; 
  commentView.style.display = 'none';
  // Create the Cancel button and hide the edit view:
  let cancelButton = document.querySelector(`#cancel-${id}`);
  cancelButton.addEventListener('click', () => { 
      editView.style.display = 'none'; 
      commentView.style.display = 'block';
  });
  // Create the Save button:
  let saveButton = document.querySelector(`#save-${id}`);
  saveButton.addEventListener('click', () => {
      editComment(id, document.querySelector(`#content-${id}`).value)
  });
}