import React from "react";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";

function HomePage() {
  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        minHeight: "calc(100vh - 64px - 48px)", // Full viewport height minus AppBar height and Layout padding
      }}
    >
      <Typography variant="h5" component="p">
        Bienvenido a MemoryBook
      </Typography>
    </Box>
  );
}

export default HomePage;
