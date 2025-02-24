import React, { useState, useEffect } from "react";

function App() {
  const [items, setItems] = useState([]);
  const [newItem, setNewItem] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:5000/items")
      .then((response) => response.json())
      .then((data) => setItems(data))
      .catch((error) => console.error("Error fetching items:", error));
  }, []);

  const addItem = () => {
    fetch("http://127.0.0.1:5000/items", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text: newItem }),
    })
      .then((response) => response.json())
      .then((data) => {
        setItems([...items, data]);
        setNewItem("");
      })
      .catch((error) => console.error("Error adding item:", error));
  };

  const removeItem = (itemId) => {
    fetch(`http://127.0.0.1:5000/items/${itemId}`, {
      method: "DELETE",
    })
      .then((response) => {
        if (response.ok) {
          setItems(items.filter((item) => item.id !== itemId));
        } else {
          console.error("Error deleting item:", response.status);
        }
      })
      .catch((error) => console.error("Error deleting item:", error));
  };

  return (
    <div>
      {items.length === 0 ? (
        <p>Your to-do list is empty.</p>
      ) : (
        <ul>
          {items.map((item) => (
            <li key={item.id}>
              {item.text}{" "}
              <button onClick={() => removeItem(item.id)}>❌</button>
            </li>
          ))}
        </ul>
      )}

      <input
        type="text"
        placeholder="Add a new item"
        value={newItem}
        onChange={(e) => setNewItem(e.target.value)}
        style={{ marginRight: "5px" }}
      />
      <button onClick={addItem}>Add Item</button>
    </div>
  );
}

export default App;
