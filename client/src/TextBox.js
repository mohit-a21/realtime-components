import React, { useState } from "react";
import "./TextBox.css"; // Import the CSS file for styling

const TextBox = ({ onTextChange, onSubmit }) => {
  const [inputValue, setInputValue] = useState("");

  const handleInputChange = (e) => {
    setInputValue(e.target.value);
    onTextChange(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Perform any necessary actions with the submitted value
    console.log("Submitted value:", inputValue);
  };

  return (
    <form onSubmit={handleSubmit} className="textbox-container">
      <input
        type="text"
        value={inputValue}
        onChange={handleInputChange}
        className="textbox-input"
        placeholder="Enter your text"
        contentEditable={true}
      />
      <button
        type="submit"
        className="submit-button"
        onClick={() => {
          onSubmit(inputValue);
        }}
      >
        Submit
      </button>
    </form>
  );
};

export default TextBox;
