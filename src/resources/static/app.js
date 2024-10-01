const roomId = "{{ room }}";    // 방 ID 설정
const ws = new WebSocket(`ws://127.0.0.1:8000/chat/ws/${roomId}`);  // WebSocket 연결 설정

// DOM 요소 가져오기
const messagesDiv = document.getElementById("messages");
const messageInput = document.getElementById("messageInput");

// WebSocket 연결이 열렸을 때 실행되는 이벤트 핸들러
ws.onopen = function() {
    const newMessage = document.createElement("p");
    newMessage.textContent = "You are connected!";
    newMessage.style.color = "green";  // 연결 상태를 색상으로 표시
    messagesDiv.appendChild(newMessage);
    scrollToBottom();  // 연결 후 스크롤을 맨 아래로
};

// 서버로부터 메시지 수신 시 실행되는 이벤트 핸들러
ws.onmessage = function(event) {
    const newMessage = document.createElement("p");
    newMessage.textContent = event.data;
    messagesDiv.appendChild(newMessage);
    scrollToBottom();  // 새로운 메시지 수신 후 스크롤을 맨 아래로
};

// WebSocket 연결이 닫혔을 때 실행되는 이벤트 핸들러
ws.onclose = function() {
    const newMessage = document.createElement("p");
    newMessage.textContent = "Disconnected from server.";
    newMessage.style.color = "red";  // 연결 종료 상태를 색상으로 표시
    messagesDiv.appendChild(newMessage);
    scrollToBottom();  // 연결 종료 후 스크롤을 맨 아래로
};

// Enter 키로 메시지 전송
messageInput.addEventListener("keyup", function(event) {
    if (event.key === "Enter") {
        sendMessage();  // Enter 키를 누르면 메시지 전송
        event.preventDefault();  // 기본 Enter 동작(줄바꿈)을 막음
    }
});

// 메시지 전송 함수
function sendMessage() {
    const message = messageInput.value.trim();  // 공백 제거 후 메시지 사용
    if (message && ws.readyState === WebSocket.OPEN) {
        ws.send(message);  // WebSocket을 통해 서버로 메시지 전송
        messageInput.value = "";  // 메시지 전송 후 입력 필드 초기화
        messageInput.focus();  // 전송 후 입력창에 포커스 유지
    } else {
        console.log("WebSocket is not open or message is empty.");
    }
}

// 스크롤을 맨 아래로 내리는 함수
function scrollToBottom() {
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}
