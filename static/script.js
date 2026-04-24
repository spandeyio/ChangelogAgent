let chatHistory = [];

document.getElementById('fileInput').addEventListener('change', function(e) {
    const fileName = e.target.files[0] ? e.target.files[0].name : 'Select File (.md, .pdf)';
    e.target.parentElement.querySelector('span').textContent = fileName;
});

async function uploadFile() {
    const fileInput = document.getElementById('fileInput');
    const statusDiv = document.getElementById('uploadStatus');
    
    if (!fileInput.files || fileInput.files.length === 0) {
        statusDiv.textContent = 'Please select a file first.';
        return;
    }
    
    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append('file', file);
    
    statusDiv.textContent = 'Uploading...';
    
    try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });
        
        const data = await response.json();
        if (!response.ok) {
            statusDiv.textContent = `Error: ${data.detail || data.error}`;
        } else {
            statusDiv.textContent = data.message;
        }
    } catch (error) {
        statusDiv.textContent = `Error uploading file: ${error.message}`;
    }
}

function handleKeyPress(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
}

function appendMessage(role, content) {
    const chatBox = document.getElementById('chatBox');
    const msgDiv = document.createElement('div');
    msgDiv.className = `message ${role}`;
    if (role === 'agent') {
        // Strip markdown HTML blocks if the LLM ignores instructions
        let cleanContent = content.replace(/^```html\n/, '').replace(/```$/, '');
        msgDiv.innerHTML = cleanContent;
    } else {
        msgDiv.textContent = content;
    }
    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {
    const queryInput = document.getElementById('queryInput');
    const query = queryInput.value.trim();
    
    if (!query) return;
    
    // Add user message to UI
    appendMessage('user', query);
    queryInput.value = '';
    
    try {
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                query: query,
                history: chatHistory
            })
        });
        
        const data = await response.json();
        if (!response.ok) {
            throw new Error(data.detail || data.error || 'Failed to fetch response');
        }

        const agentResponse = data.response;
        
        // Add agent response to UI
        appendMessage('agent', agentResponse);
        
        // Update history
        chatHistory.push({ role: 'user', content: query });
        chatHistory.push({ role: 'agent', content: agentResponse });
        
        // Keep only last 10 pairs (20 messages)
        if (chatHistory.length > 20) {
            chatHistory = chatHistory.slice(chatHistory.length - 20);
        }
        
    } catch (error) {
        appendMessage('agent', `Error: ${error.message}`);
    }
}
