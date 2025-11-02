import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Layout from "../components/common/Layout";
import HomePage from "./HomePage";
import ProyectosPage from "./ProyectosPage";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<HomePage />} />
          <Route path="proyectos" element={<ProyectosPage />} />
        </Route>
      </Routes>
    </Router>
  );
}

export default App;
