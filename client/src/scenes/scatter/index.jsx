import { Box } from "@mui/material";
import Header from "../../components/Header";
import ScatterPlot from "../../components/ScatterPlot";

const Scatter = () => {
  return (
    <Box m="20px">
      <Header
        title="Scatter Chart"
        subtitle="Age on the x-axis and starting balance on the y-axis. Each point represents a user, showing the relationship between age and starting balance"
      />
      <Box height="75vh">
        <ScatterPlot />
      </Box>
    </Box>
  );
};

export default Scatter;
