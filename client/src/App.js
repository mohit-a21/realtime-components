import React, { useState, useEffect } from "react";
import { CopyToClipboard } from "react-copy-to-clipboard";
import "./styles.css";
import TextBox from "./TextBox";
import axios from "axios";

const defaultColors = [
  "#9253a1",
  "#f063a4",
  "#2dc5f4",
  "#fcee21",
  "#f16164",
  "#70327e",
  "#a42963",
  "#0b6a88",
  "#f89e4f",
  "#ec015a"
];

export default function App() {
  const [text, setText] = useState("");

  const [colors, setColors] = useState(
    defaultColors.sort(() => 0.5 - Math.random()).slice(0, 5)
  );

  useEffect(() => {
    if (text) {
      const fetchData = async () => {
        try {
          const response = await axios.post(
            "/generate_palette/text",
            {
              // JSON body data
              text: text
            }
          );

          setColors([
            response.data.text,
            response.data.background,
            response.data.primary,
            response.data.secondary,
            response.data.accent
          ]);
        } catch (error) {
          console.error(error);
        }
      };
      fetchData();
    }
  }, [text]);

  const [background, setBackground] = useState("#071415");
  const [current, setCurrent] = useState(null);

  useEffect(() => {
    const timeoutId = setTimeout(() => {
      setCurrent(null);
    }, 3000);
    return () => clearTimeout(timeoutId);
  }, [current]);

  return (
    <div className="App" style={{ background: background }}>
      <div>
        <TextBox onSubmit={setText} />
      </div>
      <div className="container">
        {colors.map((color, index) => (
          <div key={index} className="card">
            <div
              style={{
                background: color,
                filter: "brightness(85%)",
                boxShadow: color === background ? "0 0 5px #000" : ""
              }}
              className="box"
              onClick={() => setBackground(color)}
            />
            <CopyToClipboard text={`color: ${color};`}>
              <p
                style={{ color: color === background ? "#fff" : color }}
                onClick={() => setCurrent(color)}
              >
                {color}
              </p>
            </CopyToClipboard>
          </div>
        ))}
      </div>
    </div>
  );
}
