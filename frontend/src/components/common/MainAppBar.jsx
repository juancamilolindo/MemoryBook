import {
  Avatar,
  Box,
  Button,
  Divider,
  IconButton,
  Menu,
  MenuItem,
  AppBar as MuiAppBar,
  Toolbar,
  Typography,
} from "@mui/material";
import { styled, useTheme } from "@mui/material/styles";
import React from "react";
import { Link } from "react-router-dom";

import AccountCircleIcon from "@mui/icons-material/AccountCircle";

// Componente AppBar estilizado
const StyledAppBar = styled(MuiAppBar)(({ theme }) => ({
  zIndex: theme.zIndex.drawer + 1,
  boxShadow: "none",
  backgroundColor: theme.palette.custom.backgroundLight,
  borderBottom: `1px solid ${theme.palette.divider}`,
}));

const APP_VERSION = "1.0.0"; // Placeholder para la versión de la app

function MainAppBar() {
  const [anchorEl, setAnchorEl] = React.useState(null);
  const openUserMenu = Boolean(anchorEl);
  const theme = useTheme();

  // Placeholder para el perfil de usuario (simulado)
  const userProfile = { name: "Usuario Demo", picture: "" };

  const handleMenu = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleCloseUserMenu = () => {
    setAnchorEl(null);
  };

  const handleUserLogout = () => {
    handleCloseUserMenu();
    console.log("Cerrar sesión"); // Placeholder para la lógica de logout
  };

  return (
    <StyledAppBar position="fixed">
      <Toolbar>
        {/* Logo de la empresa (opcional) */}
        {/* <img
          src={Logo} // Necesitarías importar tu logo aquí
          alt="MemoryBook Logo"
          style={{ height: '40px', marginRight: '8px' }}
        /> */}

        {/* Título de la aplicación */}
        <Typography
          variant="h6"
          noWrap
          component="div"
          sx={{ fontWeight: 600, mr: 2, color: theme.palette.custom.backgroundDark }}
        >
          MemoryBook
        </Typography>

        {/* Espaciador flexible para empujar la navegación a la derecha del título */}
        <Box sx={{ flexGrow: 1 }} />

        {/* --- NAVEGACIÓN PRINCIPAL --- */}
        <Box sx={{ display: { xs: "none", sm: "block" } }}>
          <Button
            key="mis-albumes"
            // component={Link} // Usar Link de react-router-dom cuando esté configurado
            // to="/mis-albumes"
            sx={{
              color: theme.palette.custom.menuText,
              fontWeight: 500,
              textTransform: "none",
              mx: 1,
            }}
          >
            Mis Álbumes
          </Button>
          <Button
            key="mis-proyectos"
            component={Link}
            to="/proyectos"
            sx={{
              color: theme.palette.custom.menuText,
              fontWeight: 500,
              textTransform: "none",
              mx: 1,
            }}
          >
            Mis Proyectos
          </Button>
          {/* Puedes añadir más botones de navegación aquí */}
        </Box>

        {/* Otro espaciador flexible para empujar el menú de usuario al final */}
        <Box sx={{ flexGrow: 1 }} />

        {/* Menú de Usuario con Avatar */}
        <div>
          <IconButton
            size="large"
            aria-label="account of current user"
            aria-controls="menu-appbar"
            aria-haspopup="true"
            onClick={handleMenu}
            color="inherit"
          >
            {userProfile && userProfile.picture ? (
              <Avatar
                alt={userProfile.name || "Usuario"}
                src={userProfile.picture}
                sx={{ width: 32, height: 32 }}
              />
            ) : (
              <Avatar sx={{ width: 32, height: 32 }}>
                {userProfile && userProfile.name ? (
                  userProfile.name.charAt(0).toUpperCase()
                ) : (
                  <AccountCircleIcon />
                )}
              </Avatar>
            )}
          </IconButton>
          <Menu
            id="menu-appbar"
            anchorEl={anchorEl}
            anchorOrigin={{ vertical: "top", horizontal: "right" }}
            keepMounted
            transformOrigin={{ vertical: "top", horizontal: "right" }}
            open={openUserMenu}
            onClose={handleCloseUserMenu}
            PaperProps={{
              sx: {
                borderRadius: 2,
                boxShadow: "0 4px 12px rgba(0, 0, 0, 0.1)",
                mt: "48px",
                borderBottom: `1px solid ${theme.palette.divider}`,
              },
            }}
          >
            {userProfile && (
              <MenuItem disabled>
                <Typography
                  variant="subtitle2"
                  sx={{ fontWeight: "bold", color: theme.palette.custom.menuText }}
                >
                  {userProfile.name}
                </Typography>
              </MenuItem>
            )}
            {/* <MenuItem
              // component={Link} // Usar Link de react-router-dom cuando esté configurado
              // to="/configuracion"
              onClick={handleCloseUserMenu}
              sx={{ color: theme.palette.custom.menuText }}
            >
              Configuración
            </MenuItem> */}
            <MenuItem
              onClick={handleUserLogout}
              sx={{ color: theme.palette.custom.menuText }}
            >
              Cerrar Sesión
            </MenuItem>
            {/* <MenuItem onClick={handleOpenReleaseNotes}>Novedades</MenuItem> */}
            <Divider sx={{ my: 0.5 }} />
            <MenuItem
              disabled
              sx={{
                cursor: "default",
                opacity: 1,
                "&:hover": { backgroundColor: "transparent" },
              }}
            >
              <Typography
                variant="caption"
                color="text.secondary"
                sx={{ width: "100%", textAlign: "right", pr: 1 }}
              >
                V {APP_VERSION}
              </Typography>
            </MenuItem>
          </Menu>
        </div>
      </Toolbar>
    </StyledAppBar>
  );
}

export default MainAppBar;
