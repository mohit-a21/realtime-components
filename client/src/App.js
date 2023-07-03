import React, {useEffect, useState} from "react";
import {CopyToClipboard} from "react-copy-to-clipboard";
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

const linkGenerator = (endpoint, colors) => {
  return `${endpoint}${colors.map(str => str.substring(1)).join("-")}`;
}

const muzliPaletteLinkGenerator = (colors) => {
  return `https://colors.muz.li/palette/${colors.map(str => str.substring(1)).join("/")}`;
}

function generateContrastingColor(hexColor) {
  // Remove the # symbol if present
  hexColor = hexColor.replace("#", "");

  // Convert the hex color to RGB format
  const red = parseInt(hexColor.substring(0, 2), 16);
  const green = parseInt(hexColor.substring(2, 4), 16);
  const blue = parseInt(hexColor.substring(4, 6), 16);

  // Calculate the relative luminance of the color
  const luminance = (red * 0.299 + green * 0.587 + blue * 0.114) / 255;

  // Determine the contrast color based on the luminance
  return luminance > 0.5 ? "#000000" : "#ffffff";
}


export default function App() {
  const [text, setText] = useState("");
  const [typedText, setTypedText] = useState("");

  const [colors, setColors] = useState(
    defaultColors.sort(() => 0.5 - Math.random()).slice(0, 5)
  );

  const [reason, setReason] = useState("")

  const [background, setBackground] = useState("#071415");
  const [current, setCurrent] = useState(null);

  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (loading) {
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
          setReason(response.data.reason);
          setLoading(false);
        } catch (error) {
          console.error(error);
        }
      };
      fetchData();
    }
  }, [loading]);



  useEffect(() => {
    const timeoutId = setTimeout(() => {
      setCurrent(null);
    }, 3000);
    return () => clearTimeout(timeoutId);
  }, [current]);

  return (
    <div className="App" style={{background: background}}>
      <div style={{
        display: "flex",
        flexDirection: "column",
        justifyContent: "space-evenly",
        alignItems: "center",
        width: "100%",
        gap: "12px",
        flexWrap: "wrap"
      }}>
        <div>
          <h1 style={{color: generateContrastingColor(background)}}>
            Give a text prompt for a theme to generate a color palette using chat gpt
          </h1>
        </div>
        <div>
          <TextBox
            onTextChange={
              (t) => {
                setTypedText(t);
              }
            }
            onSubmit={
              (t) => {
                setText(t);
                setLoading(true);
              }
            }/>
        </div>
        <div>
          <h2 style={{color: generateContrastingColor(background)}}>
            {typedText}
          </h2>
        </div>
        <div>
          {
            loading ? <h2 style={{color: generateContrastingColor(background)}}>Loading...</h2> : null
          }
        </div>
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
                style={{
                  color: color === background ? "#fff" : color
                }}
                onClick={() => setCurrent(color)}
              >
                {color}
              </p>
            </CopyToClipboard>
          </div>
        ))}
        <div>

          <p style={{color: generateContrastingColor(background),}} align={"justify"}>
            {reason ? reason : null}
          </p>
        </div>
      </div>
      <div style={{
        display: "flex",
        flexDirection: "row",
        justifyContent: "space-evenly",
        width: "100%",
        gap: "10px",
        flexWrap: "wrap"
      }}>
        <div>
          <a href={linkGenerator("https://realtimecolors.com/?colors=", colors)} target={"_blank"}>
            <h2 style={{color: generateContrastingColor(background)}}>
              Realtime Colors
            </h2>
          </a>
        </div>

        <div>
          <a href={linkGenerator("https://coolors.co/", colors)} target={"_blank"}>
            <h2 style={{color: generateContrastingColor(background)}}>
              Coolors
            </h2>
          </a>
        </div>

        <div>
          <a href={muzliPaletteLinkGenerator(colors)} target={"_blank"}>
            <h2 style={{color: generateContrastingColor(background)}}>
              Muzli Palette
            </h2>
          </a>
        </div>
      </div>
    </div>
  );
}
