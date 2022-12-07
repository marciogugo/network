document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#all-posts-view').addEventListener('change', (e) => viewPosts());
    document.querySelector('#button-like').addEventListener('click', () => like_post());
    document.querySelector('#button-unlike').addEventListener('click', () => unlike_post());
    document.querySelector('#button-edit').addEventListener('click', () => edit_post());
//    document.querySelector('#button-reply').addEventListener('click', () => reply_post());
    document.querySelectorAll('div.post-bt-reply').addEventListener('click', () => reply_post());

    document.onreadystatechange = () => {
        if (document.readyState === 'complete') {
            loaded()
        }
    }

    //By default load all posts
    viewPosts();
});


function loaded() {
}


function edit_post(id) {
    alert('edit post ' + id)
}


function reply_post() {
    const id = document.activeElement.getAttribute('name').replace(/\D/g,''); //only numbers

    if (id != null) {
        alert(id);
        document.querySelector('#compose-post-view').style.display = 'none';
        document.querySelector('#all-posts-view').style.display='block';
        document.querySelector('#edit-post-view').style.display='none';
        document.getElementById('post-bt-reply-'||id).style.display='block';
    }
  }


function like_post() {
    alert('user liked')
}

function unlike_post() {
    alert('user unliked')
}

function viewPosts() {
  // Show the posts view and hide other views
  document.querySelector('#compose-post-view').style.display = 'block';
  document.querySelector('#all-posts-view').style.display='block';
  document.querySelector('#edit-post-view').style.display='none';
  document.querySelector('#reply-post-view').style.display='none';

}

 function send_post() {

  // Submit email and show sent mailbox
  document.querySelector('Saveform').onsubmit = function (){
    const post_content = document.querySelector('#postContent').value;

    if (post_content !== undefined & post_content !== '') {
        fetch('/posts', {
            method: 'POST',
            body: JSON.stringify({
                postContent: post_content,
            })
          })
          .then(response => response.json())
          .then(result => {
              load_mailbox('sent')
          });
        } else {
          alert('Please, inform the content of the post!')
    }  
}
}