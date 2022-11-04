document.addEventListener('DOMContentLoaded', function() {
//    document.querySelector('#imageFile').addEventListener('change', (e) => chooseImage());
//    document.querySelector('#defaultImageFile').addEventListener('change', (e) => chooseImage());
    document.querySelector('#fileChooser').addEventListener('click', (e) => fileChooser());
    document.querySelector('#i').addEventListener('change', (e) => imageChange());

    // document.onreadystatechange = () => {
    //     if (document.readyState === 'complete') {
    //         loaded()
    //     }
    // }
});

function fileChooser(e) {
    document.querySelector('#i').click() 
}

function imageChange(e) {
    const reader = new FileReader();
    reader.addEventListener("load", () => {
        const uploaded_image = reader.result;
        console.log(uploaded_image)
        imageFile = document.querySelector('#imageFile')
        imageFile.src = `${uploaded_image}`;
        document.querySelector('#imageFile').style.display = '';
        document.querySelector('#defaultImageFile').style.display = 'none';
    })

    sessionStorage.setItem('registerImageFile', document.querySelector('#i').files[0])
    reader.readAsDataURL(document.querySelector('#i').files[0]);

//     console.log(document.querySelector('#i').value);
//     var fakePath = document.querySelector('#i').value.toString().split('\\');
//     console.log(fakePath);
//     const uploaded_image = fakePath[fakePath.length - 1];
//     document.querySelector('#imageName').innerHTML = fakePath[fakePath.length - 1];

//     imageFile = document.querySelector('#imageFile')
//     imageFile.src = `${uploaded_image}`;
//     document.querySelector('#imageFile').style.display = '';
//     document.querySelector('#defaultImageFile').style.display = 'none';
// 
}

// function loaded() {
//     console.log('loaded')
//     document.querySelector('#defaultImageFile').style.display.style = 'block';
//     document.querySelector('#imageFile').style.display = 'none';

//     const image_input = document.querySelector("#image-input");

//     image_input.addEventListener("change", function() {
//         const reader = new FileReader();
//         reader.addEventListener("load", () => {
//             const uploaded_image = reader.result;

//             imageFile = document.querySelector('#imageFile')
//             imageFile.src = `${uploaded_image}`;
//             document.querySelector('#imageFile').style.display = '';
//             document.querySelector('#defaultImageFile').style.display = 'none';
//         });
//         reader.readAsDataURL(this.files[0]);
//     });
// }

function chooseImage(e) {
    // console.log('choose')
    // document.querySelector('#defaultImageFile').style.display.style = 'block';
    // document.querySelector('#imageFile').style.display = 'none';

    // const image_input = document.querySelector("#image-input");

    // image_input.addEventListener("change", function() {
    //     const reader = new FileReader();
    //     reader.addEventListener("load", () => {
    //         const uploaded_image = reader.result;

    //         imageFile = document.querySelector('#imageFile')
    //         imageFile.src = `${uploaded_image}`;
    //         document.querySelector('#imageFile').style.display = '';
    //         document.querySelector('#defaultImageFile').style.display = 'none';
    //     });
    //     reader.readAsDataURL(this.files[0]);
    // });
}    

function clearImage() {
    image_uploaded = false;
    document.getElementById('formFile').value = null;
    document.getElementById('buttonImage').style.display=image_uploaded?"":"none";
    frame.src = "";
}
