import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import PropTypes from "prop-types";

// Componente para renderizar un elemento individual (texto o imagen)
const ElementoRenderer = ({ elemento }) => {
  const { tipo_elemento, posicion_x, posicion_y, ancho, alto, rotacion, contenido } =
    elemento;

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

ElementoRenderer.propTypes = {
  elemento: PropTypes.shape({
    tipo_elemento: PropTypes.string.isRequired,
    posicion_x: PropTypes.number.isRequired,
    posicion_y: PropTypes.number.isRequired,
    ancho: PropTypes.number.isRequired,
    alto: PropTypes.number.isRequired,
    rotacion: PropTypes.number.isRequired,
    contenido: PropTypes.object.isRequired,
  }).isRequired,
};

// Componente para renderizar una página y sus elementos
const PaginaRenderer = ({ pagina }) => {
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
      {pagina.elementos.map((elemento) => (
        <ElementoRenderer key={elemento.id} elemento={elemento} />
      ))}
    </Box>
  );
};

PaginaRenderer.propTypes = {
  pagina: PropTypes.shape({
    id: PropTypes.number.isRequired,
    elementos: PropTypes.arrayOf(PropTypes.object).isRequired,
  }).isRequired,
};

export default PaginaRenderer;
