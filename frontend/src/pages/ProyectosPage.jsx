import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import { useEffect, useState } from "react";
import { getProyectoById } from "../api/proyectosService";
import PaginaRenderer from "../components/proyectos/PaginaRenderer";

function ProyectosPage() {
  const [project, setProject] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchProject = async () => {
      try {
        const data = await getProyectoById(1); // Fetch project with ID 1

        console.log(data);
        setProject(data);
      } catch (err) {
        setError(err);
      } finally {
        setLoading(false);
      }
    };

    fetchProject();
  }, []);

  if (loading) {
    return (
      <Box sx={{ p: 3 }}>
        <Typography variant="h6">Cargando proyecto...</Typography>
      </Box>
    );
  }

  if (error) {
    return (
      <Box sx={{ p: 3 }}>
        <Typography variant="h6" color="error">
          Error al cargar el proyecto: {error.message}
        </Typography>
      </Box>
    );
  }

  if (!project) {
    return (
      <Box sx={{ p: 3 }}>
        <Typography variant="h6">No se encontró el proyecto.</Typography>
      </Box>
    );
  }

  return (
    <Box sx={{ p: 3 }}>
      <Typography variant="h4" component="h1" gutterBottom>
        {project.nombre}
      </Typography>
      <Typography variant="body1" paragraph>
        {project.descripcion}
      </Typography>
      <Typography variant="subtitle1" gutterBottom>
        Tipo de Proyecto: {project.tipo_proyecto}
      </Typography>

      <Typography variant="h5" component="h2" sx={{ mt: 4, mb: 2 }}>
        Páginas del Proyecto:
      </Typography>
      <Box>
        {project.paginas && project.paginas.length > 0 ? (
          project.paginas.map((pagina) => (
            <PaginaRenderer key={pagina.id} pagina={pagina} />
          ))
        ) : (
          <Typography variant="body2">Este proyecto no tiene páginas.</Typography>
        )}
      </Box>
    </Box>
  );
}

export default ProyectosPage;
