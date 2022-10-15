// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getDatabase, ref, set } from "firebase/database";

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyChpBr5C781ArEOrydestQSHui-miNzbHU",
  authDomain: "fallhacks-2022.firebaseapp.com",
  projectId: "fallhacks-2022",
  storageBucket: "fallhacks-2022.appspot.com",
  messagingSenderId: "928206523983",
  appId: "1:928206523983:web:a4afe4bd1767bafb34e43a",
};

let count = 0;

function writeToDb(id, query, maxPrice, postalCode, radius) {
  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  const db = getDatabase();

  const reference = ref(db, "queries/" + id);
  set(reference, {
    query: query,
    maxPrice: maxPrice,
    postalCode: postalCode,
    radius: radius,
  });
}

// const elem = document.getElementById("para");

// writeToDb(0, "address", 1000, "abcdef", 10);
