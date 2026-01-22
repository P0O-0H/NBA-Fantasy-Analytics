import {
    LineChart,
    Line,
    XAxis,
    YAxis,
    Tooltip,
    Legend,
    ResponsiveContainer
  } from "recharts";
  
  type Props = {
    data: {
      date: string;
      fantasy_points: number;
      rolling_FPoint_Last5: number;
      rolling_FPoint_Last10: number;
    }[];
  };
  
  export default function PlayerTimeseriesChart({ data }: Props) {
    return (
      <ResponsiveContainer width="100%" height={350}>
        <LineChart data={data}>
          <XAxis dataKey="date" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line
            type="monotone"
            dataKey="fantasy_points"
            stroke="#8884d8"
            dot={false}
            name="Fantasy Points"
          />
          <Line
            type="monotone"
            dataKey="rolling_FPoint_Last5"
            stroke="#82ca9d"
            dot={false}
            name="5-Game Avg"
          />
          <Line
            type="monotone"
            dataKey="rolling_FPoint_Last10"
            stroke="#ffc658"
            dot={false}
            name="10-Game Avg"
          />
        </LineChart>
      </ResponsiveContainer>
    );
  }