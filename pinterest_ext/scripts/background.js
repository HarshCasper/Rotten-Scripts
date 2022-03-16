let recent_tab_id = null,
    new_pin_data = {};


chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.message === 'add_pin') {
        new_pin_data = { ...request.payload };

        chrome.tabs.create({
            active: true,
            url: './board.html'
        }, tab => recent_tab_id = tab.id);
    } else if (request.message === 'board_loaded') {
        if (sender.tab.id === recent_tab_id) {
            sendResponse({
                message: 'success',
                payload: new_pin_data
            });

            recent_tab_id = null;
            new_pin_data = {};
        } else {
            sendResponse({ message: 'fail' });
        }

        return true;
    } else if (request.message === 'open_board') {
        chrome.tabs.create({
            active: true,
            url: './board.html'
        });
    } else if (request.message === 'save_pin') {
        chrome.storage.local.get('pins', data => {
            if (chrome.runtime.lastError) {
                sendResponse({ message: 'fail' });
                return;
            }

            chrome.storage.local.set({
                pins: data.pins ? [...data.pins, request.payload] : [request.payload]
            }, () => {
                if (chrome.runtime.lastError) {
                    sendResponse({ message: 'fail' });
                    return;
                }

                sendResponse({ message: 'success' });
            });
        });

        return true;
    } else if (request.message === 'get_pins') {
        chrome.storage.local.get('pins', data => {
            if (chrome.runtime.lastError) {
                sendResponse({ message: 'fail' });
                return;
            }

            sendResponse({
                message: 'success',
                payload: data.pins ? data.pins : []
            });
        });

        return true;
    }
});