const add_pin_modal = document.querySelector('.add_pin_modal');

document.querySelector('.add_pin').addEventListener('click', () => {
    add_pin_modal.style.opacity = 1;
    add_pin_modal.style.pointerEvents = 'all';
});

document.querySelector('.add_pin_modal').addEventListener('click', event => {
    if (event.target === add_pin_modal) {
        reset_modal();
    }
});

let pin_image_blob = null;

document.querySelector('#upload_img').addEventListener('change', event => {
    if (event.target.files && event.target.files[0]) {
        if (/image\/*/.test(event.target.files[0].type)) {
            const reader = new FileReader();

            reader.onload = function () {
                const new_image = new Image();

                new_image.src = reader.result;
                pin_image_blob = reader.result;

                new_image.onload = function () {
                    const modals_pin = document.querySelector('.add_pin_modal .modals_pin');

                    new_image.classList.add('pin_max_width');

                    document.querySelector('.add_pin_modal .pin_image').appendChild(new_image);
                    document.querySelector('#upload_img_label').style.display = 'none';

                    modals_pin.style.display = 'block';

                    if (
                        new_image.getBoundingClientRect().width < new_image.parentElement.getBoundingClientRect().width ||
                        new_image.getBoundingClientRect().height < new_image.parentElement.getBoundingClientRect().height
                    ) {
                        new_image.classList.remove('pin_max_width');
                        new_image.classList.add('pin_max_height');
                    }

                    modals_pin.style.opacity = 1;
                }
            }

            reader.readAsDataURL(event.target.files[0]);
        }
    }

    document.querySelector('#upload_img').value = '';
});

document.querySelector('.save_pin').addEventListener('click', () => {
    const users_data = {
        author: 'Jack',
        board: 'default',
        title: document.querySelector('#pin_title').value,
        description: document.querySelector('#pin_description').value,
        destination: document.querySelector('#pin_destination').value,
        img_blob: pin_image_blob,
        pin_size: document.querySelector('#pin_size').value,
        destination_title: document.querySelector('#pin_destination_title').value,
    }

    chrome.runtime.sendMessage({
        message: 'save_pin',
        payload: users_data
    }, response => {
        if (response.message === 'success') {
            create_pin(users_data);
            reset_modal();
        }
    });
});

const save_from_site = document.querySelector('.save_from_site'),
    save_from_site_input = document.querySelector('#save_from_site_input'),
    upload_image_url = document.querySelector('.upload_image_url'),
    cancel_image_url = document.querySelector('.cancel_image_url');

save_from_site.addEventListener('click', event => {
    if (event.target === save_from_site) {
        save_from_site.children[0].textContent = '';
        save_from_site.style.justifyContent = 'space-between';

        save_from_site_input.style.display = 'block';
        upload_image_url.style.display = 'flex';
        cancel_image_url.style.display = 'flex'
    } else if (event.target === upload_image_url) {
        const image_url = save_from_site_input.value;

        if (/\.(png|jpg|jpeg|gif)$/i.test(image_url)) {
            fetch(image_url)
                .then(res => res.blob())
                .then(res => {
                    const reader = new FileReader();

                    reader.onload = function () {
                        const new_image = new Image();

                        new_image.src = reader.result;
                        pin_image_blob = reader.result;

                        new_image.onload = function () {
                            const modals_pin = document.querySelector('.add_pin_modal .modals_pin');

                            new_image.classList.add('pin_max_width');

                            document.querySelector('.add_pin_modal .pin_image').innerHTML = '';
                            document.querySelector('.add_pin_modal .pin_image').appendChild(new_image);
                            document.querySelector('#upload_img_label').style.display = 'none';

                            modals_pin.style.display = 'block';

                            if (
                                new_image.getBoundingClientRect().width < new_image.parentElement.getBoundingClientRect().width ||
                                new_image.getBoundingClientRect().height < new_image.parentElement.getBoundingClientRect().height
                            ) {
                                new_image.classList.remove('pin_max_width');
                                new_image.classList.add('pin_max_height');
                            }

                            modals_pin.style.opacity = 1;
                        }
                    }

                    reader.readAsDataURL(res);
                })
                .catch(err => console.log(err));

            save_from_site.children[0].textContent = 'Save From Site';
            save_from_site.style.justifyContent = '';

            save_from_site_input.style.display = 'none';
            upload_image_url.style.display = 'none';
            cancel_image_url.style.display = 'none';
            save_from_site_input.value = ''
        }
    } else if (event.target === cancel_image_url) {
        save_from_site.children[0].textContent = 'Save From Site';
        save_from_site.style.justifyContent = '';

        save_from_site_input.style.display = 'none';
        upload_image_url.style.display = 'none';
        cancel_image_url.style.display = 'none';
        save_from_site_input.value = ''
    }
});



function create_pin(pin_details) {
    const new_pin = document.createElement('DIV');
    const new_image = new Image();

    new_image.src = pin_details.img_blob;
    new_pin.style.opacity = 0;

    new_image.onload = function () {
        new_pin.classList.add('card');
        new_pin.classList.add(`card_${pin_details.pin_size}`);
        new_image.classList.add('pin_max_width');

        new_pin.innerHTML = `<div class="pin_title">${pin_details.title}</div>
<div class="pin_modal">
    <div class="modal_head">
        <div class="save_card">Save</div>
    </div>
    <div class="modal_foot">
        <a href=${pin_details.destination} style="text-decoration: none;" target="_blank">
            <div class="destination">
                <div class="pint_mock_icon_container">
                    <img src="./images/pinterest-mock/upper-right-arrow.png" alt="destination" class="pint_mock_icon">
                </div>
                <span>${pin_details.destination_title}</span>
            </div>
        </a>
        <div class="pint_mock_icon_container">
            <img src="./images/pinterest-mock/send.png" alt="send" class="pint_mock_icon">
        </div>
        <div class="pint_mock_icon_container">
            <img src="./images/pinterest-mock/ellipse.png" alt="edit" class="pint_mock_icon">
        </div>
    </div>
</div>
<div class="pin_image">
</div>`;

        document.querySelector('.pin_container').appendChild(new_pin);
        new_pin.children[2].appendChild(new_image);

        if (
            new_image.getBoundingClientRect().width < new_image.parentElement.getBoundingClientRect().width ||
            new_image.getBoundingClientRect().height < new_image.parentElement.getBoundingClientRect().height
        ) {
            new_image.classList.remove('pin_max_width');
            new_image.classList.add('pin_max_height');
        }

        new_pin.style.opacity = 1;
    }
}


function reset_modal() {
    const modals_pin = document.querySelector('.add_pin_modal .modals_pin');

    add_pin_modal.style.opacity = 0;
    add_pin_modal.style.pointerEvents = 'none';
    document.querySelector('#upload_img_label').style.display = 'block';
    modals_pin.style.display = 'none';
    modals_pin.style.opacity = 0;

    if (modals_pin.children[0].children[0]) modals_pin.children[0].removeChild(modals_pin.children[0].children[0]);
    document.querySelector('#pin_title').value = '';
    document.querySelector('#pin_description').value = '';
    document.querySelector('#pin_destination').value = '';
    document.querySelector('#pin_size').value = '';
    pin_image_blob = null;
    document.querySelector('#pin_destination_title').value = '';
}

chrome.runtime.sendMessage({
    message: 'board_loaded'
}, response => {
    if (response.message === 'success') {
        document.querySelector('#pin_destination').value = response.payload.url;
        document.querySelector('#pin_destination_title').value = response.payload.destination_title;

        document.querySelector('.add_pin').click();
    }
});

chrome.runtime.sendMessage({
    message: 'get_pins'
}, response => {
    if (response.message === 'success') {
        response.payload.forEach(pin_data => {
            create_pin(pin_data);
        });
    }
});