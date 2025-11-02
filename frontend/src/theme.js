import { createTheme } from "@mui/material/styles";

const theme = createTheme({
  palette: {
    primary: {
      main: "#4A90E2",
    },
    background: {
      default: "#F5F5F5", // background-light
      paper: "#101c22", // background-dark
    },
    // Adding custom colors as per the user's request
    custom: {
      premiumAccent: "#F5A623",
      backgroundLight: "#f6f7f8",
      backgroundDark: "#101c22",
      menuText: "#616161",
    },
  },
  typography: {
    fontFamily: '"Manrope", sans-serif',
  },
  shape: {
    borderRadius: 4, // DEFAULT: "0.25rem"
  },
  components: {
    MuiCssBaseline: {
      styleOverrides: `
        body {
          background-color: #f6f7f8; /* Ensure body background matches background-light */
        }
      `,
    },
  },
});

export default theme;
