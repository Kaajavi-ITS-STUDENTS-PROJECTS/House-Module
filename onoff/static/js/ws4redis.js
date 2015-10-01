var ws = new WebSocket('ws://index/ws/foobar?subscribe-broadcast&publish-broadcast&echo');
ws.onopen = function() {
    console.log("websocket connected");
};
ws.onmessage = function(e) {
    console.log("Received: " + e.data);
};
ws.onerror = function(e) {
    console.error(e);
};
ws.onclose = function(e) {
    console.log("connection closed");
}
function send_message(msg) {
    ws.send(msg);
}
