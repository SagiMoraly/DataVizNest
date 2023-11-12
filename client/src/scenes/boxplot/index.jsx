import { Box } from "@mui/material";
import Header from "../../components/Header";
import Boxplot from "../../components/BoxPlot";

const BoxPlot = () => {
  return (
    <Box m="20px">
      <Header title="Pie Chart" subtitle="Simple Pie Chart" />
      <Box height="75vh">
        <Boxplot />
      </Box>
    </Box>
  );
};

export default BoxPlot;
