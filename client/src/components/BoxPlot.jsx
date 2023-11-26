import { ResponsiveBoxPlot } from "@nivo/boxplot";
import { tokens } from "../theme";
import { useTheme } from "@mui/material";
// import { mockDataBoxPlot as data } from "../data/mockData";
import { useEffect, useState } from "react";
import useHandler from "../hooks/useHandler.ts";

const BoxPlot = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const { handle_get_users_box_plot } = useHandler();
  const [APIdata, setAPIData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      let data = await handle_get_users_box_plot();
      setAPIData(data);
    };
    fetchData();
  }, []);
  return (
    <>
      {APIdata && (
        <ResponsiveBoxPlot
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
          margin={{ top: 60, right: 140, bottom: 60, left: 60 }}
          minValue={2000}
          maxValue={9000}
          subGroupBy="subgroup"
          padding={0.12}
          enableGridX={true}
          axisTop={{
            tickSize: 5,
            tickPadding: 5,
            tickRotation: 0,
            legend: "",
            legendOffset: 36,
          }}
          axisRight={{
            tickSize: 5,
            tickPadding: 5,
            tickRotation: 0,
            legend: "",
            legendOffset: 0,
          }}
          axisBottom={{
            tickSize: 5,
            tickPadding: 5,
            tickRotation: 0,
            legend: "group",
            legendPosition: "middle",
            legendOffset: 32,
          }}
          axisLeft={{
            tickSize: 5,
            tickPadding: 5,
            tickRotation: 0,
            legend: "value",
            legendPosition: "middle",
            legendOffset: -40,
          }}
          colors={{ scheme: "nivo" }}
          borderRadius={2}
          borderWidth={2}
          borderColor={{
            from: "color",
            modifiers: [["darker", 0.3]],
          }}
          medianWidth={2}
          medianColor={{
            from: "color",
            modifiers: [["darker", 0.3]],
          }}
          whiskerEndSize={0.6}
          whiskerColor={{
            from: "color",
            modifiers: [["darker", 0.3]],
          }}
          motionConfig="stiff"
          legends={[
            {
              anchor: "right",
              direction: "column",
              justify: false,
              translateX: 100,
              translateY: 0,
              itemWidth: 60,
              itemHeight: 20,
              itemsSpacing: 3,
              itemTextColor: "#999",
              itemDirection: "left-to-right",
              symbolSize: 20,
              symbolShape: "square",
              effects: [
                {
                  on: "hover",
                  style: {
                    itemTextColor: "#000",
                  },
                },
              ],
            },
          ]}
        />
      )}
    </>
  );
};

export default BoxPlot;
