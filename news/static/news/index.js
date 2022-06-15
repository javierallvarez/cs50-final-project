// Use buttons to toggle between views
document.addEventListener('DOMContentLoaded', function() {
  // Switch on different views clicking on each link:
  const general = document.querySelector('#general')
  general.addEventListener('click', () => 
      loadTopic('general'));

  const music = document.querySelector('#music')
  music.addEventListener('click', () => 
      loadTopic('music'));

  const films = document.querySelector('#films')
  films.addEventListener('click',  () => 
      loadTopic('films'));

  const astronomy = document.querySelector('#astronomy')
  astronomy.addEventListener('click', () => 
      loadTopic('astronomy'));

  const technology =document.querySelector('#technology')
  technology.addEventListener('click', () => 
      loadTopic('technology'));



//---------------SEARCH-----------------

  const search = document.querySelector('#search')
  search.addEventListener('keyup', (e) => 
      searchTopic(e));

      
//---------------READLIST-----------------

  const add = document.querySelectorAll('.add');
  add.forEach(element => {
      element.addEventListener('click', () => {
          addToReadlist(element);
      });
  })

  const added = document.querySelectorAll('.added');
  added.forEach(element => {
      element.addEventListener('click', () => {
          delFromReadlist(element);
      })
  })
  
})



// Filter by topic by clicking the buttons:
function loadTopic(topic){
  const cards = document.querySelectorAll('.card');
  cards.forEach(card => {
    const cardTopic = card.getAttribute('data-id') ? card.getAttribute('data-id').toLowerCase() : null;
    if(topic === cardTopic){
      card.style.display = 'flex';
    } else {
      if (topic === 'general') {
        card.style.display = 'flex';
      } else {
        card.style.display = 'none';
      }
    }
  })
  if (topic == 'general') {
    document.querySelector("#general").classList.add("clicked");
    document.querySelector("#music").classList.remove("clicked");
    document.querySelector("#films").classList.remove("clicked");
    document.querySelector("#astronomy").classList.remove("clicked");
    document.querySelector("#technology").classList.remove("clicked");
  }
  else if (topic == 'music') {
    document.querySelector("#general").classList.remove("clicked");
    document.querySelector("#music").classList.add("clicked");
    document.querySelector("#films").classList.remove("clicked");
    document.querySelector("#astronomy").classList.remove("clicked");
    document.querySelector("#technology").classList.remove("clicked");  
  }
  else if (topic == 'films') {
    document.querySelector("#general").classList.remove("clicked");
    document.querySelector("#music").classList.remove("clicked");
    document.querySelector("#films").classList.add("clicked");
    document.querySelector("#astronomy").classList.remove("clicked");
    document.querySelector("#technology").classList.remove("clicked");  
  }
  else if (topic == 'astronomy') {
    document.querySelector("#general").classList.remove("clicked");
    document.querySelector("#music").classList.remove("clicked");
    document.querySelector("#films").classList.remove("clicked");
    document.querySelector("#astronomy").classList.add("clicked");
    document.querySelector("#technology").classList.remove("clicked");  
  }
  else if (topic == 'technology') {
    document.querySelector("#general").classList.remove("clicked");
    document.querySelector("#music").classList.remove("clicked");
    document.querySelector("#films").classList.remove("clicked");
    document.querySelector("#astronomy").classList.remove("clicked");
    document.querySelector("#technology").classList.add("clicked");  
  }
}


// Use the searching bar to filter between the news of the page:
function searchTopic(e) {
  // Take all the info and compare it with what the user writes in id="search":
  if (e.target.matches('#search')){
    // Iterate by all news:
    document.querySelectorAll('.card').forEach( item => {
      // Check what they return:
      console.log(item.innerText)
      // Pass all the info to lower case to do a comparison:
      item.innerText.toLowerCase().includes(e.target.value.toLowerCase())
      // Add or remove the display:none class on non chosen news:
      ?item.classList.remove('none')
      :item.classList.add('none')
    })
  }
}     


function addToReadlist(element) {
    let id = element.getAttribute("data-id");
    let readlistButton = document.querySelector(`#addToRead-${id}`);
    const form = new FormData();
    form.append("id", id);
    fetch("/add_to_readlist/", {
        method: 'POST',
        body: form
    })
    .then(res => res.json())
    .then(res => {
      console.log(res.status)
      readlistButton.classList.toggle("orange");    
    })
}

function delFromReadlist(element) {
    let id = element.getAttribute("data-id");
    let readlistButton = document.querySelector(`#delFromRead-${id}`);
    const form = new FormData();
    form.append("id", id);
    fetch("/add_to_readlist/", {
        method: 'POST',
        body: form
    })
    .then(res => res.json())
    .then(res => {
      readlistButton.classList.toggle("orange");
    })
}


// ---------------BURGUER-MENU------------------

let theToggle = document.getElementById('toggle');

// hasClass
function hasClass(elem, className) {
	return new RegExp(' ' + className + ' ').test(' ' + elem.className + ' ');
}
// addClass
function addClass(elem, className) {
    if (!hasClass(elem, className)) {
    	elem.className += ' ' + className;
    }
}
// removeClass
function removeClass(elem, className) {
	var newClass = ' ' + elem.className.replace( /[\t\r\n]/g, ' ') + ' ';
	if (hasClass(elem, className)) {
        while (newClass.indexOf(' ' + className + ' ') >= 0 ) {
            newClass = newClass.replace(' ' + className + ' ', ' ');
        }
        elem.className = newClass.replace(/^\s+|\s+$/g, '');
    }
}
// toggleClass
function toggleClass(elem, className) {
	var newClass = ' ' + elem.className.replace( /[\t\r\n]/g, " " ) + ' ';
    if (hasClass(elem, className)) {
        while (newClass.indexOf(" " + className + " ") >= 0 ) {
            newClass = newClass.replace( " " + className + " " , " " );
        }
        elem.className = newClass.replace(/^\s+|\s+$/g, '');
    } else {
        elem.className += ' ' + className;
    }
}

theToggle.onclick = function() {
   toggleClass(this, 'on');
   return false;
}




