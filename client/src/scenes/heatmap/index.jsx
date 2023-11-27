import { Box } from "@mui/material";
import Header from "../../components/Header";
import HeatMap from "../../components/HeatMap";

const Heat = () => {
  return (
    <Box m="20px">
      <Header
        title="Heat Map"
        subtitle="Visualize the correlation matrix between numerical variables (e.g., age, starting balance, income)"
      />
      <Box height="75vh">
        <HeatMap />
      </Box>
    </Box>
  );
};

export default Heat;
