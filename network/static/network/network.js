document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#posts-view').addEventListener('change', (e) => viewPosts());
    document.querySelector('#sendPost').addEventListener('click', send_post);

    document.onreadystatechange = () => {
        if (document.readyState === 'complete') {
            loaded()
        }
    }

});

function loaded() {
}

 function viewPosts() {
     document.querySelector('#posts-view').style.display='block';



 }

 function send_post() {

  // Submit email and show sent mailbox
  document.querySelector('form').onsubmit = function (){
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