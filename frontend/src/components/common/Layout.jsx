import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import PropTypes from "prop-types";
import MainAppBar from "./MainAppBar";
import { Outlet } from "react-router-dom";

function Layout({ children }) {
  return (
    <Box sx={{ flexGrow: 1 }}>
      <MainAppBar />
      {/* Añadir margen superior para el AppBar fijo */}
      <Container component="main" maxWidth="md" sx={{ mt: "64px", p: 3 }}>
        {children}
        <Outlet />
      </Container>
    </Box>
  );
}

Layout.propTypes = {
  children: PropTypes.node.isRequired,
};

export default Layout;
