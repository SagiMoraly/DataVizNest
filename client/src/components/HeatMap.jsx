import { ResponsiveHeatMap } from "@nivo/heatmap";
import { tokens } from "../theme";
import { useTheme } from "@mui/material";
// import { mockDataHeatMap as data } from "../data/mockData";
import { useEffect, useState } from "react";
import useHandler from "../hooks/useHandler.ts";

const HeatMap = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const { handle_get_users_heatmap } = useHandler();
  const [APIdata, setAPIData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      let data = await handle_get_users_heatmap();
      setAPIData(data);
    };
    fetchData();
  }, []);

  return (
    <>
      {APIdata && (
        <ResponsiveHeatMap
          data={APIdata}
          theme={{
            axis: {
              domain: {
                line: {
                  stroke: colors.grey[100],
                },
              },
              legend: {
                text: {
                  fill: colors.grey[100],
                },
              },
              ticks: {
                line: {
                  stroke: colors.grey[100],
                  strokeWidth: 1,
                },
                text: {
                  fill: colors.grey[100],
                },
              },
            },
            legends: {
              text: {
                fill: colors.grey[100],
              },
            },
          }}
          margin={{ top: 60, right: 90, bottom: 60, left: 90 }}
          valueFormat=">-.2s"
          labelTextColor={{
            from: "color",
            modifiers: [["darker", "1.9"]],
          }}
          axisTop={{
            tickSize: 5,
            tickPadding: 5,
            tickRotation: -90,
            legend: "",
            legendOffset: 46,
          }}
          axisRight={{
            tickSize: 5,
            tickPadding: 5,
            tickRotation: 0,
            legend: "country",
            legendPosition: "middle",
            legendOffset: 70,
          }}
          axisLeft={{
            tickSize: 5,
            tickPadding: 5,
            tickRotation: 0,
            legend: "country",
            legendPosition: "middle",
            legendOffset: -72,
          }}
          colors={{
            type: "diverging",
            scheme: "red_yellow_blue",
            divergeAt: 0.5,
            minValue: -1000,
            maxValue: 5000,
          }}
          emptyColor="#555555"
          legends={[
            {
              anchor: "bottom",
              translateX: 0,
              translateY: 30,
              length: 400,
              thickness: 8,
              direction: "row",
              tickPosition: "after",
              tickSize: 3,
              tickSpacing: 4,
              tickOverlap: false,
              tickFormat: ">-.2s",
              title: "Value →",
              titleAlign: "start",
              titleOffset: 4,
            },
          ]}
        />
      )}
    </>
  );
};

export default HeatMap;
