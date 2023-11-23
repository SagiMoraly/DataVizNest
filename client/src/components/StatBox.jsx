import { Box, Button, Input, Typography, useTheme } from "@mui/material";
import { tokens } from "../theme";
import ProgressCircle from "./ProgressCircle";
import { useState } from "react";

const StatBox = ({
  title,
  subtitle,
  icon,
  progress,
  increase,
  button,
  input,
}) => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const [numberOfUsers, setNumberOfUsers] = useState("");
  const action = () => {
    if (button === "add") {
      console.log("add");
    } else {
      console.log("delete");
    }
  };

  return (
    <Box width="100%" m="0 30px">
      <Box display="flex" justifyContent="space-between">
        <Box>
          {icon}
          <Typography
            variant="h4"
            fontWeight="bold"
            sx={{ color: colors.grey[100] }}
          >
            {title}
          </Typography>
        </Box>
        <Box display="flex" justifyContent="space-between">
          {input && (
            <Box>
              <Input
                value={numberOfUsers}
                onChange={(e) => setNumberOfUsers(e.target.value)}
                sx={{
                  backgroundColor: colors.blueAccent[700],
                  color: colors.grey[100],
                  fontSize: "14px",
                  fontWeight: "bold",
                  padding: "10px 20px",
                  marginRight: "30px",
                }}
              />
            </Box>
          )}
          {button && (
            <Box>
              <Button
                onClick={() => action()}
                sx={{
                  backgroundColor: colors.blueAccent[700],
                  color: colors.grey[100],
                  fontSize: "14px",
                  fontWeight: "bold",
                  padding: "10px 20px",
                }}
              >
                {button}
              </Button>
            </Box>
          )}
        </Box>
      </Box>
      <Box display="flex" justifyContent="space-between" mt="2px">
        <Typography variant="h5" sx={{ color: colors.greenAccent[500] }}>
          {subtitle}
        </Typography>
        <Typography
          variant="h5"
          fontStyle="italic"
          sx={{ color: colors.greenAccent[600] }}
        >
          {increase}
        </Typography>
      </Box>
    </Box>
  );
};

export default StatBox;
