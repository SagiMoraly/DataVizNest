import { Box, useTheme } from "@mui/material";
import Header from "../../components/Header";
import Accordion from "@mui/material/Accordion";
import AccordionSummary from "@mui/material/AccordionSummary";
import AccordionDetails from "@mui/material/AccordionDetails";
import Typography from "@mui/material/Typography";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import { tokens } from "../../theme";

const FAQ = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  return (
    <Box m="20px">
      <Header title="FAQ" subtitle="Frequently Asked Questions Page" />

      <Accordion defaultExpanded>
        <AccordionSummary expandIcon={<ExpandMoreIcon />}>
          <Typography color={colors.greenAccent[500]} variant="h5">
            How am I?
          </Typography>
        </AccordionSummary>
        <AccordionDetails>
          <Typography>
            Hey I'm Sagi Moraly, I'm from Israel and my profession is web
            development.
          </Typography>
        </AccordionDetails>
      </Accordion>
      <Accordion defaultExpanded>
        <AccordionSummary expandIcon={<ExpandMoreIcon />}>
          <Typography color={colors.greenAccent[500]} variant="h5">
            Why did you make this site?
          </Typography>
        </AccordionSummary>
        <AccordionDetails>
          <Typography>
            I was looking at data analyst and wanted to see how to show data
            myself.
          </Typography>
        </AccordionDetails>
      </Accordion>
      <Accordion defaultExpanded>
        <AccordionSummary expandIcon={<ExpandMoreIcon />}>
          <Typography color={colors.greenAccent[500]} variant="h5">
            What tecnolegis did you use for front-end?
          </Typography>
        </AccordionSummary>
        <AccordionDetails>
          <Typography>
            I have used React with some TypeScript, for the charts I have used
            Nivo.
          </Typography>
        </AccordionDetails>
      </Accordion>
      <Accordion defaultExpanded>
        <AccordionSummary expandIcon={<ExpandMoreIcon />}>
          <Typography color={colors.greenAccent[500]} variant="h5">
            What tecnolegis did you use for back-end?
          </Typography>
        </AccordionSummary>
        <AccordionDetails>
          <Typography>
            In the back end I have a HTTP server of Python with MySQL database.
          </Typography>
        </AccordionDetails>
      </Accordion>
      <Accordion defaultExpanded>
        <AccordionSummary expandIcon={<ExpandMoreIcon />}>
          <Typography color={colors.greenAccent[500]} variant="h5">
            What do you want to add?
          </Typography>
        </AccordionSummary>
        <AccordionDetails>
          <Typography>I want to make the MySQL database on AWS.</Typography>
        </AccordionDetails>
      </Accordion>
    </Box>
  );
};

export default FAQ;
