document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#fileChooser').addEventListener('click', (e) => fileChooser());
    document.querySelector('#registerImageFile').addEventListener('change', (e) => imageChange());

    document.onreadystatechange = () => {
        if (document.readyState === 'complete') {
            loaded()
        }
    }
});

function loaded() {
}

function fileChooser(e) {
    document.querySelector('#registerImageFile').click()
}

function imageChange(e) {
    const reader = new FileReader();
    reader.addEventListener("load", () => {
        const uploaded_image = reader.result;
        imageFile = document.querySelector('#imageFile')
        imageFile.src = `${uploaded_image}`;

        registerImageFile = document.querySelector('#registerImageFile')
        registerImageFile.src = `${uploaded_image}`;

        registerImage = document.querySelector('#registerImage')
        registerImage.src = `${uploaded_image}`;

        document.querySelector('#imageFile').style.display = '';
        document.querySelector('#defaultImageFile').style.display = 'none';
    })

    //sessionStorage.setItem('registerImageFile1', document.querySelector('#registerImageFile').files[0])
    reader.readAsDataURL(document.querySelector('#registerImageFile').files[0]);
    // reader.readAsDataURL(document.querySelector('#registerImage').files[0]);
}
