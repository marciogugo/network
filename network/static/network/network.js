document.querySelector('#imageFile').addEventListener('click', () => preview());

function preview() {
    image_uploaded = true;
    frame.src = URL.createObjectURL(event.target.files[0]);

    sessionStorage.setItem('registerImageFile', event.target.files[0])

    document.getElementById("buttonID").style.display=image_uploaded?"":"none";
}    

function clearImage() {
    image_uploaded = false;
    document.getElementById('formFile').value = null;
    document.getElementById('buttonID').style.display=image_uploaded?"":"none";
    frame.src = "";
}
