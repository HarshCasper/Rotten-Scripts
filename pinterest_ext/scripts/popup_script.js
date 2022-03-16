document.querySelector('#add_pin').addEventListener('click', () => {
    chrome.windows.getCurrent({ populate: true }, window => {
        const site_to_pin = window.tabs.filter(tab => tab.active);

        chrome.runtime.sendMessage({
            message: 'add_pin',
            payload: {
                url: site_to_pin[0].url,
                destination_title: site_to_pin[0].title
            }
        });
    });
});

document.querySelector('#my_board').addEventListener('click', () => {
    chrome.runtime.sendMessage({
        message: 'open_board'
    });
});