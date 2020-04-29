import React, { useState } from "react";
import { TouchableOpacity, View, Text, Image } from "react-native";

import "./App.css";

function App() {
  const [quote, setQuote] = useState("");
  const [author, setAuthor] = useState("");
  const [imageAddress, setImageAddress] = useState("");

  const _handleGenerate = () => {
    fetch("http://127.0.0.1:8000/api/quote/", {
      method: "GET", // *GET, POST, PUT, DELETE, etc.
      mode: "cors", // no-cors, *cors, same-origin
      cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
      credentials: "same-origin", // include, *same-origin, omit
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((responseJson) => {
        setQuote(responseJson.text);
        setAuthor(responseJson.author);
      });

    fetch("http://127.0.0.1:8000/api/image_address/", {
      method: "GET", // *GET, POST, PUT, DELETE, etc.
      mode: "cors", // no-cors, *cors, same-origin
      cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
      credentials: "same-origin", // include, *same-origin, omit
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((responseJson) => {
        setImageAddress(responseJson.url);
      });
  };

  return (
    <View style={{ flex: 1 }}>
      <Text>{"Motivational Poster Generator"}</Text>
      <TouchableOpacity
        onPress={_handleGenerate}
        style={{ borderRadius: 5, backgroundColor: "lightblue", padding: 5 }}
      >
        <Text>{"Generate!"}</Text>
      </TouchableOpacity>
      <View
        style={{
          backgroundColor: "black",
          margin: 30,
          padding: 30,
          alignItems: "center",
        }}
      >
        <Image
          style={{ width: 640, height: 480, marginBottom: 30 }}
          source={{
            uri: imageAddress,
          }}
        />
        <View style={{ alignItems: "center" }}>
          <Text style={{ color: "white" }}>{quote}</Text>
          <Text style={{ color: "white" }}>{author}</Text>
        </View>
      </View>
    </View>
  );
}

export default App;
