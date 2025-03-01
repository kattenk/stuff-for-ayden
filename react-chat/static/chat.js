const Chat = () => {
  const [name, setName] = React.useState("");
  const [messages, setMessages] = React.useState([]);
  const [newMessageText, setNewMessageText] = React.useState("");

  React.useEffect(() => {
    fetch("http://172.16.1.4:5000/messages")
      .then((response) => response.json())
      .then((data) => setMessages(data))
      .catch((error) => console.error("Error fetching messages:", error));

    const socket = io("http://172.16.1.4:5000");
    socket.on("new_message", (newMessage) => {
      setMessages((prevMessages) => [...prevMessages, newMessage]);
      setNewMessageText("");
    });
  }, []);

  const sendMessage = () => {
    fetch("http://172.16.1.4:5000/messages", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ name: name, text: newMessageText }),
    })
  };

  return (
    <div>
      <input
        type="text"
        placeholder="Enter your name..."
        value={name} onChange={(e) => setName(e.target.value)}
      />

      <ul>
        {messages.map((message) => (
          <li key={message.id}>{message.name}: {message.text}</li>
        ))}
      </ul>
      
      <input
        type="text"
        placeholder="Write a message..."
        value={newMessageText}
        onChange={(e) => setNewMessageText(e.target.value)}
        style={{ marginRight: "5px" }}
      />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
};

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Chat />);