import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyBjWDqYKuHGf_HEv0voot52CDaBmXrQS8U",
  authDomain: "memorybook-476116.firebaseapp.com",
  projectId: "memorybook-476116",
  storageBucket: "memorybook-476116.firebasestorage.app",
  messagingSenderId: "211075419067",
  appId: "1:211075419067:web:ee791485b444de1e47529e",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

export { auth };
