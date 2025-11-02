import React from "react";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";

// Componente para renderizar un elemento individual (texto o imagen)
const ElementRenderer = ({ element }) => {
  const { tipo_elemento, posicion_x, posicion_y, ancho, alto, rotacion, contenido } =
    element;

  const commonStyles = {
    position: "absolute",
    left: `${posicion_x}%`,
    top: `${posicion_y}%`,
    width: `${ancho}%`,
    height: `${alto}%`,
    transform: `rotate(${rotacion}deg)`,
    boxSizing: "border-box",
    overflow: "hidden",
  };

  if (tipo_elemento === "TEXTO") {
    return (
      <Box
        sx={{
          ...commonStyles,
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          color: contenido.color || "#000000",
          fontSize: contenido.font_size ? `${contenido.font_size}px` : "16px",
          textAlign: "center",
          wordBreak: "break-word",
        }}
      >
        <Typography variant="inherit" sx={{ lineHeight: 1 }}>
          {contenido.text}
        </Typography>
      </Box>
    );
  } else if (tipo_elemento === "IMAGEN") {
    return (
      <Box
        sx={{
          ...commonStyles,
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        <img
          src={contenido.url}
          alt={contenido.alt_text || "Elemento de imagen"}
          style={{
            maxWidth: "100%",
            maxHeight: "100%",
            objectFit: "contain",
          }}
        />
      </Box>
    );
  }

  return null;
};

// Componente para renderizar una página y sus elementos
const PageRenderer = ({ page }) => {
  return (
    <Box
      sx={{
        position: "relative",
        width: "100%",
        paddingBottom: "75%", // Aspect ratio 4:3 (height is 75% of width)
        backgroundColor: "#f0f0f0",
        border: "1px solid #ccc",
        borderRadius: "8px",
        overflow: "hidden",
        mb: 4,
        boxShadow: 3,
      }}
    >
      {page.elementos.map((element) => (
        <ElementRenderer key={element.id} element={element} />
      ))}
    </Box>
  );
};

export default PageRenderer;
